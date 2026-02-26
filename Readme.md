# PyQt6
- Crear una ventana básica:
´
 import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout

class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi App")

        # Creas un layout (caja que organiza los elementos)
        layout = QVBoxLayout()

        # Añades widgets al layout
        label = QLabel("Hola mundo")
        layout.addWidget(label)

        # Esto siempre va al final
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# Esto también siempre va al final del archivo
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec())
´