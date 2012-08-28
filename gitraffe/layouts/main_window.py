# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created: Mon Aug 27 09:41:06 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 525)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(200)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.horizontalLayout.addWidget(self.listWidget)
        self.repositoryLayout = QtGui.QVBoxLayout()
        self.repositoryLayout.setObjectName(_fromUtf8("repositoryLayout"))
        self.repositoryTableWidget = QtGui.QTableWidget(self.centralwidget)
        self.repositoryTableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.repositoryTableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.repositoryTableWidget.setObjectName(_fromUtf8("repositoryTableWidget"))
        self.repositoryTableWidget.setColumnCount(5)
        self.repositoryTableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.repositoryTableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.repositoryTableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.repositoryTableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.repositoryTableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.repositoryTableWidget.setHorizontalHeaderItem(4, item)
        self.repositoryLayout.addWidget(self.repositoryTableWidget)
        self.changesetLayout = QtGui.QHBoxLayout()
        self.changesetLayout.setObjectName(_fromUtf8("changesetLayout"))
        self.changesetButtonsLayout = QtGui.QVBoxLayout()
        self.changesetButtonsLayout.setObjectName(_fromUtf8("changesetButtonsLayout"))
        self.stageButton = QtGui.QPushButton(self.centralwidget)
        self.stageButton.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/stage.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stageButton.setIcon(icon)
        self.stageButton.setObjectName(_fromUtf8("stageButton"))
        self.changesetButtonsLayout.addWidget(self.stageButton)
        self.unstageButton = QtGui.QPushButton(self.centralwidget)
        self.unstageButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/unstage.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unstageButton.setIcon(icon1)
        self.unstageButton.setObjectName(_fromUtf8("unstageButton"))
        self.changesetButtonsLayout.addWidget(self.unstageButton)
        self.separator = QtGui.QFrame(self.centralwidget)
        self.separator.setFrameShape(QtGui.QFrame.HLine)
        self.separator.setFrameShadow(QtGui.QFrame.Sunken)
        self.separator.setObjectName(_fromUtf8("separator"))
        self.changesetButtonsLayout.addWidget(self.separator)
        self.pullButton = QtGui.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/pull.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pullButton.setIcon(icon2)
        self.pullButton.setObjectName(_fromUtf8("pullButton"))
        self.changesetButtonsLayout.addWidget(self.pullButton)
        self.commitButton = QtGui.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/commit_icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commitButton.setIcon(icon3)
        self.commitButton.setObjectName(_fromUtf8("commitButton"))
        self.changesetButtonsLayout.addWidget(self.commitButton)
        self.stashButton = QtGui.QPushButton(self.centralwidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/stash.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stashButton.setIcon(icon4)
        self.stashButton.setObjectName(_fromUtf8("stashButton"))
        self.changesetButtonsLayout.addWidget(self.stashButton)
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/push.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.changesetButtonsLayout.addWidget(self.pushButton)
        self.changesetLayout.addLayout(self.changesetButtonsLayout)
        self.files_listWidget = QtGui.QListWidget(self.centralwidget)
        self.files_listWidget.setObjectName(_fromUtf8("files_listWidget"))
        self.changesetLayout.addWidget(self.files_listWidget)
        self.diff_textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.diff_textBrowser.setObjectName(_fromUtf8("diff_textBrowser"))
        self.changesetLayout.addWidget(self.diff_textBrowser)
        self.changesetLayout.setStretch(1, 2)
        self.changesetLayout.setStretch(2, 4)
        self.repositoryLayout.addLayout(self.changesetLayout)
        self.horizontalLayout.addLayout(self.repositoryLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuView = QtGui.QMenu(self.menubar)
        self.menuView.setObjectName(_fromUtf8("menuView"))
        self.menuRepository = QtGui.QMenu(self.menubar)
        self.menuRepository.setObjectName(_fromUtf8("menuRepository"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionClone_repository = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/clone.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClone_repository.setIcon(icon6)
        self.actionClone_repository.setObjectName(_fromUtf8("actionClone_repository"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionRefresh = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon7)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionAbout_PyGitGui = QtGui.QAction(MainWindow)
        self.actionAbout_PyGitGui.setObjectName(_fromUtf8("actionAbout_PyGitGui"))
        self.actionPull = QtGui.QAction(MainWindow)
        self.actionPull.setIcon(icon2)
        self.actionPull.setObjectName(_fromUtf8("actionPull"))
        self.actionAdd_files = QtGui.QAction(MainWindow)
        self.actionAdd_files.setObjectName(_fromUtf8("actionAdd_files"))
        self.actionRemove_files = QtGui.QAction(MainWindow)
        self.actionRemove_files.setObjectName(_fromUtf8("actionRemove_files"))
        self.actionCommit = QtGui.QAction(MainWindow)
        self.actionCommit.setIcon(icon3)
        self.actionCommit.setObjectName(_fromUtf8("actionCommit"))
        self.actionPush = QtGui.QAction(MainWindow)
        self.actionPush.setIcon(icon5)
        self.actionPush.setObjectName(_fromUtf8("actionPush"))
        self.actionChange_branch = QtGui.QAction(MainWindow)
        self.actionChange_branch.setObjectName(_fromUtf8("actionChange_branch"))
        self.actionCherry_pick = QtGui.QAction(MainWindow)
        self.actionCherry_pick.setObjectName(_fromUtf8("actionCherry_pick"))
        self.actionClone_repository_2 = QtGui.QAction(MainWindow)
        self.actionClone_repository_2.setIcon(icon6)
        self.actionClone_repository_2.setObjectName(_fromUtf8("actionClone_repository_2"))
        self.actionAdd_existing_repository = QtGui.QAction(MainWindow)
        self.actionAdd_existing_repository.setIcon(icon)
        self.actionAdd_existing_repository.setObjectName(_fromUtf8("actionAdd_existing_repository"))
        self.actionSettings = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(os.path.dirname(__file__)+"/icons/settings.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSettings.setIcon(icon8)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionAbout_Gitraffe = QtGui.QAction(MainWindow)
        self.actionAbout_Gitraffe.setObjectName(_fromUtf8("actionAbout_Gitraffe"))
        self.actionClone_repository_3 = QtGui.QAction(MainWindow)
        self.actionClone_repository_3.setIcon(icon6)
        self.actionClone_repository_3.setObjectName(_fromUtf8("actionClone_repository_3"))
        self.actionAdd_existing_repository_2 = QtGui.QAction(MainWindow)
        self.actionAdd_existing_repository_2.setIcon(icon)
        self.actionAdd_existing_repository_2.setObjectName(_fromUtf8("actionAdd_existing_repository_2"))
        self.actionStash = QtGui.QAction(MainWindow)
        self.actionStash.setIcon(icon4)
        self.actionStash.setObjectName(_fromUtf8("actionStash"))
        self.actionDelete_repository = QtGui.QAction(MainWindow)
        self.actionDelete_repository.setIcon(icon1)
        self.actionDelete_repository.setObjectName(_fromUtf8("actionDelete_repository"))
        self.actionDelete_branch = QtGui.QAction(MainWindow)
        self.actionDelete_branch.setObjectName(_fromUtf8("actionDelete_branch"))
        self.menuFile.addAction(self.actionClone_repository_2)
        self.menuFile.addAction(self.actionAdd_existing_repository)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuView.addAction(self.actionRefresh)
        self.menuRepository.addAction(self.actionPull)
        self.menuRepository.addAction(self.actionCommit)
        self.menuRepository.addAction(self.actionStash)
        self.menuRepository.addAction(self.actionPush)
        self.menuRepository.addSeparator()
        self.menuRepository.addAction(self.actionChange_branch)
        self.menuRepository.addAction(self.actionDelete_branch)
        self.menuRepository.addSeparator()
        self.menuRepository.addAction(self.actionCherry_pick)
        self.menuHelp.addAction(self.actionAbout_Gitraffe)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuRepository.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionClone_repository_3)
        self.toolBar.addAction(self.actionAdd_existing_repository_2)
        self.toolBar.addAction(self.actionDelete_repository)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Gitraffe", None, QtGui.QApplication.UnicodeUTF8))
        item = self.repositoryTableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Commit", None, QtGui.QApplication.UnicodeUTF8))
        item = self.repositoryTableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Message", None, QtGui.QApplication.UnicodeUTF8))
        item = self.repositoryTableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Author", None, QtGui.QApplication.UnicodeUTF8))
        item = self.repositoryTableWidget.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.stageButton.setText(QtGui.QApplication.translate("MainWindow", "Stage", None, QtGui.QApplication.UnicodeUTF8))
        self.unstageButton.setText(QtGui.QApplication.translate("MainWindow", "Unstage", None, QtGui.QApplication.UnicodeUTF8))
        self.pullButton.setText(QtGui.QApplication.translate("MainWindow", "Pull", None, QtGui.QApplication.UnicodeUTF8))
        self.commitButton.setText(QtGui.QApplication.translate("MainWindow", " Commit", None, QtGui.QApplication.UnicodeUTF8))
        self.stashButton.setText(QtGui.QApplication.translate("MainWindow", "Stash", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Push", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuView.setTitle(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuRepository.setTitle(QtGui.QApplication.translate("MainWindow", "Repository", None, QtGui.QApplication.UnicodeUTF8))
        self.menuHelp.setTitle(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClone_repository.setText(QtGui.QApplication.translate("MainWindow", "Clone repository...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_PyGitGui.setText(QtGui.QApplication.translate("MainWindow", "About PyGitGui", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPull.setText(QtGui.QApplication.translate("MainWindow", "Pull", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_files.setText(QtGui.QApplication.translate("MainWindow", "Add files...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRemove_files.setText(QtGui.QApplication.translate("MainWindow", "Remove files...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCommit.setText(QtGui.QApplication.translate("MainWindow", "Commit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPush.setText(QtGui.QApplication.translate("MainWindow", "Push", None, QtGui.QApplication.UnicodeUTF8))
        self.actionChange_branch.setText(QtGui.QApplication.translate("MainWindow", "Change branch", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCherry_pick.setText(QtGui.QApplication.translate("MainWindow", "Cherry-pick", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClone_repository_2.setText(QtGui.QApplication.translate("MainWindow", "Clone repository...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_existing_repository.setText(QtGui.QApplication.translate("MainWindow", "Add existing repository...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout_Gitraffe.setText(QtGui.QApplication.translate("MainWindow", "About Gitraffe", None, QtGui.QApplication.UnicodeUTF8))
        self.actionClone_repository_3.setText(QtGui.QApplication.translate("MainWindow", "Clone repository...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAdd_existing_repository_2.setText(QtGui.QApplication.translate("MainWindow", "Add existing repository", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStash.setText(QtGui.QApplication.translate("MainWindow", "Stash", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_repository.setText(QtGui.QApplication.translate("MainWindow", "Delete repository", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_branch.setText(QtGui.QApplication.translate("MainWindow", "Delete branch", None, QtGui.QApplication.UnicodeUTF8))

