import os
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QTextEdit


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowsTitle("Ejercicio 8")

        menu = self.menuBar()
        barraMenu = menu.addMenu("&Menu")

        rutaIcono = os.path.join(os.path.dirname(
            __file__), "imagenes/icono.png")
        accion = QAction(QIcon(rutaIcono), "imprimir en dock", self)
        accion.setWhatsThis("Al ejecutar esta acción, se añadirá el texto \"Acción pulsada\" en el dock. Se puede lanzar por Menú > Imprimir en dock, con Ctrl + P o haciendo clic en el botón correspondiente de la barra de herramientas")
        accion.setShortcut(QKeySequence("Ctrl+P"))
        barraTareas = QToolBar("Barra de tareas")
        self.addToolBar(barraTareas)
        accion.triggered.connect(self.imprimirEnDock)
        barraMenu.addAction(accion)
        barraTareas.addAction(accion)
        




if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
