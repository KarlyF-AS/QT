import sys
import sqlite3
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QTextEdit, QComboBox, QCheckBox,
                             QGroupBox, QSlider)
from PyQt6.QtCore import Qt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo completo")
        self.setMinimumSize(800, 400)

# _________________________________________________________________________
#  REPORTLAB
# ______________________________________________________________________

        # # 1. Crear el PDF
        # #Título grande
        # pdf = canvas.Canvas("peliculas.pdf", pagesize=A4)
        # pdf.drawString(100,780, "Lista de peliculas")
        #
        # # 2. Escribir texto
        # pdf.setFont("Helvetica", 18)
        # pdf.drawString(100,780, "Titulo: El padrino")
        # pdf.drawString(100, 730, "Director: Coppola")
        # # Línea separadora
        # pdf.line(100, 720, 500, 720)
        # # 3. Guardar
        #pdf.save()
# _________________________________________________________________________
        #CONEXION DB
# _________________________________________________________________________
        # Conectar y guardar como self. para usarlo en toda la clase
        self.conexion = sqlite3.connect("peliculas.db")
        self.cursor = self.conexion.cursor()

        # Crear la tabla si no existe
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS peliculas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT,
                    director TEXT,
                    genero TEXT,
                    puntuacion INTEGER
                )
            """)
        self.conexion.commit()

        # ---- LAYOUT PRINCIPAL: izquierda y derecha ----
        layout_principal = QHBoxLayout()

        # ==============================
        # COLUMNA IZQUIERDA: formulario
        # ==============================
        columna_izquierda = QVBoxLayout()

        gpb = QGroupBox("Datos de la pelicula")
        layout_gpb = QVBoxLayout()

        # Nombre
        fila1 = QHBoxLayout()
        self.lblTitulo = QLabel("Titulo")
        self.txtTitulo = QLineEdit()
        fila1.addWidget(self.lblTitulo)
        fila1.addWidget(self.txtTitulo)

        # Director
        fila2 = QHBoxLayout()
        self.lblDirector = QLabel("Director")
        self.txtDirector = QLineEdit()
        fila2.addWidget(self.lblDirector)
        fila2.addWidget(self.txtDirector)

        # Género
        fila3 = QHBoxLayout()
        lblGénero = QLabel("Género")
        self.cmbGénero = QComboBox()
        self.cmbGénero.addItems(["Accion", "Comedia", "Drama", "Terror"])
        fila3.addWidget(lblGénero)
        fila3.addWidget(self.cmbGénero)

        # # CheckBox
        # self.chkActivo = QCheckBox("Cliente activo")
        # self.chkActivo.stateChanged.connect(self.al_cambiar_check)

        # Slider
        fila5 = QHBoxLayout()
        lblSlider = QLabel("Puntuacion")
        self.sld = QSlider(Qt.Orientation.Horizontal)
        self.sld.setRange(0, 10)
        self.sld.valueChanged.connect(self.al_mover_slider)
        fila5.addWidget(lblSlider)
        fila5.addWidget(self.sld)

        # # Dial
        # fila6 = QHBoxLayout()
        # lblDial = QLabel("Dial")
        # self.dial = QDial()
        # self.dial.setRange(0, 100)
        # self.dial.valueChanged.connect(self.al_mover_dial)
        # fila6.addWidget(lblDial)
        # fila6.addWidget(self.dial)

        # Botones
        layout_botones = QHBoxLayout()
        self.btnAnadir = QPushButton("Añadir")
        self.btnAnadir.clicked.connect(self.al_anadir)
        self.btnLimpiar = QPushButton("Limpiar")
        self.btnLimpiar.clicked.connect(self.limpiar)
        layout_botones.addWidget(self.btnAnadir)
        layout_botones.addWidget(self.btnLimpiar)
        #Boton reporlab y bd
        self.btnPDF = QPushButton("PDF")
        self.btnPDF.clicked.connect(self.generar_pdf)
        layout_botones.addWidget(self.btnPDF)

        # Meter todo en el groupbox
        layout_gpb.addLayout(fila1)
        layout_gpb.addLayout(fila2)
        layout_gpb.addLayout(fila3)
        # layout_gpb.addWidget(self.chkActivo)
        layout_gpb.addLayout(fila5)
        # layout_gpb.addLayout(fila6)
        gpb.setLayout(layout_gpb)

        # Meter groupbox y botones en columna izquierda
        columna_izquierda.addWidget(gpb)
        columna_izquierda.addLayout(layout_botones)

        # ==============================
        # COLUMNA DERECHA: área de texto
        # ==============================
        columna_derecha = QVBoxLayout()
        lblResultado = QLabel("Resultado")
        self.txeResultado = QTextEdit()
        columna_derecha.addWidget(lblResultado)
        columna_derecha.addWidget(self.txeResultado)

        # ---- JUNTAR LAS DOS COLUMNAS ----
        layout_principal.addLayout(columna_izquierda)
        layout_principal.addLayout(columna_derecha)

        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

    # ---- FUNCIONES ----

    # def al_mover_dial(self, valor):
    #     if valor < 33:
    #         self.dial.setStyleSheet("background-color: green")
    #     elif valor < 66:
    #         self.dial.setStyleSheet("background-color: orange")
    #     else:
    #         self.dial.setStyleSheet("background-color: red")
    #     self.txeResultado.append(f"Dial: {valor}")

    # Función
    def generar_pdf(self):
        self.cursor.execute("SELECT * FROM peliculas")
        peliculas = self.cursor.fetchall()

        pdf = canvas.Canvas("peliculas.pdf", pagesize=A4)

        pdf.setFont("Helvetica-Bold", 18)
        pdf.drawString(100, 780, "Lista de películas")

        y = 740  # posición donde empieza la lista
        pdf.setFont("Helvetica", 12)

        for pelicula in peliculas:
            texto = f"{pelicula[1]}, {pelicula[2]}, {pelicula[3]}, Puntuación: {pelicula[4]}"
            pdf.drawString(100, y, texto)
            y -= 20  # bajar 20 puntos por cada línea

        pdf.save()
        self.txeResultado.append("PDF generado: peliculas.pdf")

    def al_mover_slider(self, valor):
        if valor < 33:
            self.sld.setStyleSheet("background-color: green")
        elif valor < 66:
            self.sld.setStyleSheet("background-color: orange")
        else:
            self.sld.setStyleSheet("background-color: red")

    def al_anadir(self):
        titulo = self.txtTitulo.text()
        Director = self.txtDirector.text()
        Género = self.cmbGénero.currentText()
        punctuacion = self.sld.value()

        if titulo == "":
            self.lblTitulo.setStyleSheet("color: red; font-weight: bold")
            return
        else:
            self.lblTitulo.setStyleSheet("")

        if Director == "":
            self.lblDirector.setStyleSheet("color: red; font-weight: bold")
            return
        else:
            self.lblDirector.setStyleSheet("")

            # Guardar en la base de datos
        self.cursor.execute("INSERT INTO peliculas (titulo, director, genero, puntuacion) VALUES (?,?,?,?)",
                            (titulo, Director, Género, punctuacion))
        self.conexion.commit()

        texto = f"{titulo}, {Director}, {Género}, Puntuación: {punctuacion}"
        self.txeResultado.append(texto)
        self.limpiar()

    def limpiar(self):
        self.txtTitulo.clear()
        self.txtDirector.clear()
        self.cmbGénero.setCurrentIndex(0)
        self.sld.setValue(0)

    # def al_cambiar_check(self):
    #     if self.chkActivo.isChecked():
    #         self.txeResultado.append("Cliente marcado como activo")
    #     else:
    #         self.txeResultado.append("Cliente marcado como inactivo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())