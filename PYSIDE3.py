from PySide6.QtWidgets import QApplication, QFormLayout, QLineEdit, QMainWindow, QPushButton, QWidget, QLabel

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("formulario")

        self.usuarioInput = QLineEdit()
        self.contraseniaInput = QLineEdit()

        self.centralWidget = QWidget(self)
        self.formLayout = QFormLayout(self.centralWidget)
        self.formLayout.addRow("Usuario:", self.usuarioInput)
        self.formLayout.addRow("Contraseña:", self.contraseniaInput)
        self.pushButton = QPushButton("Log in")
        self.formLayout.addRow(self.pushButton)
        self.resultadoLabel = QLabel("")
        self.formLayout.addRow(self.resultadoLabel)
        self.centralWidget.setLayout(self.formLayout)
        self.setCentralWidget(self.centralWidget)

        self.pushButton.clicked.connect(self.mostrarDatos)


    def mostrarDatos(self):
        self.usuario = self.usuarioInput.text()
        self.contraseña = self.contraseniaInput.text()

        if(self.usuario == "admin" and self.contraseña == "admin"):
                self.resultadoLabel.setText("Usuario correcto")
                self.resultadoLabel.setStyleSheet("color: green;")
                
        else:
                self.resultadoLabel.setText("Usuario incorrecto")
                self.resultadoLabel.setStyleSheet("color: red;")    

if __name__ == "__main__":
    app = QApplication([])
    ventana1 = ventanaPrincipal()
    ventana1.show()
    app.exec()