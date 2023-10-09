
import sys
import os
from PyQt5 import uic
from PyQt5.QtCore import Qt, QSignalBlocker
from PyQt5.QtWidgets import (QPlainTextEdit, QApplication, QAction, QWidgetAction, QComboBox, QSizePolicy,QInputDialog)
from PyQt5.QtGui import QCloseEvent
import PyQtAds as QtAds

UI_FILE = os.path.join(os.path.dirname(__file__), 'mainwindow.ui')
MainWindowUI, MainWindowBase = uic.loadUiType(UI_FILE)

class CMainWindow(MainWindowUI, MainWindowBase):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        #QtAds.CDockManager.setConfigFlag(QtAds.CDockManager.OpaqueSplitterResize, True)
        #QtAds.CDockManager.setConfigFlag(QtAds.CDockManager.XmlCompressionEnabled, False)
       # QtAds.CDockManager.setConfigFlag(QtAds.CDockManager.FocusHighlighting, True)
       # self.dock_manager = QtAds.CDockManager(self)

        #creating a text edit area
        text_edit = QPlainTextEdit()
        text_edit.SetPlaceHolderText("Введите текст здесь")
        central_dock_widget = QtAds.CDockWindget("Текстовый виджет по центру")
        central_dock_widget.setWidget(text_edit)
        central_dock_area = self.dock_manager.setCentralWidget(central_dock_widget)
        central_dock_area.setAllowedAreas(QtAds.DockWidgetArea.OuterDockAreas)
        
    
    def createPerspectiveUi(self):
        save_perspective_action = QAction("Создать расположение окон", self)
        save_perspective_action.triggered.connect(self.savePerspective)
        perspective_list_action = QWidgetAction(self)
        self.perspective_combo_box = QComboBox(self)
        self.perspective_combo_box.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.perspective_combo_box.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.perspective_combo_box.activated[str].connect(self.dock_manager.openPerspective)
        perspective_list_action.setDefaultWidget(self.perspective_combo_box)
        self.toolBar.addSeparator()
        self.toolBar.addAction(perspective_list_action)
        self.toolBar.addAction(save_perspective_action)

    def savePerspective(self):
        perspective_name, ok = QInputDialog.getText(self, "Сохранить расположение", "Введите название:")
        if not perspective_name or not ok:
            return
        
        self.dock_manager.addPerspective(perspective_name)
        blocker = QSignalBlocker(self.perspective_combo_box)
        self.perspective_combo_box.clear()
        self.perspective_combo_box.addItems(self.dock_manager.perspectiveNames())
        self.perspective_combo_box.setCurrentText(perspective_name)
        
    def closeEvent(self, event: QCloseEvent):
        # Delete dock manager here to delete all floating widgets. This ensures
        # that all top level windows of the dock manager are properly closed
        self.dock_manager.deleteLater()
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    w = CMainWindow()
    w.show()
    app.exec_()

