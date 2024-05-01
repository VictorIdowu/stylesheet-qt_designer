from PyQt6.QtWidgets import QMainWindow,QWidget,QApplication,QGroupBox,QStyleFactory,QLabel,QVBoxLayout,QTabWidget,QHBoxLayout,QPushButton,QRadioButton,QCheckBox
import sys



class Window(QWidget):
  def __init__(self):
    super().__init__()
    self.initUI()

  def initUI(self):
    self.setGeometry(0,0,700,500)
    self.setWindowTitle("Beverage Shop")

    tab_widget = QTabWidget()

    tee = QWidget()
    Kaffee = QWidget()

    tab_widget.addTab(tee, "Tee")
    tab_widget.addTab(Kaffee, "Kaffee")
    
    # Tea layout
    tee_layout = QVBoxLayout()

    flüssig_label = QLabel("Select Milch/Wasser")
    spice_label = QLabel("Select Milch/Wasser")

    milch_btn = QRadioButton("Milch")
    wasser_btn = QRadioButton("Wasser")

    


    # Container erstellen für milch/wasser
    liquid_group = QGroupBox()

    # Create layout for liquid container
    liquid_group_layout = QVBoxLayout()
    liquid_group_layout.addWidget(milch_btn)
    liquid_group_layout.addWidget(wasser_btn)

    liquid_group.setLayout(liquid_group_layout)

    # Container erstellen für spice
    spice_group = QGroupBox()

    # Create layout for spice container
    spice_group_layout = QVBoxLayout()

    # Add checkboxes to layout
    spices = ["Spice","Clove","Black pepper","Cinamon", "Turmuric"]

    for spice in spices:
      spices_checkboxe = QCheckBox(spice)
      spice_group_layout.addWidget(spices_checkboxe)

    spice_group.setLayout(spice_group_layout)

    tee_layout.addWidget(flüssig_label)
    tee_layout.addWidget(liquid_group)
    tee_layout.addWidget(spice_label)
    tee_layout.addWidget(spice_group)
    tee.setLayout(tee_layout)

    main_layout = QVBoxLayout(self)
    main_layout.addWidget(tab_widget)
      

app = QApplication(sys.argv)
app.setStyle("Fusion")
window = Window()
window.show()
app.exec()