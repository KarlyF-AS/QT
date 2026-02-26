import sys
from symtable import Class

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton


class MiVenta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MiVenta")

        layout = QVBoxLayout()

        # 1. creamos el widget
        self.btnAceptar = QPushButton("Aceptar")
        self.btnCancelar = QPushButton("Cancelar")

        # 2. Lo conectamos a una funcion
        self.btnAceptar.clicked.connect(self.al_pulsar)
        self.btnCancelar.clicked.connect(self.al_pulsar)

        # 3. Lo añadimo al layout <- esto es lo que lo hace visible
        layout.addWidget(self.btnAceptar)
        layout.addWidget(self.btnCancelar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def al_pulsar(self):
        print("Boton pulsado")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVenta()
    ventana.show()
    sys.exit(app.exec())

# **La regla es siempre la misma para TODO** — label, botón, input... lo que sea:
# ```
# 1. Crear     →   self.btn = QPushButton("texto")
# 2. Conectar  →   self.btn.clicked.connect(self.funcion)   # solo botones
# 3. Añadir    →   layout.addWidget(self.btn)