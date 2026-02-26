import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QTextEdit, QComboBox, QCheckBox,
                             QGroupBox, QSlider, QDial)
from PyQt6.QtCore import Qt


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo completo")
        self.setMinimumSize(800, 400)

        # ---- LAYOUT PRINCIPAL: izquierda y derecha ----
        layout_principal = QHBoxLayout()

        # ==============================
        # COLUMNA IZQUIERDA: formulario
        # ==============================
        columna_izquierda = QVBoxLayout()

        gpb = QGroupBox("Datos del cliente")
        layout_gpb = QVBoxLayout()

        # Nombre
        fila1 = QHBoxLayout()
        self.lblNombre = QLabel("Nombre")
        self.txtNombre = QLineEdit()
        fila1.addWidget(self.lblNombre)
        fila1.addWidget(self.txtNombre)

        # Apellidos
        fila2 = QHBoxLayout()
        self.lblApellidos = QLabel("Apellidos")
        self.txtApellidos = QLineEdit()
        fila2.addWidget(self.lblApellidos)
        fila2.addWidget(self.txtApellidos)

        # Provincia
        fila3 = QHBoxLayout()
        lblProvincia = QLabel("Provincia")
        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(["Madrid", "Barcelona", "Sevilla"])
        fila3.addWidget(lblProvincia)
        fila3.addWidget(self.cmbProvincia)

        # CheckBox
        self.chkActivo = QCheckBox("Cliente activo")
        self.chkActivo.stateChanged.connect(self.al_cambiar_check)

        # Slider
        fila5 = QHBoxLayout()
        lblSlider = QLabel("Valoración")
        self.sld = QSlider(Qt.Orientation.Horizontal)
        self.sld.setRange(0, 100)
        self.sld.valueChanged.connect(self.al_mover_slider)
        fila5.addWidget(lblSlider)
        fila5.addWidget(self.sld)

        # Dial
        fila6 = QHBoxLayout()
        lblDial = QLabel("Dial")
        self.dial = QDial()
        self.dial.setRange(0, 100)
        self.dial.valueChanged.connect(self.al_mover_dial)
        fila6.addWidget(lblDial)
        fila6.addWidget(self.dial)

        # Botones
        layout_botones = QHBoxLayout()
        self.btnAnadir = QPushButton("Añadir")
        self.btnAnadir.clicked.connect(self.al_anadir)
        self.btnLimpiar = QPushButton("Limpiar")
        self.btnLimpiar.clicked.connect(self.limpiar)
        layout_botones.addWidget(self.btnAnadir)
        layout_botones.addWidget(self.btnLimpiar)

        # Meter todo en el groupbox
        layout_gpb.addLayout(fila1)
        layout_gpb.addLayout(fila2)
        layout_gpb.addLayout(fila3)
        layout_gpb.addWidget(self.chkActivo)
        layout_gpb.addLayout(fila5)
        layout_gpb.addLayout(fila6)
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

    def al_mover_dial(self, valor):
        if valor < 33:
            self.dial.setStyleSheet("background-color: green")
        elif valor < 66:
            self.dial.setStyleSheet("background-color: orange")
        else:
            self.dial.setStyleSheet("background-color: red")
        self.txeResultado.append(f"Dial: {valor}")

    def al_mover_slider(self, valor):
        if valor < 33:
            self.sld.setStyleSheet("background-color: green")
        elif valor < 66:
            self.sld.setStyleSheet("background-color: orange")
        else:
            self.sld.setStyleSheet("background-color: red")
        self.txeResultado.append(f"Slider: {valor}")

    def al_anadir(self):
        nombre = self.txtNombre.text()
        apellidos = self.txtApellidos.text()
        provincia = self.cmbProvincia.currentText()

        if nombre == "":
            self.lblNombre.setStyleSheet("color: red; font-weight: bold")
            return
        else:
            self.lblNombre.setStyleSheet("")

        if apellidos == "":
            self.lblApellidos.setStyleSheet("color: red; font-weight: bold")
            return
        else:
            self.lblApellidos.setStyleSheet("")

        texto = f"{nombre}, {apellidos}, {provincia}"
        self.txeResultado.append(texto)
        self.limpiar()

    def limpiar(self):
        self.txtNombre.clear()
        self.txtApellidos.clear()
        self.cmbProvincia.setCurrentIndex(0)

    def al_cambiar_check(self):
        if self.chkActivo.isChecked():
            self.txeResultado.append("Cliente marcado como activo")
        else:
            self.txeResultado.append("Cliente marcado como inactivo")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())