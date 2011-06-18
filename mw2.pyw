# Import the compiled UI module
import os, sys, platform
from PyQt4 import QtCore
from PyQt4.QtGui import QMainWindow, QDialog, QApplication, QMessageBox, QTreeWidgetItem, QFont, QFontMetrics, QColor, QIcon
from PyQt4.Qsci import QsciScintilla, QsciScintillaBase, QsciLexerTCL

from ui.Ui_F5Editor1 import Ui_mw_F5Editor
from ui.Ui_connect import Ui_dia_connect
from ui.Ui_createscript import Ui_dia_createscript
from ui.Ui_datagroups import Ui_dia_datagroups

import pycontrol.pycontrol as pc

__version__ = '0.0.1'
__author__ = 'j.rahm@f5.com'

ltm_rules = []
gtm_rules = []
# added 5/6/2011 - untested
active_rule = dict()

# Create a class for our main window
class Main(QMainWindow, Ui_mw_F5Editor):
	def __init__(self):
		QMainWindow.__init__(self)

		# This is always the same
		self.setupUi(self)
		# QActions on Editor Menubar / Toolbar
		self.actionConnect.triggered.connect(self.connectDialog)
		self.actionNew.triggered.connect(self.newDialog)
		#self.actionSave.triggered.connect(self.saveRule)
		self.actionRefresh.triggered.connect(self.refreshRules)
		self.actionAbout_F5_Editor.triggered.connect(self.about)
		self.actionData_Group_Editor.triggered.connect(self.dgDialog)
		self.treeWidget_iRulesList.itemClicked.connect(self.displayRule)

		self.textEdit_ScriptCanvas.clear()
		# define the font
		font = QFont()
		font.setFamily('Consolas')
		font.setFixedPitch(True)
		font.setPointSize(9)
		# font metrics will help build margins
		fm = QFontMetrics(font)
		# set default font for lines / linenumbers
		self.textEdit_ScriptCanvas.setFont(font)
		self.textEdit_ScriptCanvas.setMarginsFont(font)
		# line numbers
		self.textEdit_ScriptCanvas.setMarginWidth(0, fm.width('0000') + 5)
		self.textEdit_ScriptCanvas.setMarginLineNumbers(0, True)
		# Edge Mode
		self.textEdit_ScriptCanvas.setEdgeMode(QsciScintilla.EdgeLine)
		self.textEdit_ScriptCanvas.setEdgeColumn(80)
		self.textEdit_ScriptCanvas.setEdgeColor(QColor('#FF0000'))
		# folding
		self.textEdit_ScriptCanvas.setFolding(QsciScintilla.BoxedTreeFoldStyle)
		# Braces Matching
		self.textEdit_ScriptCanvas.setBraceMatching(QsciScintilla.SloppyBraceMatch)
		# active line color
		self.textEdit_ScriptCanvas.setCaretLineVisible(True)
		self.textEdit_ScriptCanvas.setCaretLineBackgroundColor(QColor('#CCCCCC'))
		#margins colors
		# line number colors
		self.textEdit_ScriptCanvas.setMarginsBackgroundColor(QColor('#000000'))
		self.textEdit_ScriptCanvas.setMarginsForegroundColor(QColor('#FFFFFF'))
		# fold colors
		self.textEdit_ScriptCanvas.setFoldMarginColors(QColor('#99CC66'), QColor('#333300'))
		# lexer
		lex = QsciLexerTCL()
		lex.setDefaultFont(font)
		self.textEdit_ScriptCanvas.setLexer(lex)
		self.textEdit_ScriptCanvas.setText('\n\n\n\t\tAre you ready to iRule?')

	def displayRule(self, item):
		self.textEdit_ScriptCanvas.clear()
		for i in ltm_rules:
			if i.rule_name == item.text(0):
				self.textEdit_ScriptCanvas.setText(i.rule_definition)
				# added 5/6/2011 - untested
				#active_rule[i.rule_name] = i.rule_definition
		for i in gtm_rules:
			if i.rule_name == item.text(0):
				self.textEdit_ScriptCanvas.setText(i.rule_definition)
				# added 5/6/2011 - untested
				#active_rule[i.rule_name] = i.rule_definition

	#def saveRule(self):
	#
	#    try:
	#        ltm.modify_rule(rule_names = [active_rule.keys()[0]])

	def connectDialog(self):
		if self.actionConnect.isChecked():
			self.connectdlg = ConnectDlg()
			self.connectdlg.exec_()
			if self.connectdlg.result() == QDialog.Accepted:
				ltm, gtm, dg, sysinfo = self.get_objects(self.connectdlg.host, self.connectdlg.uname, self.connectdlg.upass)
				self.loadData(ltm, gtm, dg, sysinfo)
				self.labelSyntaxCheckResults.clear()
				self.labelSyntaxCheckResults.setText('Connected to %s' % self.connectdlg.host)
				self.actionConnect.setIcon(QIcon('icons/default/ToolbarDisconnect.png'))
				self.actionConnect.setText('Disconnect')
		else:
			self.labelSyntaxCheckResults.setText('Disconnected')
			self.actionConnect.setIcon(QIcon('icons/default/ToolbarConnect.png'))
			self.actionConnect.setText('Disconnect')
			self.textEdit_ScriptCanvas.clear()
			self.treeWidget_iRulesList.clear()

	def refreshRules(self):
		if self.actionConnect.isChecked():
			self.labelSyntaxCheckResults.setText('Refreshing...')
			self.textEdit_ScriptCanvas.clear()
			self.treeWidget_iRulesList.clear()
			# where do I pass ltm, gtm, dg, sysinfo into this refresh def?
			self.loadData(ltm, gtm, dg, sysinfo)
			self.labelSyntaxCheckResults.setText('Rules refreshed.')

	def get_objects(self, host, uname, upass):
		try:
			b = pc.BIGIP(
				hostname = host,
				username = uname,
				password = upass,
				fromurl = True,
				wsdls = ['LocalLB.Rule', 'LocalLB.Class', 'GlobalLB.Rule', 'System.SystemInfo'])

			ltm = b.LocalLB.Rule
			gtm = b.GlobalLB.Rule
			dg = b.LocalLB.Class
			sysinfo = b.System.SystemInfo

			return (ltm, gtm, dg, sysinfo)

		except Exception, e:
			qmb = QMessageBox()
			QMessageBox.about(qmb, 'Error', '''<b>Connection Error</b><p>%s''' % e)

	def loadData(self, ltm, gtm, dg, sysinfo):
		self.treeWidget_iRulesList.clear()
		self.treeWidget_iRulesList.setColumnCount(1)
		self.treeWidget_iRulesList.setHeaderLabels(["Rules"])
		self.treeWidget_iRulesList.setItemsExpandable(True)

		# Get LTM & GTM iRules
		global ltm_rules, gtm_rules
		ltm_rules = ltm.query_all_rules()
		gtm_rules = gtm.query_all_rules()

		# Get Datagroups
		#ltm_dg_addr = dg.get_address_class(class_names = dg.get_address_class_list())
		#ltm_dg_str = dg.get_string_class(class_names = dg.get_string_class_list())
		#ltm_dg_int = dg.get_value_class(class_names = dg.get_value_class_list())
		#ltm_dg_ext = dg.get_external_class_list()

		# Get System Info
		ltm_sysinfo = sysinfo.get_system_information()

		hdr = QTreeWidgetItem(['gtm'])
		self.treeWidget_iRulesList.addTopLevelItem(hdr)
		self.treeWidget_iRulesList.expandItem(hdr)
		i = []
		for i in [x.rule_name for x in gtm_rules]:
			rule = QTreeWidgetItem(hdr, [i])
			self.treeWidget_iRulesList.addTopLevelItem(rule)

		hdr = QTreeWidgetItem(['ltm'])
		self.treeWidget_iRulesList.addTopLevelItem(hdr)
		self.treeWidget_iRulesList.expandItem(hdr)
		i = []
		for i in [x.rule_name for x in ltm_rules]:
			rule = QTreeWidgetItem(hdr, [i])
			self.treeWidget_iRulesList.addTopLevelItem(rule)

		self.treeWidget_iRulesList.resizeColumnToContents(0)

	def newDialog(self):
		self.newdlg = NewDlg()
		self.newdlg.show()

	def dgDialog(self):
		self.dgdlg = DgDlg()
		self.dgdlg.show()

	def about(self):
		QMessageBox.about(self, "About F5 Editor",
			   """<b> F5 Editor </b> v %s
				<p>The Initial Developer of the Original
		Code is F5 Networks, Inc. Seattle, WA, USA. 
		Portions created by F5 are Copyright (C) 2011
		F5 Networks, Inc. All Rights Reserved. iControl
		(TM), BIG-IP and iRules are registered trademarks
		or trademarks of F5 Networks, Inc. in the U.S. 
		and certain other countries.  F5 Networks'
		trademarks may not be used in connection with any
		product or service except as permitted in writing 
		by F5. Released in accordance with GPL v3 or later 
		- NO WARRANTIES!<p>Python %s - pyControl %s - on %s""" % \
		(__version__, platform.python_version(), pc.__version__, platform.system()))

class ConnectDlg(QDialog, Ui_dia_connect):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.pb_ok.clicked.connect(self.button_click)
		self.pb_cancel.clicked.connect(self.reject)

	def button_click(self):
		self.host = unicode(self.cb_hostname.currentText())
		self.uname = unicode(self.le_username.text())
		self.upass = unicode(self.le_username.text())

class NewDlg(QDialog, Ui_dia_createscript):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.pb_createscript_ok.clicked.connect(self.accept)
		self.pb_createscript_cancel.clicked.connect(self.reject)

class DgDlg(QDialog, Ui_dia_datagroups):
	def __init__(self):
		QDialog.__init__(self)
		self.setupUi(self)
		self.pb_dg_ok.clicked.connect(self.accept)

def main():

	# Again, this is boilerplate, it's going to be the same on
	# almost every app you write
	app = QApplication(sys.argv)
	window=Main()
	window.show()
	# It's exec_ because exec is a reserved word in Python
	sys.exit(app.exec_())


if __name__ == "__main__":
	main()
