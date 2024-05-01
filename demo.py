from PyQt6.QtWidgets import QMainWindow,QWidget,QApplication,QStyleFactory,QLabel,QVBoxLayout,QPushButton
import sys

stylesheet = """
                QPushButton#My_button{
                background-color: gray;
                padding:5px;
                border-radius: 10px;
                color:white;
                }
                QPushButton#My_button:hover{
                background-color: red;
                }
                QPushButton#My_button:pressed{
                background-color: blue;
                }
                QLabel#my_label{
                background-color:blue;
                color:white;
                margin:100px;
                }
                """

class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
      self.setGeometry(0,0,700,500)
      label = QLabel("<h1>Das ist ein label</h1>", self)
      label.resize(200,50)
      label.setObjectName("my_label")
      
      button = QPushButton("Click me", self)
      button.setObjectName("My_button")

      layout = QVBoxLayout()
      layout.addWidget(label)
      layout.addWidget(button)
      self.setLayout(layout)

app = QApplication(sys.argv)
app.setStyle("Windows")
app.setStyleSheet(stylesheet)
window = Window()
window.show()
app.exec()