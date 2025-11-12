from PySide6.QtWidgets import QApplication, QLabel, QPushButton

class MiClase(QPushButton):
    def __init__(self):
        super().__init__()
        self.Boton = QPushButton("dame click")
        self.Boton.clicked.connect(self.cuenta)
        self.contador = 0

    def cuenta(self):
        self.contador += 1
        print(self.contador)


if __name__ == "__main__":
    app = QApplication([])
    ventana1 = MiClase()
    ventana1.show()
    app.exec()