import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import QCoreApplication, Qt

class DemoWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(300, 300, 200, 200)
        self.setWindowTitle('Demo Window')
        
        layout = QVBoxLayout()
        quit_button = QPushButton('Close', self)
        #quit_button.setGeometry(10, 10, 70, 40)
        quit_button.clicked.connect(QCoreApplication.instance().quit)
        
        layout.addWidget(quit_button)
        layout.setAlignment(quit_button, Qt.AlignmentFlag.AlignCenter)
        self.setLayout(layout)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dw = DemoWindow()
    dw.show()
    sys.exit(app.exec())