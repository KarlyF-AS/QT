import sys

import layout
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QTextEdit, QWidget


class MiVenta(QMainWindow):
    def __init__(self):
        # Crear campos
        super().__init__()
        self.setWindowTitle('Mi Venta')

        #creamos componentes
        self.txtNombre = QLineEdit()
        self.txt.setPlaceholderText('Nombre')
        self.txtApellidos = QLineEdit()
        self.txtApellidos.setPlaceholderText('Apellidos')
        self.txeResultado = QTextEdit()  # área grande donde se muestra todo

        self.btnAnadir = QPushButton("Añadir")
        self.btnAnadir.clicked.connect(self.al_anadir)

        #CReamso el layout y añadimos los componentes
        layout.addWidget(self.btnAnadir)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def al_anadir(self):
        nombre = self.txtNombre.text() #leer campo
        apellidos = self.txtApellidos.text()

        texto = f"{nombre}, {apellidos}"
        self.txeResultado.append(texto)  # append = añade una línea nueva
        self.txeResultado.setText(texto)    # setText = REEMPLAZA todo el texto


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVenta()
    ventana.show()
    sys.exit(app.exec())