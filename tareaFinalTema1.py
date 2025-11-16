from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QWidget,
    QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QFileDialog, QLabel, QToolBar, QStatusBar, QMessageBox, QColorDialog
)
from PySide6.QtGui import QAction, QKeySequence, QTextDocument, QIcon
from PySide6.QtCore import Qt
import os


class MiniWord(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Word")
        self.resize(950, 600)

    
        self.editor = QTextEdit()
        self.editor.textChanged.connect(self.contar_palabras)


        self.panel_buscar = QWidget()
        self.panel_buscar.setFixedWidth(250)
        self.panel_buscar.setVisible(False)  # oculto al inicio

        layout_panel = QVBoxLayout()

        self.caja_buscar = QLineEdit()
        self.caja_buscar.setPlaceholderText("Texto a buscar...")

        self.caja_reemplazar = QLineEdit()
        self.caja_reemplazar.setPlaceholderText("Texto a reemplazar...")

        boton_buscar = QPushButton("Buscar siguiente")
        boton_anterior = QPushButton("Buscar anterior")
        boton_todo = QPushButton("Buscar todo")
        boton_reemplazar = QPushButton("Reemplazar siguiente")
        boton_reemplazar_todo = QPushButton("Reemplazar todo")
        mayusculas = QPushButton("Convertir a mayúculas")

        boton_buscar.clicked.connect(self.buscar_siguiente)
        boton_anterior.clicked.connect(self.buscar_anterior)
        boton_todo.clicked.connect(self.buscar_todo)
        boton_reemplazar.clicked.connect(self.reemplazar_siguiente)
        boton_reemplazar_todo.clicked.connect(self.reemplazar_todo)

        layout_panel.addWidget(QLabel(" Buscar y Reemplazar"))
        layout_panel.addWidget(self.caja_buscar)
        layout_panel.addWidget(self.caja_reemplazar)
        layout_panel.addWidget(boton_buscar)
        layout_panel.addWidget(boton_anterior)
        layout_panel.addWidget(boton_todo)
        layout_panel.addWidget(boton_reemplazar)
        layout_panel.addWidget(boton_reemplazar_todo)
        layout_panel.addStretch()

        self.panel_buscar.setLayout(layout_panel)


        contenedor = QWidget()
        layout_principal = QHBoxLayout()
        layout_principal.addWidget(self.editor)
        layout_principal.addWidget(self.panel_buscar)
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)


        self.ruta_archivo = None


        menu = self.menuBar()
        menu_archivo = menu.addMenu("Archivo")
        menu_editar = menu.addMenu("Editar")


        nuevo = QAction(QIcon.fromTheme("document-new"), "Nuevo", self)
        nuevo.setShortcut(QKeySequence("Ctrl+N"))
        nuevo.triggered.connect(self.nuevo)

        abrir = QAction(QIcon.fromTheme("document-open"), "Abrir", self)
        abrir.setShortcut(QKeySequence("Ctrl+O"))
        abrir.triggered.connect(self.abrir)

        guardar = QAction(QIcon.fromTheme("document-save"), "Guardar", self)
        guardar.setShortcut(QKeySequence("Ctrl+S"))
        guardar.triggered.connect(self.guardar)

        salir = QAction(QIcon.fromTheme("application-exit"), "Salir", self)
        salir.setShortcut(QKeySequence("Ctrl+E"))
        salir.triggered.connect(self.close)

        buscar = QAction(QIcon.fromTheme("edit-find"), "Buscar / Reemplazar", self)
        buscar.setShortcut(QKeySequence("Ctrl+F"))
        buscar.triggered.connect(self.toggle_panel_buscar)

        mayusculas = QAction(QIcon.fromTheme("format-text-uppercase"), "Texto a mayúculas", self)
        mayusculas.setShortcut(QKeySequence("Ctrl+M"))
        mayusculas.triggered.connect(self.convertir_a_mayusculas)

        fondo = QAction(QIcon.fromTheme("preferences-desktop-color"),   "Cambiar color de fondo", self)
        fondo.setShortcut(QKeySequence("Ctrl+B"))
        fondo.triggered.connect(self.cambiarColorFondo)
        
        for a in (nuevo, abrir, guardar, salir):
            menu_archivo.addAction(a)
        
        for a in (buscar, mayusculas, fondo):
            menu_editar.addAction(a)

    
        barra = QToolBar("Herramientas")
        self.addToolBar(barra)
        barra.addAction(nuevo)
        barra.addAction(abrir)
        barra.addAction(guardar)
        barra.addAction(buscar)

    
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        self.label_palabras = QLabel("Palabras: 0")
        self.status.addPermanentWidget(self.label_palabras)



    def nuevo(self):
        self.editor.clear()
        self.ruta_archivo = None
        self.status.showMessage("Nuevo documento creado", 2000)

    def abrir(self):
        ruta, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Archivos de texto (*.txt)")
        if ruta:
            with open(ruta, "r", encoding="utf-8") as f:
                self.editor.setPlainText(f.read())
            self.ruta_archivo = ruta
            self.status.showMessage(f"Archivo abierto: {os.path.basename(ruta)}", 2000)

    def guardar(self):
        if not self.ruta_archivo:
            ruta, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Archivos de texto (*.txt)")
            if not ruta:
                return
            self.ruta_archivo = ruta

        with open(self.ruta_archivo, "w", encoding="utf-8") as f:
            f.write(self.editor.toPlainText())

        self.status.showMessage("Archivo guardado correctamente.", 2000)

    def contar_palabras(self):
        texto = self.editor.toPlainText().strip()

        if texto:
            # Si el texto no está vacío, contamos las palabras
                n = len(texto.split())
        else:
            # Si el texto está vacío, el número de palabras es 0
            n = 0
        self.label_palabras.setText(f"Palabras: {n}")

    def toggle_panel_buscar(self):
        """Muestra u oculta el panel lateral."""
        visible = not self.panel_buscar.isVisible()
        self.panel_buscar.setVisible(visible)

    def buscar_siguiente(self):
        texto = self.caja_buscar.text()
        if texto:
            if not self.editor.find(texto):
                self.status.showMessage("No se encontró más coincidencias.", 2000)

    def buscar_anterior(self):
        texto = self.caja_buscar.text()
        if texto:
            if not self.editor.find(texto, QTextDocument.FindFlag.FindBackward):
                self.status.showMessage("No se encontró coincidencia anterior.", 2000)

    def buscar_todo(self):
        texto = self.caja_buscar.text()
        if not texto:
            return
        contenido = self.editor.toPlainText()
        cantidad = contenido.count(texto)
        QMessageBox.information(self, "Buscar todo", f"Se encontraron {cantidad} coincidencias.")

    def reemplazar_siguiente(self):
        texto = self.caja_buscar.text()
        nuevo = self.caja_reemplazar.text()
        if texto:
            cursor = self.editor.textCursor()
            if cursor.hasSelection() and cursor.selectedText() == texto:
                cursor.insertText(nuevo)
            self.buscar_siguiente()

    def reemplazar_todo(self):
        texto = self.caja_buscar.text()
        nuevo = self.caja_reemplazar.text()
        contenido = self.editor.toPlainText()
        nuevo_texto = contenido.replace(texto, nuevo)
        self.editor.setPlainText(nuevo_texto)
        QMessageBox.information(self, "Reemplazar todo", "Todas las coincidencias fueron reemplazadas.")

    def convertir_a_mayusculas(self):
        texto = self.editor.toPlainText().upper()
        self.editor.setPlainText(texto)
    
    def cambiarColorFondo(self, color):
        color = QColorDialog.getColor()
        if color.isValid():
            self.editor.setStyleSheet(f"background-color: {color.name()};")

if __name__ == "__main__":
    app = QApplication([])
    ventana = MiniWord()
    ventana.show()
    app.exec()