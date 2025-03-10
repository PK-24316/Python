import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit
from PyQt6.QtCore import Qt

class AdvancedApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced PyQt6 App")
        self.setGeometry(300, 300, 400, 250)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Enter your name: ", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Type Here...")
        layout.addWidget(self.text_input)
        
        self.button = QPushButton("Submit", self)
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)
        
        self.greeting_label = QLabel("", self)
        self.greeting_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.greeting_label)
        
        self.setLayout(layout)
        
    def on_button_click(self):
        name = self.text_input.text()
        if name:
            self.greeting_label.setText(f"Hello, {name}!")
        else:
            self.greeting_label.setText("Please enter a name.")
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedApp()
    window.show()
    sys.exit(app.exec())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        