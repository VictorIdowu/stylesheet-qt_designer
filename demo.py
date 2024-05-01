from PyQt6.QtWidgets import QMainWindow,QWidget,QApplication,QGroupBox,QStyleFactory,QLabel,QVBoxLayout,QTabWidget,QHBoxLayout,QPushButton
import sys



class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
      self.setGeometry(0,0,700,500)
      # Creating a tab widget
      tab_widget = QTabWidget()

      # Create tabs
      tab1 = QWidget()
      tab2 = QWidget()

      # Add tabs to the tab widget
      tab_widget.addTab(tab1, "Tab 1")
      tab_widget.addTab(tab2, "Tab 2")
      
      # Create widgets to be added to the tabs
      btn1 = QPushButton("Button 1")
      btn2 = QPushButton("Button 2")

      # Creating layout for the 2 tabs
      layout1 = QVBoxLayout()
      layout1.addWidget(btn1)
      layout2 = QVBoxLayout()
      layout2.addWidget(btn2)

      # Setting tabs layouts to layout 1&2
      tab1.setLayout(layout1)
      tab2.setLayout(layout2)
      

      # Add the above tab widget to the main window
      layout = QVBoxLayout(self)
      layout.addWidget(tab_widget)
      
      

app = QApplication(sys.argv)
app.setStyle("Fusion")
window = Window()
window.show()
app.exec()