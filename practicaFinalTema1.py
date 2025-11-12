import os
from PySide6.QtGui import QIcon, QKeySequence, QAction
from PySide6.QtWidgets import QTextEdit, QMainWindow, QApplication, QToolBar, QMenuBar



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Word")
        self.setGeometry(100, 100, 800, 600)

        self.editor = QTextEdit(self)
        self.setCentralWidget(self.editor)
        self.MenuPrincipal = self.menuBar()
        self.crearAccion = self.acciones
        self.menuArchivo = self.MenuPrincipal.addMenu("&Archivo")
        self.menuArchivo.addAction(self.crearAccion("Nuevo", "Ctrl+N", "abrir un nuevo documento en blanco", self.nuevoDocumento))
        self.menuArchivo.addAction(self.crearAccion("Abrir", "Ctrl+O", "abrir un documento existente", self.abrirDocumento))
        self.menuArchivo.addAction(self.crearAccion("Guardar", "Ctrl+S", "guardar el documento", self.guardarDocumento))
        self.menuArchivo.addAction(self.crearAccion("Salir", "Ctrl+E", "salir de la aplicacion", self.salir))
    def acciones(self, nombre, atajo, descripcion, metodo):
        accion = QAction(nombre, self)
        accion.setShortcut(QKeySequence(atajo))
        accion.setStatusTip(descripcion)
        accion.triggered.connect(metodo)
        return accion
    def nuevoDocumento(self):
        self.ventanas_abiertas = []
        nueva_ventana = VentanaPrincipal()
        nueva_ventana.show()
        self.ventanas_abiertas.append(nueva_ventana)
    def abrirDocumento(self):
         pass                  #Modificar                
    def guardarDocumento(self):
        pass                    #Modificar  
    def salir(self):
        QApplication.quit()


if __name__ == "__main__":
    app = QApplication([])
    ventanaPrincipal = VentanaPrincipal()
    ventanaPrincipal.show()
    app.exec()