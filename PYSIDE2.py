from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow

class ventanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ventanaPrincipal")

        self.QComboBox = QComboBox(self)
        self.QComboBox.setFixedSize(100,30)
        self.QComboBox.move(50,50)

        self.QComboBox.addItems(["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"])

        self.QComboBox.activated.connect(self.mostrarMes)

    def mostrarMes(self):
        print("en la posicion ", self.QComboBox.currentIndex() + 1, " esta el mes de ", self.QComboBox.currentText())




if __name__ == "__main__":
    app = QApplication([])
    ventana1 = ventanaPrincipal()
    ventana1.show()
    app.exec()
