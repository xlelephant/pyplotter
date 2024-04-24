# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow_r2c2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(709, 900)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(709, 294))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setDocumentMode(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.TopHorizontalLayout = QtWidgets.QHBoxLayout()
        self.TopHorizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.TopHorizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.TopHorizontalLayout.setObjectName("TopHorizontalLayout")
        self.groupBoxDataExplorer = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBoxDataExplorer.sizePolicy().hasHeightForWidth())
        self.groupBoxDataExplorer.setSizePolicy(sizePolicy)
        self.groupBoxDataExplorer.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBoxDataExplorer.setFont(font)
        self.groupBoxDataExplorer.setObjectName("groupBoxDataExplorer")
        self.verticalLayout_12 = QtWidgets.QHBoxLayout(self.groupBoxDataExplorer)
        self.verticalLayout_12.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_12.setSpacing(4)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pushButtonOpenFolder = pushButtonOpenFolder(self.groupBoxDataExplorer)
        self.pushButtonOpenFolder.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButtonOpenFolder.setMaximumSize(QtCore.QSize(80, 50))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.pushButtonOpenFolder.setFont(font)
        self.pushButtonOpenFolder.setObjectName("pushButtonOpenFolder")
        self.verticalLayout_12.addWidget(self.pushButtonOpenFolder)
        self.TopHorizontalLayout.addWidget(self.groupBoxDataExplorer)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.TopHorizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.TopHorizontalLayout, 0, 0, 1, 1)
        self.splitter_3 = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_3.sizePolicy().hasHeightForWidth())
        self.splitter_3.setSizePolicy(sizePolicy)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter = QtWidgets.QSplitter(self.splitter_3)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tableWidgetFolder = TableWidgetFolder(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetFolder.sizePolicy().hasHeightForWidth())
        self.tableWidgetFolder.setSizePolicy(sizePolicy)
        self.tableWidgetFolder.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidgetFolder.setMaximumSize(QtCore.QSize(600, 200))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidgetFolder.setFont(font)
        self.tableWidgetFolder.setStyleSheet("")
        self.tableWidgetFolder.setLineWidth(0)
        self.tableWidgetFolder.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidgetFolder.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetFolder.setAlternatingRowColors(True)
        self.tableWidgetFolder.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetFolder.setShowGrid(False)
        self.tableWidgetFolder.setObjectName("tableWidgetFolder")
        self.tableWidgetFolder.setColumnCount(2)
        self.tableWidgetFolder.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidgetFolder.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidgetFolder.setHorizontalHeaderItem(1, item)
        self.tableWidgetFolder.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetFolder.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidgetFolder.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetFolder.verticalHeader().setVisible(False)
        self.tableWidgetFolder.verticalHeader().setDefaultSectionSize(100)
        self.widget = QtWidgets.QWidget(self.splitter)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelDataBase = QtWidgets.QLabel(self.widget)
        self.labelDataBase.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelDataBase.sizePolicy().hasHeightForWidth())
        self.labelDataBase.setSizePolicy(sizePolicy)
        self.labelDataBase.setMaximumSize(QtCore.QSize(60, 20))
        self.labelDataBase.setObjectName("labelDataBase")
        self.horizontalLayout.addWidget(self.labelDataBase)
        self.labelCurrentDataBase = QtWidgets.QLabel(self.widget)
        self.labelCurrentDataBase.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCurrentDataBase.sizePolicy().hasHeightForWidth())
        self.labelCurrentDataBase.setSizePolicy(sizePolicy)
        self.labelCurrentDataBase.setMinimumSize(QtCore.QSize(0, 0))
        self.labelCurrentDataBase.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCurrentDataBase.setFont(font)
        self.labelCurrentDataBase.setStyleSheet("")
        self.labelCurrentDataBase.setText("")
        self.labelCurrentDataBase.setObjectName("labelCurrentDataBase")
        self.horizontalLayout.addWidget(self.labelCurrentDataBase)
        self.checkBoxHidden = CheckBoxHidden(self.widget)
        self.checkBoxHidden.setEnabled(True)
        self.checkBoxHidden.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBoxHidden.setMaximumSize(QtCore.QSize(90, 20))
        self.checkBoxHidden.setObjectName("checkBoxHidden")
        self.horizontalLayout.addWidget(self.checkBoxHidden, 0, QtCore.Qt.AlignRight)
        self.checkBoxStared = CheckBoxStared(self.widget)
        self.checkBoxStared.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBoxStared.sizePolicy().hasHeightForWidth())
        self.checkBoxStared.setSizePolicy(sizePolicy)
        self.checkBoxStared.setMinimumSize(QtCore.QSize(0, 0))
        self.checkBoxStared.setMaximumSize(QtCore.QSize(16777215, 20))
        self.checkBoxStared.setObjectName("checkBoxStared")
        self.horizontalLayout.addWidget(self.checkBoxStared, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tableWidgetDataBase = TableWidgetDatabase(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetDataBase.sizePolicy().hasHeightForWidth())
        self.tableWidgetDataBase.setSizePolicy(sizePolicy)
        self.tableWidgetDataBase.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidgetDataBase.setMaximumSize(QtCore.QSize(600, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidgetDataBase.setFont(font)
        self.tableWidgetDataBase.setLineWidth(0)
        self.tableWidgetDataBase.setAlternatingRowColors(True)
        self.tableWidgetDataBase.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetDataBase.setShowGrid(False)
        self.tableWidgetDataBase.setObjectName("tableWidgetDataBase")
        self.tableWidgetDataBase.setColumnCount(0)
        self.tableWidgetDataBase.setRowCount(0)
        self.tableWidgetDataBase.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidgetDataBase.horizontalHeader().setMinimumSectionSize(32)
        self.tableWidgetDataBase.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetDataBase.verticalHeader().setVisible(False)
        self.verticalLayout_2.addWidget(self.tableWidgetDataBase)
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelRun = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelRun.sizePolicy().hasHeightForWidth())
        self.labelRun.setSizePolicy(sizePolicy)
        self.labelRun.setMinimumSize(QtCore.QSize(1, 20))
        self.labelRun.setMaximumSize(QtCore.QSize(150, 20))
        self.labelRun.setObjectName("labelRun")
        self.horizontalLayout_3.addWidget(self.labelRun)
        self.labelCurrentRun = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCurrentRun.sizePolicy().hasHeightForWidth())
        self.labelCurrentRun.setSizePolicy(sizePolicy)
        self.labelCurrentRun.setMinimumSize(QtCore.QSize(0, 20))
        self.labelCurrentRun.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelCurrentRun.setFont(font)
        self.labelCurrentRun.setText("")
        self.labelCurrentRun.setObjectName("labelCurrentRun")
        self.horizontalLayout_3.addWidget(self.labelCurrentRun)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.tableWidgetParameter = TableWidgetParameter(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetParameter.sizePolicy().hasHeightForWidth())
        self.tableWidgetParameter.setSizePolicy(sizePolicy)
        self.tableWidgetParameter.setMinimumSize(QtCore.QSize(250, 0))
        self.tableWidgetParameter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.tableWidgetParameter.setFont(font)
        self.tableWidgetParameter.setLineWidth(0)
        self.tableWidgetParameter.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidgetParameter.setAlternatingRowColors(True)
        self.tableWidgetParameter.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidgetParameter.setShowGrid(False)
        self.tableWidgetParameter.setObjectName("tableWidgetParameter")
        self.tableWidgetParameter.setColumnCount(0)
        self.tableWidgetParameter.setRowCount(0)
        self.tableWidgetParameter.horizontalHeader().setStretchLastSection(True)
        self.tableWidgetParameter.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidgetParameter)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelMetadata = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelMetadata.sizePolicy().hasHeightForWidth())
        self.labelMetadata.setSizePolicy(sizePolicy)
        self.labelMetadata.setMinimumSize(QtCore.QSize(0, 20))
        self.labelMetadata.setMaximumSize(QtCore.QSize(140, 20))
        self.labelMetadata.setObjectName("labelMetadata")
        self.horizontalLayout_2.addWidget(self.labelMetadata)
        self.labelCurrentSnapshot = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelCurrentSnapshot.sizePolicy().hasHeightForWidth())
        self.labelCurrentSnapshot.setSizePolicy(sizePolicy)
        self.labelCurrentSnapshot.setMinimumSize(QtCore.QSize(0, 20))
        self.labelCurrentSnapshot.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelCurrentSnapshot.setFont(font)
        self.labelCurrentSnapshot.setText("")
        self.labelCurrentSnapshot.setObjectName("labelCurrentSnapshot")
        self.horizontalLayout_2.addWidget(self.labelCurrentSnapshot)
        self.labelSnapshot = LabelSnapshot(self.layoutWidget)
        self.labelSnapshot.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelSnapshot.sizePolicy().hasHeightForWidth())
        self.labelSnapshot.setSizePolicy(sizePolicy)
        self.labelSnapshot.setMinimumSize(QtCore.QSize(0, 20))
        self.labelSnapshot.setMaximumSize(QtCore.QSize(40, 20))
        self.labelSnapshot.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelSnapshot.setObjectName("labelSnapshot")
        self.horizontalLayout_2.addWidget(self.labelSnapshot)
        self.lineEditFilterSnapshot = LineEditSnapshot(self.layoutWidget)
        self.lineEditFilterSnapshot.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditFilterSnapshot.sizePolicy().hasHeightForWidth())
        self.lineEditFilterSnapshot.setSizePolicy(sizePolicy)
        self.lineEditFilterSnapshot.setMinimumSize(QtCore.QSize(0, 20))
        self.lineEditFilterSnapshot.setMaximumSize(QtCore.QSize(150, 20))
        font = QtGui.QFont()
        font.setItalic(True)
        self.lineEditFilterSnapshot.setFont(font)
        self.lineEditFilterSnapshot.setText("")
        self.lineEditFilterSnapshot.setObjectName("lineEditFilterSnapshot")
        self.horizontalLayout_2.addWidget(self.lineEditFilterSnapshot)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.treeViewSnapshot = TreeViewSnapshot(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeViewSnapshot.sizePolicy().hasHeightForWidth())
        self.treeViewSnapshot.setSizePolicy(sizePolicy)
        self.treeViewSnapshot.setMinimumSize(QtCore.QSize(250, 0))
        self.treeViewSnapshot.setMaximumSize(QtCore.QSize(16777215, 500))
        self.treeViewSnapshot.setObjectName("treeViewSnapshot")
        self.gridLayout.addWidget(self.splitter_3, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBarMain = StatusBar(MainWindow)
        self.statusBarMain.setMinimumSize(QtCore.QSize(0, 30))
        self.statusBarMain.setObjectName("statusBarMain")
        MainWindow.setStatusBar(self.statusBarMain)
        self.menuBarMain = MenuBar(MainWindow)
        self.menuBarMain.setGeometry(QtCore.QRect(0, 0, 709, 26))
        self.menuBarMain.setObjectName("menuBarMain")
        MainWindow.setMenuBar(self.menuBarMain)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.tableWidgetFolder, self.tableWidgetParameter)
        MainWindow.setTabOrder(self.tableWidgetParameter, self.treeViewSnapshot)
        MainWindow.setTabOrder(self.treeViewSnapshot, self.lineEditFilterSnapshot)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "pyplotter"))
        self.groupBoxDataExplorer.setTitle(_translate("MainWindow", "Data explorer"))
        self.pushButtonOpenFolder.setText(_translate("MainWindow", "Open folder"))
        self.tableWidgetFolder.setSortingEnabled(True)
        item = self.tableWidgetFolder.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "item"))
        item = self.tableWidgetFolder.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "size"))
        self.labelDataBase.setText(_translate("MainWindow", "Database:"))
        self.checkBoxHidden.setText(_translate("MainWindow", "Show hidden"))
        self.checkBoxStared.setText(_translate("MainWindow", "Show stared"))
        self.tableWidgetDataBase.setSortingEnabled(True)
        self.labelRun.setText(_translate("MainWindow", "Parameters run:"))
        self.tableWidgetParameter.setSortingEnabled(True)
        self.labelMetadata.setText(_translate("MainWindow", "Metadata run:"))
        self.labelSnapshot.setText(_translate("MainWindow", "Filter:"))
from ..ui.checkBoxHidden import CheckBoxHidden
from ..ui.checkBoxStared import CheckBoxStared
from ..ui.labelSnapshot import LabelSnapshot
from ..ui.lineEditSnapshot import LineEditSnapshot
from ..ui.menuBar import MenuBar
from ..ui.pushButtonOpenFolder import pushButtonOpenFolder
from ..ui.statusBar import StatusBar
from ..ui.tableWidgetDatabase import TableWidgetDatabase
from ..ui.tableWidgetFolder import TableWidgetFolder
from ..ui.tableWidgetParameter import TableWidgetParameter
from ..ui.treeViewSnapshot import TreeViewSnapshot


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
