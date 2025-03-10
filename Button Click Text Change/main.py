import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple PyQt6 App")
        self.setGeometry(300, 300, 300, 200)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Hello, PyQt6!", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
        
    def on_button_click(self):
        self.label.setText("Button Clicked!")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleApp()
    window.show()
    sys.exit(app.exec())