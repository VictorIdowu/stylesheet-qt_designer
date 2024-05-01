from PyQt6.QtWidgets import QMainWindow,QWidget,QApplication,QGroupBox,QStyleFactory,QLabel,QVBoxLayout,QHBoxLayout,QPushButton
import sys



class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
      self.setGeometry(0,0,700,500)
      # Step 1 - Creating a container
      box = QGroupBox()
      box2 = QGroupBox()

      # Step 2 - Creating widgets to be added to the container
      btn1 = QPushButton("Button 1")
      btn2 = QPushButton("Button 2")
      btn3 = QPushButton("Button 3")
      btn4 = QPushButton("Button 4")

      # Step 3 - Create a layout and add the above widgets
      layout = QVBoxLayout()
      layout.addWidget(btn1)
      layout.addWidget(btn2)

      layout2 = QHBoxLayout()
      layout2.addWidget(btn3)
      layout2.addWidget(btn4)

      # Step 4 - Add the above layout to container
      box.setLayout(layout)
      box2.setLayout(layout2)

      # Step 5 - Set the main window's layout to the container
      main_layout = QVBoxLayout(self)
      main_layout.addWidget(box)
      main_layout.addWidget(box2)
      

app = QApplication(sys.argv)
app.setStyle("Fusion")
window = Window()
window.show()
app.exec()