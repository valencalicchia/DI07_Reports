from PySide6.QtWidgets import QWidget, QFileDialog, QInputDialog
from utilidades.message_box import MessageBox
from vistas.gestorinformes_ui import Ui_GestorInformes
from controladores import crearinforme
import os

class ReportController(QWidget):
    def __init__(self):
        super().__init__()
        try:
            self.ui = Ui_GestorInformes()
            self.ui.setupUi(self)

            self.ui.vcTxtRutaInf.mousePressEvent = self.select_report_dir
            self.ui.vcTxtRutaGuardado.mousePressEvent = self.select_save_dir
            self.ui.vcBtnGuardar.clicked.connect(self.generate)

        except Exception as e:
            MessageBox("No se pudo iniciar la interfaz de informes.", "error", str(e)).show()

    def select_report_dir(self, event):
        dir = QFileDialog.getExistingDirectory(
            self, "Selecciona carpeta de informes", os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        if dir:
            self.ui.vcTxtRutaInf.setText(dir)
            self.ui.vcCbo.setEnabled(True)
            self.get_reports(dir)

    def select_save_dir(self, event):
        dir = QFileDialog.getExistingDirectory(
            self, "Selecciona carpeta para guardar informes", os.path.expanduser("~"),
            QFileDialog.ShowDirsOnly
        )
        if dir:
            self.ui.vcTxtRutaGuardado.setText(dir)

    def get_reports(self, ruta):
        try:
            ficheros = [archivo for archivo in os.listdir(ruta) if archivo.lower().endswith(('.jrxml', '.jasper'))]
            self.ui.vcCbo.clear()
            self.ui.vcCbo.addItems(ficheros)
        except Exception as e:
            MessageBox(f"No se pudieron listar los informes disponibles.\n{str(e)}", "error").show()

    def get_params(self, descripcion):
        titulo = "Parámetro requerido"
        texto = descripcion
        valor, confirmado = QInputDialog.getText(self, titulo, texto)
        return valor if confirmado and valor else None

    def generate(self):
        try:
            informes_con_dato = {
                'Informe_AlbaranPedido': "Introduce el número del pedido",
                'Informe_AlbaranCliente': "Introduce el número del cliente",
                'Informe_AlbaranClienteSub': "Introduce el número del cliente"
            }

            informe_elegido = self.ui.vcCbo.currentText().replace('.jrxml', '')

            parametros = {}
            if informe_elegido in informes_con_dato:
                texto_solicitud = informes_con_dato[informe_elegido]
                dato = self.get_params(texto_solicitud)
                if not dato:
                    return
                clave = 'param_pedido' if 'Pedido' in informe_elegido else 'param_cliente'
                parametros[clave] = dato

            origen = self.ui.vcTxtRutaInf.text()
            if not origen:
                MessageBox("Debe indicar una carpeta de origen válida y un informe.", "error").show()
                return

            destino = self.ui.vcTxtRutaGuardado.text() or origen
            if not self.ui.vcTxtRutaGuardado.text():
                MessageBox(f"No se especificó carpeta de salida. Se usará la misma de origen:\n{destino}").show()

            archivo_in = os.path.join(origen, f"{informe_elegido}.jrxml")
            archivo_out = os.path.join(destino, informe_elegido)

            crearinforme.advanced_example_using_database(archivo_in, archivo_out, parametros)
            MessageBox(f"Informe generado exitosamente en:\n{archivo_out}").show()

        except Exception as e:
            MessageBox("Se produjo un error durante la generación del informe.", "error", str(e)).show()
