import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget,
                             QVBoxLayout, QHBoxLayout, QLabel, QLineEdit,
                             QPushButton, QTextEdit, QComboBox, QCheckBox,
                             QGroupBox, QTabWidget, QSlider, QDial)
from PyQt6.QtCore import Qt


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo completo")
        self.dial = QDial()
        self.dial.setRange(0, 100)
        self.dial.valueChanged.connect(self.al_mover_dial)

        # ---- LAYOUT PRINCIPAL ----
        layout_principal = QVBoxLayout()

        # ---- GROUPBOX con formulario ----
        gpb = QGroupBox("Datos del cliente")
        layout_gpb = QVBoxLayout()

        # Fila 1: Nombre
        fila1 = QHBoxLayout()
        self.lblNombre = QLabel("Nombre")
        self.txtNombre = QLineEdit()
        fila1.addWidget(self.lblNombre)
        fila1.addWidget(self.txtNombre)

        # Fila 2: Apellidos
        fila2 = QHBoxLayout()
        self.lblApellidos = QLabel("Apellidos")
        self.txtApellidos = QLineEdit()
        fila2.addWidget(self.lblApellidos)
        fila2.addWidget(self.txtApellidos)

        # Fila 3: Provincia (ComboBox)
        fila3 = QHBoxLayout()
        lblProvincia = QLabel("Provincia")
        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(["Madrid", "Barcelona", "Sevilla"])
        fila3.addWidget(lblProvincia)
        fila3.addWidget(self.cmbProvincia)

        # Fila 4: CheckBox
        self.chkActivo = QCheckBox("Cliente activo")
        self.chkActivo.stateChanged.connect(self.al_cambiar_check)

        # Fila 5: Slider
        fila5 = QHBoxLayout()
        lblSlider = QLabel("Valoración")
        self.sld = QSlider(Qt.Orientation.Horizontal)
        self.sld.setRange(0, 100)
        self.sld.valueChanged.connect(self.al_mover_slider)
        fila5.addWidget(lblSlider)
        fila5.addWidget(self.sld)

        # Añadir filas al groupbox
        layout_gpb.addLayout(fila1)
        layout_gpb.addLayout(fila2)
        layout_gpb.addLayout(fila3)
        layout_gpb.addWidget(self.chkActivo)
        layout_gpb.addLayout(fila5)
        layout_principal.addWidget(self.dial)
        gpb.setLayout(layout_gpb)

        # ---- AREA DE TEXTO donde se muestran los datos ----
        self.txeResultado = QTextEdit()

        # ---- BOTONES ----
        self.btnAnadir = QPushButton("Añadir")
        self.btnAnadir.clicked.connect(self.al_anadir)

        self.btnLimpiar = QPushButton("Limpiar")
        self.btnLimpiar.clicked.connect(self.limpiar)

        layout_botones = QHBoxLayout()
        layout_botones.addWidget(self.btnAnadir)
        layout_botones.addWidget(self.btnLimpiar)

        self.dial.setStyleSheet("background-color: purple")
        self.sld.setStyleSheet("background-color: green")

        # ---- JUNTAR TODO ----
        layout_principal.addWidget(gpb)
        layout_principal.addWidget(self.txeResultado)
        layout_principal.addLayout(layout_botones)

        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

    # ---- FUNCIONES ----
    def al_mover_dial(self, valor):
        if valor < 33:
            self.dial.setStyleSheet("background-color: red; font-weight: bold")
        elif valor < 66:
            self.dial.setStyleSheet("background-color: green; font-weight: orange")
        else:
            self.dial.setStyleSheet("background-color: purple; font-weight: red")
        self.txeResultado.append(f"Dial: {valor}")

    def al_anadir(self):
        nombre = self.txtNombre.text()
        apellidos = self.txtApellidos.text()
        provincia = self.cmbProvincia.currentText()

        # Validar que no estén vacíos
        if nombre == "":
            self.lblNombre.setStyleSheet("color: red; font-weight: bold")
            return
        else:
            self.lblNombre.setStyleSheet("")  # quitar el rojo si ya tiene texto

        if apellidos == "":
            self.lblApellidos.setStyleSheet("color: red; font-weight: bold")
            return
        else:
            self.lblApellidos.setStyleSheet("")

        # Si todo está bien, mostrar en el área de texto
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

    def al_mover_slider(self, valor):
        if valor < 33:
            self.sld.setStyleSheet("background-color: red; font-weight: bold")
        elif valor < 66:
            self.sld.setStyleSheet("background-color: green; font-weight: orange")
        else:
            self.sld.setStyleSheet("background-color: purple; font-weight: red")
        self.txeResultado.append(f"Slider: {valor}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
