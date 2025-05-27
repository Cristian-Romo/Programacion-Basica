import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout

class Calculadora(QWidget):
    def _init_(self):
        super()._init_()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 400)

        layout = QVBoxLayout()
        
        self.pantalla = QLineEdit(self)
        self.pantalla.setReadOnly(True)
        layout.addWidget(self.pantalla)

        botones = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+')
        ]
        
        grid_layout = QGridLayout()
        for i, fila in enumerate(botones):
            for j, boton in enumerate(fila):
                btn = QPushButton(boton)
                btn.clicked.connect(self.on_click)
                grid_layout.addWidget(btn, i, j)
        
        layout.addLayout(grid_layout)
        self.setLayout(layout)

    def on_click(self):
        boton = self.sender().text()
        if boton == '=':
            try:
                resultado = str(eval(self.pantalla.text()))
                self.pantalla.setText(resultado)
            except:
                self.pantalla.setText("Error")
        else:
            self.pantalla.setText(self.pantalla.text() + boton)

if _name_ == "_main_":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())