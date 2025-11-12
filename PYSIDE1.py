from PySide6.QtWidgets import QLineEdit, QLabel, QMainWindow, QApplication
from PySide6.QtCore import Qt
##Desarrolla una aplicación que tenga una ventana principal
#  con un QLineEdit y un QLabel.
#  Asigna un tamaño máximo de texto de 5 carácteres al QLineEdit 
# y un tamaño fijo de 50x30 
# píxeles. El Qlabel también tendrá un tamaño fijo de 50x30 píxeles.
 
# y se desplazará 50 píxeles a la derecha para no solaparse con
#  el QLineEdit. 
# 
# Cuando el texto del QLineEdit cambie, la etiqueta
#  monstrará el texto introducido.
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ventanaPrincipal")
        self.QLineEdit = QLineEdit(self)
        self.QLabel = QLabel(self)
        self.QLineEdit.setMaxLength(5)
        self.QLineEdit.setFixedSize(50,30)
        self.QLabel.setFixedSize(50,30)

        self.QLabel.move(50,0)
        self.QLabel.setAlignment(Qt.AlignCenter)  ## No es del ejercicio

        self.QLineEdit.textChanged.connect(self.QLabel.setText)
if __name__ == "__main__":
    app = QApplication([])
    Ventana1 = VentanaPrincipal()
    Ventana1.show()
    app.exec()