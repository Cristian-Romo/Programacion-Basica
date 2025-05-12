import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QHBoxLayout

class CalculatorApp(QWidget):
    def _init_(self):
        super()._init_()
        self.setWindowTitle("Calculadora en PyQt5")
        self.setGeometry(100, 100, 350, 200)
        
        self.initUI()

    def initUI(self):
        # Crear widgets
        self.label = QLabel("Ingrese dos números:", self)
        self.text_input1 = QLineEdit(self)
        self.text_input2 = QLineEdit(self)
        
        # Botones de operaciones
        self.button_suma = QPushButton("Suma", self)
        self.button_resta = QPushButton("Resta", self)
        self.button_mult = QPushButton("Multiplicación", self)
        self.button_div = QPushButton("División", self)
        
        self.result_label = QLabel("Resultado: ", self)

        # Conectar botones a métodos
        self.button_suma.clicked.connect(lambda: self.calculate(self.suma))
        self.button_resta.clicked.connect(lambda: self.calculate(self.resta))
        self.button_mult.clicked.connect(lambda: self.calculate(self.multiplicacion))
        self.button_div.clicked.connect(lambda: self.calculate(self.division))

        # Layouts
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input1)
        layout.addWidget(self.text_input2)
        
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.button_suma)
        button_layout.addWidget(self.button_resta)
        button_layout.addWidget(self.button_mult)
        button_layout.addWidget(self.button_div)
        
        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def calculate(self, operation):
        try:
            num1 = float(self.text_input1.text())
            num2 = float(self.text_input2.text())
            resultado = operation(num1, num2)
            self.result_label.setText(f"Resultado: {resultado}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Por favor ingresa números válidos.")

    def suma(self, a, b):
        return a + b

    def resta(self, a, b):
        return a - b

    def multiplicacion(self, a, b):
        return a * b

    def division(self, a, b):
        return a / b if b != 0 else "Error: División por cero"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = CalculatorApp()
    ventana.show()
    sys.exit(app.exec_())