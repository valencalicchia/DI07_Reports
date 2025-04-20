#!/usr/bin/python3
import sys
from PySide6.QtWidgets import QApplication
from controladores.gestor_informe_controller import ReportController


if __name__ == "__main__":
    """
    Punto de entrada de la aplicación.
    """
    app = QApplication(sys.argv)
    window =  ReportController()
    window.show()
    sys.exit(app.exec())