import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
    QFileDialog, QAction, QMessageBox, QVBoxLayout, QWidget
)
from PyQt5.QtCore import Qt

class JsonViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSON Viewer")
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create the tree widget to display JSON data
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Key", "Value"])
        self.tree.setColumnWidth(0, 250)

        # Set scrollbars to appear only as needed
        self.tree.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tree.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Apply custom styles: background, text color, header color and scrollbar styling
        self.tree.setStyleSheet("""
            QTreeWidget {
                background-color: #f5f5f5;
                color: #333333;
                alternate-background-color: #e8f0fe;
            }
            QTreeWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 4px;
                border: 1px solid #6c6c6c;
            }
            QScrollBar:horizontal {
                border: 1px solid #999999;
                background: #dddddd;
                height: 15px;
                margin: 0px 20px 0 20px;
            }
            QScrollBar::handle:horizontal {
                background: #4CAF50;
                min-width: 20px;
            }
            QScrollBar:vertical {
                border: 1px solid #999999;
                background: #dddddd;
                width: 15px;
                margin: 20px 0 20px 0;
            }
            QScrollBar::handle:vertical {
                background: #4CAF50;
                min-height: 20px;
            }
        """)
        self.tree.setAlternatingRowColors(True)

        layout.addWidget(self.tree)

        # Create the menu bar with a File->Open action
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_action = QAction("Open JSON File", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.openFile)
        file_menu.addAction(open_action)

    def openFile(self):
        # Open a file dialog to choose a JSON file
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.tree.clear()
                self.addItems(self.tree.invisibleRootItem(), data)
                self.tree.expandAll()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load JSON file:\n{str(e)}")

    def addItems(self, parent, value, key=""):
        """
        Recursively adds items to the QTreeWidget.
        - If value is a dictionary, create a new item for each key.
        - If value is a list, create an item for each element.
        - Otherwise, set the value in the second column.
        """
        if isinstance(value, dict):
            if key:
                item = QTreeWidgetItem(parent, [str(key), ""])
                parent = item
            for k, v in value.items():
                self.addItems(parent, v, key=k)
        elif isinstance(value, list):
            if key:
                item = QTreeWidgetItem(parent, [str(key), ""])
                parent = item
            for index, element in enumerate(value):
                self.addItems(parent, element, key=f"[{index}]")
        else:
            QTreeWidgetItem(parent, [str(key), str(value)])

def main():
    app = QApplication(sys.argv)
    viewer = import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
    QFileDialog, QAction, QMessageBox, QVBoxLayout, QWidget
)
from PyQt5.QtCore import Qt

class JsonViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSON Viewer")
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create the tree widget to display JSON data
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Key", "Value"])
        self.tree.setColumnWidth(0, 250)

        # Set scrollbars to appear only as needed
        self.tree.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tree.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Apply custom styles: background, text color, header color and scrollbar styling
        self.tree.setStyleSheet("""
            QTreeWidget {
                background-color: #f5f5f5;
                color: #333333;
                alternate-background-color: #e8f0fe;
            }
            QTreeWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 4px;
                border: 1px solid #6c6c6c;
            }
            QScrollBar:horizontal {
                border: 1px solid #999999;
                background: #dddddd;
                height: 15px;
                margin: 0px 20px 0 20px;
            }
            QScrollBar::handle:horizontal {
                background: #4CAF50;
                min-width: 20px;
            }
            QScrollBar:vertical {
                border: 1px solid #999999;
                background: #dddddd;
                width: 15px;
                margin: 20px 0 20px 0;
            }
            QScrollBar::handle:vertical {
                background: #4CAF50;
                min-height: 20px;
            }
        """)
        self.tree.setAlternatingRowColors(True)

        layout.addWidget(self.tree)

        # Create the menu bar with a File->Open action
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_action = QAction("Open JSON File", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.openFile)
        file_menu.addAction(open_action)

    def openFile(self):
        # Open a file dialog to choose a JSON file
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.tree.clear()
                self.addItems(self.tree.invisibleRootItem(), data)
                self.tree.expandAll()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load JSON file:\n{str(e)}")

    def addItems(self, parent, value, key=""):
        """
        Recursively adds items to the QTreeWidget.
        - If value is a dictionary, create a new item for each key.
        - If value is a list, create an item for each element.
        - Otherwise, set the value in the second column.
        """
        if isinstance(value, dict):
            if key:
                item = QTreeWidgetItem(parent, [str(key), ""])
                parent = item
            for k, v in value.items():
                self.addItems(parent, v, key=k)
        elif isinstance(value, list):
            if key:
                item = QTreeWidgetItem(parent, [str(key), ""])
                parent = item
            for index, element in enumerate(value):
                self.addItems(parent, element, key=f"[{index}]")
        else:
            QTreeWidgetItem(parent, [str(key), str(value)])

def main():
    app = QApplication(sys.argv)
    viewer = JsonViewer()
    viewer.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
    QFileDialog, QAction, QMessageBox, QVBoxLayout, QWidget
)
from PyQt5.QtCore import Qt

class JsonViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSON Viewer")
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create the tree widget to display JSON data
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Key", "Value"])
        self.tree.setColumnWidth(0, 250)

        # Set scrollbars to appear only as needed
        self.tree.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tree.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Apply custom styles: background, text color, header color and scrollbar styling
        self.tree.setStyleSheet("""
            QTreeWidget {
                background-color: #f5f5f5;
                color: #333333;
                alternate-background-color: #e8f0fe;
            }
            QTreeWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 4px;
                border: 1px solid #6c6c6c;
            }
            QScrollBar:horizontal {
                border: 1px solid #999999;
                background: #dddddd;
                height: 15px;
                margin: 0px 20px 0 20px;
            }
            QScrollBar::handle:horizontal {
                background: #4CAF50;
                min-width: 20px;
            }
            QScrollBar:vertical {
                border: 1px solid #999999;
                background: #dddddd;
                width: 15px;
                margin: 20px 0 20px 0;
            }
            QScrollBar::handle:vertical {
                background: #4CAF50;
                min-height: 20px;
            }
        """)
        self.tree.setAlternatingRowColors(True)

        layout.addWidget(self.tree)

        # Create the menu bar with a File->Open action
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_action = QAction("Open JSON File", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.openFile)
        file_menu.addAction(open_action)

    def openFile(self):
        # Open a file dialog to choose a JSON file
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.tree.clear()
                self.addItems(self.tree.invisibleRootItem(), data)
                self.tree.expandAll()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load JSON file:\n{str(e)}")

    def addItems(self, parent, value, key=""):
        """
        Recursively adds items to the QTreeWidget.
        - If value is a dictionary, create a new item for each key.
        - If value is a list, create an item for each element.
        - Otherwise, set the value in the second column.
        """
        if isinstance(value, dict):
            if key:
                item = QTreeWidgetItem(parent, [str(key), ""])
                parent = item
            for k, v in value.items():
                self.addItems(parent, v, key=k)
        elif isinstance(value, list):
            if key:
                item = QTreeWidgetItem(parent, [str(key), ""])
                parent = item
            for index, element in enumerate(value):
                self.addItems(parent, element, key=f"[{index}]")
        else:
            QTreeWidgetItem(parent, [str(key), str(value)])

def main():
    app = QApplication(sys.argv)
    viewer = JsonViewer()
    viewer.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem,
    QFileDialog, QAction, QMessageBox, QVBoxLayout, QWidget
)
from PyQt5.QtCore import Qt

class JsonViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("JSON Viewer")
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        # Create the central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Create the tree widget to display JSON data
        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["Key", "Value"])
        self.tree.setColumnWidth(0, 250)

        # Set scrollbars to appear only as needed
        self.tree.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tree.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Apply custom styles: background, text color, header color and scrollbar styling
        self.tree.setStyleSheet("""
            QTreeWidget {
                background-color: #f5f5f5;
                color: #333333;
                alternate-background-color: #e8f0fe;
            }
            QTreeWidget::item {
                padding: 5px;
            }
            QHeaderView::section {
                background-color: #4CAF50;
                color: white;
                padding: 4px;
                border: 1px solid #6c6c6c;
            }
            QScrollBar:horizontal {
                border: 1px solid #999999;
                background: #dddddd;
                height: 15px;
                margin: 0px 20px 0 20px;
            }
            QScrollBar::handle:horizontal {
                background: #4CAF50;
                min-width: 20px;
            }
            QScrollBar:vertical {
                border: 1px solid #999999;
                background: #dddddd;
                width: 15px;
                margin: 20px 0 20px 0;
            }
            QScrollBar::handle:vertical {
                background: #4CAF50;
                min-height: 20px;
            }
        """)
        self.tree.setAlternatingRowColors(True)

        layout.addWidget(self.tree)

        # Create the menu bar with a File->Open action
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        open_action = QAction("Open JSON File", self)
        open_action.setShortcut("Ctrl+O")
        open_action.triggered.connect(self.openFile)
        file_menu.addAction(open_action)

    def openFile(self):
        # Open a file dialog to choose a JSON file
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(
            self, "Open JSON File", "", "JSON Files (*.json);;All Files (*)", options=options)
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                self.tree.clear()
                self.addItems(self.tree.invisibleRootItem(), data)
                self.tree.expandAll()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load JSON file:\n{str(e)}")

    def addItems(self, parent, value, key=""):
        """
        Recursively adds items to the QTreeWidget.
        - If value is a dictionary, create a new item for each key.
        - If value is a list, create an item for each element.
        - Otherwise, set the value in the second column.
        """
        if isinstance(value, dict):
            if key:
                item = QTreeWidgetItem(parent, [str(key), ""])
                parent = item
            for k, v in value.items():
                self.addItems(parent, v, key=k)
        elif isinstance(value, list):
            if key:
                item = QTreeWidgetItem(parent, [str(key), ""])
                parent = item
            for index, element in enumerate(value):
                self.addItems(parent, element, key=f"[{index}]")
        else:
            QTreeWidgetItem(parent, [str(key), str(value)])

def main():
    app = QApplication(sys.argv)
    viewer = JsonViewer()
    viewer.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
()
    viewer.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
