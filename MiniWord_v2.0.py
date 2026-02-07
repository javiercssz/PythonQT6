from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QWidget,
    QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton,
    QFileDialog, QLabel, QToolBar, QStatusBar, QMessageBox, QColorDialog
)
from PySide6.QtGui import QAction, QKeySequence, QTextDocument, QIcon
from PySide6.QtCore import Qt
import os
from contadorWidget import WordCounterWidget

# IMPORTACIÓN PARA RECONOCIMIENTO DE VOZ
import speech_recognition as sr

class MiniWord(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mini Word")
        self.resize(950, 600)

        # Editor de texto
        self.editor = QTextEdit()
        # Conectamos el cambio de texto a nuestra función que actualiza el widget
        self.editor.textChanged.connect(self.contar_palabras)

        # Panel Buscar/Reemplazar
        self.panel_buscar = QWidget()
        self.panel_buscar.setFixedWidth(250)
        self.panel_buscar.setVisible(False)

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

        # Layout principal
        contenedor = QWidget()
        layout_principal = QHBoxLayout()
        layout_principal.addWidget(self.editor)
        layout_principal.addWidget(self.panel_buscar)
        contenedor.setLayout(layout_principal)
        self.setCentralWidget(contenedor)

        self.ruta_archivo = None

        # Menús
        menu = self.menuBar()
        menu_archivo = menu.addMenu("Archivo")
        menu_editar = menu.addMenu("Editar")

        nuevo = QAction("Nuevo", self)
        nuevo.setShortcut("Ctrl+N")
        nuevo.triggered.connect(self.nuevo)

        abrir = QAction("Abrir", self)
        abrir.setShortcut("Ctrl+O")
        abrir.triggered.connect(self.abrir)

        guardar = QAction("Guardar", self)
        guardar.setShortcut("Ctrl+S")
        guardar.triggered.connect(self.guardar)

        salir = QAction("Salir", self)
        salir.setShortcut("Ctrl+E")
        salir.triggered.connect(self.close)

        buscar = QAction("Buscar / Reemplazar", self)
        buscar.setShortcut("Ctrl+F")
        buscar.triggered.connect(self.toggle_panel_buscar)

        mayusculas = QAction("Texto a mayúculas", self)
        mayusculas.setShortcut("Ctrl+M")
        mayusculas.triggered.connect(self.convertir_a_mayusculas)

        fondo = QAction("Cambiar color de fondo", self)
        fondo.setShortcut("Ctrl+B")
        fondo.triggered.connect(self.cambiarColorFondo)

        voz = QAction("Dictado por voz", self)
        voz.setShortcut("Ctrl+R")
        voz.triggered.connect(self.reconocimiento_voz)

        for a in (nuevo, abrir, guardar, salir):
            menu_archivo.addAction(a)

        for a in (buscar, mayusculas, fondo, voz):
            menu_editar.addAction(a)

        # Barra de herramientas
        barra = QToolBar("Herramientas")
        self.addToolBar(barra)
        barra.addAction(nuevo)
        barra.addAction(abrir)
        barra.addAction(guardar)
        barra.addAction(buscar)
        barra.addAction(voz)

        # Status bar configurada con WordCounterWidget
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        
        # Instanciamos tu clase personalizada de conteo
        self.contador_info = WordCounterWidget()
        # La añadimos de forma permanente a la derecha de la status bar
        self.status.addPermanentWidget(self.contador_info)

    # ----------- FUNCIONES ------------

    def reconocimiento_voz(self):
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

        self.status.showMessage("Escuchando... habla ahora.", 3000)

        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source, timeout=5)

            texto = recognizer.recognize_google(audio, language="es-ES")
            self.editor.insertPlainText(texto + " ")
            self.status.showMessage("Texto agregado desde voz.", 2000)
            # El conteo se actualiza automáticamente por la señal textChanged

        except sr.WaitTimeoutError:
            self.status.showMessage("No se detectó voz.", 2000)
        except sr.UnknownValueError:
            self.status.showMessage("No se entendió lo que dijiste.", 2000)
        except sr.RequestError:
            self.status.showMessage("Error con el servicio de reconocimiento de voz.", 2000)

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
        """Llama al método del widget especializado para procesar el texto"""
        texto_actual = self.editor.toPlainText()
        self.contador_info.update_from_text(texto_actual)

    def toggle_panel_buscar(self):
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
            if not self.editor.find(texto, QTextDocument.FindBackward):
                self.status.showMessage("No se encontró coincidencia anterior.", 2000)

    def buscar_todo(self):
        texto = self.caja_buscar.text()
        if texto:
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
        self.editor.setPlainText(contenido.replace(texto, nuevo))
        QMessageBox.information(self, "Reemplazar todo", "Todas las coincidencias fueron reemplazadas.")

    def convertir_a_mayusculas(self):
        self.editor.setPlainText(self.editor.toPlainText().upper())

    def cambiarColorFondo(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.editor.setStyleSheet(f"background-color: {color.name()};")


if __name__ == "__main__":
    app = QApplication([])
    ventana = MiniWord()
    ventana.show()
    app.exec()