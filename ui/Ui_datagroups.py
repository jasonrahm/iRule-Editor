# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datagroups.ui'
#
# Created: Wed Apr 13 11:34:39 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dia_datagroups(object):
    def setupUi(self, dia_datagroups):
        dia_datagroups.setObjectName(_fromUtf8("dia_datagroups"))
        dia_datagroups.setWindowModality(QtCore.Qt.ApplicationModal)
        dia_datagroups.resize(480, 431)
        self.verticalLayout_5 = QtGui.QVBoxLayout(dia_datagroups)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tab_datagroups = QtGui.QTabWidget(dia_datagroups)
        self.tab_datagroups.setObjectName(_fromUtf8("tab_datagroups"))
        self.tab_addr = QtGui.QWidget()
        self.tab_addr.setToolTip(_fromUtf8(""))
        self.tab_addr.setObjectName(_fromUtf8("tab_addr"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_addr)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tv_dgaddr = QtGui.QTreeView(self.tab_addr)
        self.tv_dgaddr.setObjectName(_fromUtf8("tv_dgaddr"))
        self.verticalLayout_2.addWidget(self.tv_dgaddr)
        self.tab_datagroups.addTab(self.tab_addr, _fromUtf8(""))
        self.tab_int = QtGui.QWidget()
        self.tab_int.setObjectName(_fromUtf8("tab_int"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tab_int)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.tv_dgint = QtGui.QTreeView(self.tab_int)
        self.tv_dgint.setObjectName(_fromUtf8("tv_dgint"))
        self.verticalLayout_7.addWidget(self.tv_dgint)
        self.tab_datagroups.addTab(self.tab_int, _fromUtf8(""))
        self.tab_str = QtGui.QWidget()
        self.tab_str.setObjectName(_fromUtf8("tab_str"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.tab_str)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.tv_dgstr = QtGui.QTreeView(self.tab_str)
        self.tv_dgstr.setObjectName(_fromUtf8("tv_dgstr"))
        self.verticalLayout_8.addWidget(self.tv_dgstr)
        self.tab_datagroups.addTab(self.tab_str, _fromUtf8(""))
        self.tab_ext = QtGui.QWidget()
        self.tab_ext.setObjectName(_fromUtf8("tab_ext"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_ext)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.tab_extdg = QtGui.QTabWidget(self.tab_ext)
        self.tab_extdg.setTabPosition(QtGui.QTabWidget.West)
        self.tab_extdg.setObjectName(_fromUtf8("tab_extdg"))
        self.tab_extaddr = QtGui.QWidget()
        self.tab_extaddr.setObjectName(_fromUtf8("tab_extaddr"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.tab_extaddr)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.tv_extdgaddr = QtGui.QTreeView(self.tab_extaddr)
        self.tv_extdgaddr.setObjectName(_fromUtf8("tv_extdgaddr"))
        self.verticalLayout_3.addWidget(self.tv_extdgaddr)
        self.tab_extdg.addTab(self.tab_extaddr, _fromUtf8(""))
        self.tab_extint = QtGui.QWidget()
        self.tab_extint.setObjectName(_fromUtf8("tab_extint"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab_extint)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.tv_extdgint = QtGui.QTreeView(self.tab_extint)
        self.tv_extdgint.setObjectName(_fromUtf8("tv_extdgint"))
        self.verticalLayout_4.addWidget(self.tv_extdgint)
        self.tab_extdg.addTab(self.tab_extint, _fromUtf8(""))
        self.tab_extstr = QtGui.QWidget()
        self.tab_extstr.setObjectName(_fromUtf8("tab_extstr"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.tab_extstr)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.tv_extdgstr = QtGui.QTreeView(self.tab_extstr)
        self.tv_extdgstr.setObjectName(_fromUtf8("tv_extdgstr"))
        self.verticalLayout_9.addWidget(self.tv_extdgstr)
        self.tab_extdg.addTab(self.tab_extstr, _fromUtf8(""))
        self.verticalLayout_6.addWidget(self.tab_extdg)
        self.tab_datagroups.addTab(self.tab_ext, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tab_datagroups)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pb_dg_add = QtGui.QPushButton(dia_datagroups)
        self.pb_dg_add.setObjectName(_fromUtf8("pb_dg_add"))
        self.verticalLayout.addWidget(self.pb_dg_add)
        self.pb_dg_edit = QtGui.QPushButton(dia_datagroups)
        self.pb_dg_edit.setObjectName(_fromUtf8("pb_dg_edit"))
        self.verticalLayout.addWidget(self.pb_dg_edit)
        self.pb_dg_del = QtGui.QPushButton(dia_datagroups)
        self.pb_dg_del.setObjectName(_fromUtf8("pb_dg_del"))
        self.verticalLayout.addWidget(self.pb_dg_del)
        spacerItem = QtGui.QSpacerItem(20, 158, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.pb_dg_refresh = QtGui.QPushButton(dia_datagroups)
        self.pb_dg_refresh.setObjectName(_fromUtf8("pb_dg_refresh"))
        self.verticalLayout.addWidget(self.pb_dg_refresh)
        self.pb_dg_ok = QtGui.QPushButton(dia_datagroups)
        self.pb_dg_ok.setObjectName(_fromUtf8("pb_dg_ok"))
        self.verticalLayout.addWidget(self.pb_dg_ok)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.retranslateUi(dia_datagroups)
        self.tab_datagroups.setCurrentIndex(3)
        self.tab_extdg.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dia_datagroups)

    def retranslateUi(self, dia_datagroups):
        dia_datagroups.setWindowTitle(QtGui.QApplication.translate("dia_datagroups", "Data Groups", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_datagroups.setTabText(self.tab_datagroups.indexOf(self.tab_addr), QtGui.QApplication.translate("dia_datagroups", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_datagroups.setTabText(self.tab_datagroups.indexOf(self.tab_int), QtGui.QApplication.translate("dia_datagroups", "Integer", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_datagroups.setTabText(self.tab_datagroups.indexOf(self.tab_str), QtGui.QApplication.translate("dia_datagroups", "String", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_extdg.setTabText(self.tab_extdg.indexOf(self.tab_extaddr), QtGui.QApplication.translate("dia_datagroups", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_extdg.setTabText(self.tab_extdg.indexOf(self.tab_extint), QtGui.QApplication.translate("dia_datagroups", "Integer", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_extdg.setTabText(self.tab_extdg.indexOf(self.tab_extstr), QtGui.QApplication.translate("dia_datagroups", "String", None, QtGui.QApplication.UnicodeUTF8))
        self.tab_datagroups.setTabText(self.tab_datagroups.indexOf(self.tab_ext), QtGui.QApplication.translate("dia_datagroups", "External", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_dg_add.setText(QtGui.QApplication.translate("dia_datagroups", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_dg_edit.setText(QtGui.QApplication.translate("dia_datagroups", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_dg_del.setText(QtGui.QApplication.translate("dia_datagroups", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_dg_refresh.setText(QtGui.QApplication.translate("dia_datagroups", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.pb_dg_ok.setText(QtGui.QApplication.translate("dia_datagroups", "Ok", None, QtGui.QApplication.UnicodeUTF8))

