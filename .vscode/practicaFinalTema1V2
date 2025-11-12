from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QFileDialog,
    QMessageBox, QLabel, QStatusBar, QToolBar
)
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import Qt
import os


class MiniWord(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Word")
        self.resize(800, 600)

        # ---- Área de texto ----
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.editor.textChanged.connect(self.contar_palabras)

        # ---- Archivo actual ----
        self.ruta_archivo = None

        # ---- Barra de menú ----
        barra_menu = self.menuBar()
        menu_archivo = barra_menu.addMenu("Archivo")

        # Crear acciones del menú
        nuevo = QAction("Nuevo", self)
        nuevo.setShortcut(QKeySequence("Ctrl+N"))
        nuevo.triggered.connect(self.nuevo)

        abrir = QAction("Abrir", self)
        abrir.setShortcut(QKeySequence("Ctrl+O"))
        abrir.triggered.connect(self.abrir)

        guardar = QAction("Guardar", self)
        guardar.setShortcut(QKeySequence("Ctrl+S"))
        guardar.triggered.connect(self.guardar)

        salir = QAction("Salir", self)
        salir.setShortcut(QKeySequence("Ctrl+E"))
        salir.triggered.connect(self.salir)

        # Agregar al menú
        for accion in (nuevo, abrir, guardar, salir):
            menu_archivo.addAction(accion)

        # ---- Barra de herramientas ----
        barra_herramientas = QToolBar("Herramientas")
        self.addToolBar(barra_herramientas)
        barra_herramientas.addAction(nuevo)
        barra_herramientas.addAction(abrir)
        barra_herramientas.addAction(guardar)

        # ---- Barra de estado ----
        self.barra_estado = QStatusBar()
        self.setStatusBar(self.barra_estado)
        self.contador = QLabel("Palabras: 0")
        self.barra_estado.addPermanentWidget(self.contador)

    def nuevo(self):
        """Limpia el texto para empezar de cero."""
        self.editor.clear()
        self.ruta_archivo = None                                               # <===--Aclarar y entender-->
        self.barra_estado.showMessage("Nuevo documento listo.", 3000)

    def abrir(self):
        """Abre un archivo de texto y lo muestra en el editor."""        """<--Aclarar y entender-->"""
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if ruta:
            with open(ruta, "r", encoding="utf-8") as f:
                contenido = f.read()
            self.editor.setPlainText(contenido)
            self.ruta_archivo = ruta
            self.barra_estado.showMessage(f"Archivo abierto: {os.path.basename(ruta)}", 3000)

    def guardar(self):
        """Guarda el texto actual en un archivo."""   """<--Aclarar y entender-->"""
        if not self.ruta_archivo:
            ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
            if not ruta:
                return
            self.ruta_archivo = ruta

        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            f.write(self.editor.toPlainText())

        self.barra_estado.showMessage("Archivo guardado correctamente.", 3000)

    def salir(self):
        self.close()

    def contar_palabras(self):
        """Actualiza el contador de palabras en la barra de estado."""   """<--Aclarar y entender-->"""
        texto = self.editor.toPlainText().strip()
        cantidad = len(texto.split()) if texto else 0
        self.contador.setText(f"Palabras: {cantidad}")


if __name__ == "__main__":
    app = QApplication([])
    ventana = MiniWord()
    ventana.show()
    app.exec()
