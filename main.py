import sys
from symtable import Class

import layout
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QPushButton


class MiVenta(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.setWindowTitle("MiVenta")
        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.clicked.connect(self.al_pulsar) # conectamos el clic

        #Creamos un layout (caja que organiza los elementos)
        layout = QVBoxLayout()

        #Añadimos widgets al layout
        label = QLabel("Hola")
        layout.addWidget(label)

        #Esto siempre va al final
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def al_pulsar(self):
        texto = self.txtNombre.text() #leemos el campo
        self.txeResultado.append(texto) #lo añadimos al campo de texto
        layout.addWidget(self.btnAceptar)

#Esto siempre va al final del archivo
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVenta()
    ventana.show()
    sys.exit(app.exec())
# _________________________________________________________
#QVBoxLayout Pone elementos uno debajo del otro
#QHBoxLayout Pone elementos uno al lado del otro
#QGridLayout Los pone en una cuadrícula (fila, columna)

# # VBox = vertical
# layout = QVBoxLayout()
# layout.addWidget(boton1)  # arriba
# layout.addWidget(boton2)  # abajo

# # HBox = horizontal
# layout = QHBoxLayout()
# layout.addWidget(boton1)  # izquierda
# layout.addWidget(boton2)  # derecha
#
# # Grid = cuadrícula
# layout = QGridLayout()
# layout.addWidget(label, 0, 0)   # fila 0, columna 0
# layout.addWidget(input, 0, 1)   # fila 0, columna 1
# _________________________________________________________

#Widgets más usados
# from PyQt6.QtWidgets import (QLabel, QLineEdit, QPushButton,
#                               QComboBox, QTextEdit, QCheckBox, QGroupBox)
#
# QLabel("Texto")           # texto estático
# QLineEdit()               # caja de texto para escribir
# QPushButton("Aceptar")    # botón
# QComboBox()               # desplegable
# QTextEdit()               # área de texto grande
# QCheckBox("Activar")      # casilla de marcar
# QGroupBox("Título")       # caja con título que agrupa cosas

