from PyQt4.QtGui import QMainWindow, QFileDialog, qApp, QListWidgetItem, QMessageBox, QInputDialog, QIcon, QTableWidgetItem, QAbstractItemView
from PyQt4.QtCore import QDir, QObject, SIGNAL, Qt
from PyQt4 import QtGui
from layouts.main_window import Ui_MainWindow
from git import check_repository, open_repository, get_graph, get_files, change_local_branch, change_remote_branch
import db_adapter
import os
from layouts import main_window
from layouts.clone_dialog_wrapper import CloneWindowWrapper
from layouts.branches_dialog_wrapper import BranchesDialogWrapper

class MainWindowWrapper(QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Repository list
        self.ui.listWidget.setMouseTracking(True)
        self.ui.listWidget.itemSelectionChanged.connect(self.view_repository)
        self.list_all_repositories()
        #Repository Table
        self.ui.repositoryTableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.repositoryTableWidget.verticalHeader().setVisible(False)
        self.ui.repositoryTableWidget.itemSelectionChanged.connect(self.view_files)
        # Menu/toolbar
        QObject.connect(self.ui.actionAdd_existing_repository, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionAdd_existing_repository_2, SIGNAL('triggered()'), self.browse)
        QObject.connect(self.ui.actionExit, SIGNAL('triggered()'), qApp.exit)
        QObject.connect(self.ui.actionDelete_repository, SIGNAL('triggered()'), self.delete_listWidgetitem)
        QObject.connect(self.ui.actionClone_repository_3, SIGNAL('triggered()'), self.clone_respoitory)
        QObject.connect(self.ui.actionClone_repository_2, SIGNAL('triggered()'), self.clone_respoitory)
        QObject.connect(self.ui.actionClone_repository, SIGNAL('triggered()'), self.clone_respoitory)
        QObject.connect(self.ui.actionChange_branch, SIGNAL('triggered()'), self.change_branch_dialog)

    def list_all_repositories(self):
        repositories = db_adapter.get_repositories()
        for repository in repositories:
            self.add_to_list(repository.name, repository.path)

    def browse(self):
        directory = QFileDialog.getExistingDirectory(self, QDir.homePath(), QDir.homePath())
        if directory!="":
            path = check_repository(directory)
            if path[0]:
                if not db_adapter.exists_repository(directory):
                    directory = path[1]
                    name = QInputDialog().getText(self, 'Name', 'Put your repository name:', text=os.path.basename(directory))
                    if name[1]:
                        self.add_to_database(name[0], directory)
                        self.add_to_list(name[0], directory)
                else:
                    QMessageBox.critical(self, "Error", "This repository is already added", QMessageBox.Ok)
            else: QMessageBox.critical(self, "Error", "That directory is not a git repository", QMessageBox.Ok)

    def add_to_database(self, name, directory):
        db_adapter.add_repository(name, directory)

    def add_to_list(self, name, directory):
        repo = QListWidgetItem(QIcon(os.path.dirname(main_window.__file__)+'/icons/Git-Icon-Black.png'), name, self.ui.listWidget)
        repo.setStatusTip(directory)
        repo.setData(Qt.UserRole, directory)
        repo.setFlags(repo.flags() | Qt.ItemIsEditable)

    def delete_listWidgetitem(self):
        if self.ui.listWidget.count()!=0:
            name = self.ui.listWidget.item(self.ui.listWidget.currentRow()).text()
            respond = QMessageBox.question(self, "Delete", 
                                           "Are you sure, that you want delete " + name,
                                           QMessageBox.Ok, QMessageBox.Cancel)
            if respond==QMessageBox.Ok:
                db_adapter.delete_repository(self.ui.listWidget.currentItem().data(Qt.UserRole))
                self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())

    def graph(self):
        i = 0
        graph = get_graph()
        self.ui.repositoryTableWidget.setRowCount(len(graph))
        for row in graph:
            j = 0
            for col in row:
                item = QTableWidgetItem(col)
                self.ui.repositoryTableWidget.setItem(i, j, item)
                j += 1
            i += 1

    def refresh_graph(self):
        self.ui.repositoryTableWidget.clearContents()
        self.graph()

    def view_repository(self):
        path = self.ui.listWidget.currentItem().data(Qt.UserRole)
        open_repository(path)
        self.refresh_graph()

    def clone_respoitory(self):
        cwd = CloneWindowWrapper(self)
        cwd.exec_()

    def view_files(self):
        self.ui.files_listWidget.clear()
        commit = self.ui.repositoryTableWidget.item(self.ui.repositoryTableWidget.currentRow(), 1).text()
        if commit != "":
            files = get_files(commit)
            for flag, file in files:
               item = QListWidgetItem(flag+" "+file, self.ui.files_listWidget)

    def get_default_branch_name(self, name):
        name = name.split('/')
        return name[1]

    def change_lcl_branch(self):
        item = self.bdw.ui.localBranchesListWidget.currentItem()
        if item == None:
            self.error()
        else:
            change_local_branch(item.text())

    def change_rmt_branch(self):
        item = self.bdw.ui.remoteBranchesListWidget.currentItem()
        if item == None:
            self.error()
        else:
            name = QInputDialog().getText(self, 'Name', 'Put your branch name:', text=self.get_default_branch_name(item.text()))
            if name[1]:
                change_remote_branch(item.text(), name[0])

    def change_branch(self):
        if self.bdw.ui.branchesTabWidget.currentIndex() == 0:
            self.change_lcl_branch()
        else:
            self.change_rmt_branch()
        self.refresh_graph()

    def change_branch_dialog(self):
        self.bdw = BranchesDialogWrapper(self)
        QObject.connect(self.bdw, SIGNAL('accepted()'), self.change_branch)
        self.bdw.exec_()

