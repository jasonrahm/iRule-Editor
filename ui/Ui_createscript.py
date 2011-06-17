# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'createscript.ui'
#
# Created: Wed Apr 13 11:33:27 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dia_createscript(object):
    def setupUi(self, dia_createscript):
        dia_createscript.setObjectName(_fromUtf8("dia_createscript"))
        dia_createscript.setWindowModality(QtCore.Qt.ApplicationModal)
        dia_createscript.resize(305, 340)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(dia_createscript)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(dia_createscript)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.le_scriptname = QtGui.QLineEdit(dia_createscript)
        self.le_scriptname.setObjectName(_fromUtf8("le_scriptname"))
        self.gridLayout.addWidget(self.le_scriptname, 0, 1, 1, 1)
        self.pb_createscript_ok = QtGui.QPushButton(dia_createscript)
        self.pb_createscript_ok.setObjectName(_fromUtf8("pb_createscript_ok"))
        self.gridLayout.addWidget(self.pb_createscript_ok, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(dia_createscript)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.cb_scripttype = QtGui.QComboBox(dia_createscript)
        self.cb_scripttype.setObjectName(_fromUtf8("cb_scripttype"))
        self.cb_scripttype.addItem(_fromUtf8(""))
        self.cb_scripttype.addItem(_fromUtf8(""))
        self.cb_scripttype.addItem(_fromUtf8(""))
        self.cb_scripttype.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.cb_scripttype, 1, 1, 1, 1)
        self.pb_createscript_cancel = QtGui.QPushButton(dia_createscript)
        self.pb_createscript_cancel.setObjectName(_fromUtf8("pb_createscript_cancel"))
        self.gridLayout.addWidget(self.pb_createscript_cancel, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox = QtGui.QGroupBox(dia_createscript)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tv_templates = QtGui.QTreeView(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tv_templates.sizePolicy().hasHeightForWidth())
        self.tv_templates.setSizePolicy(sizePolicy)
        self.tv_templates.setObjectName(_fromUtf8("tv_templates"))
        self.horizontalLayout.addWidget(self.tv_templates)
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.label.setBuddy(self.le_scriptname)
        self.label_2.setBuddy(self.cb_scripttype)

        self.retranslateUi(dia_createscript)
        QtCore.QObject.connect(self.pb_createscript_ok, QtCore.SIGNAL(_fromUtf8("clicked()")), dia_createscript.accept)
        QtCore.QObject.connect(self.pb_createscript_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), dia_createscript.reject)
        QtCore.QMetaObject.connectSlotsByName(dia_createscript)
        dia_createscript.setTabOrder(self.le_scriptname, self.cb_scripttype)
        dia_createscript.setTabOrder(self.cb_scripttype, self.tv_templates)

    def retranslateUi(self, dia_createscript):
        dia_createscript.setWindowTitle(QtGui.QApplication.translate("dia_createscript", "Create a New Script", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dia_createscript", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_createscript_ok.setText(QtGui.QApplication.translate("dia_createscript", "OK", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dia_createscript", "Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_scripttype.setItemText(0, QtGui.QApplication.translate("dia_createscript", "BIG-IP LTM iRule", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_scripttype.setItemText(1, QtGui.QApplication.translate("dia_createscript", "BIG-IP GTM iRule", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_scripttype.setItemText(2, QtGui.QApplication.translate("dia_createscript", "tmsh Script", None, QtGui.QApplication.UnicodeUTF8))
        self.cb_scripttype.setItemText(3, QtGui.QApplication.translate("dia_createscript", "iApps Script", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_createscript_cancel.setText(QtGui.QApplication.translate("dia_createscript", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("dia_createscript", "Templates", None, QtGui.QApplication.UnicodeUTF8))

