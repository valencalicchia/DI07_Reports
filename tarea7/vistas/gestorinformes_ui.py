# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gestorinformes.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import imagenes.imagenes_rc

class Ui_GestorInformes(object):
    def setupUi(self, GestorInformes):
        if not GestorInformes.objectName():
            GestorInformes.setObjectName(u"GestorInformes")
        GestorInformes.resize(365, 260)
        GestorInformes.setMinimumSize(QSize(365, 260))
        GestorInformes.setMaximumSize(QSize(365, 260))
        icon = QIcon()
        icon.addFile(u":/imagenes/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        GestorInformes.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(GestorInformes)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.vcLblImage = QLabel(GestorInformes)
        self.vcLblImage.setObjectName(u"vcLblImage")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcLblImage.sizePolicy().hasHeightForWidth())
        self.vcLblImage.setSizePolicy(sizePolicy)
        self.vcLblImage.setMinimumSize(QSize(150, 0))
        self.vcLblImage.setStyleSheet(u"image: url(:./imagenes/logo.png);")

        self.horizontalLayout.addWidget(self.vcLblImage)

        self.vcLblTitulo = QLabel(GestorInformes)
        self.vcLblTitulo.setObjectName(u"vcLblTitulo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.vcLblTitulo.sizePolicy().hasHeightForWidth())
        self.vcLblTitulo.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.vcLblTitulo.setFont(font)
        self.vcLblTitulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.vcLblTitulo)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.vcTxtRutaGuardado = QLineEdit(GestorInformes)
        self.vcTxtRutaGuardado.setObjectName(u"vcTxtRutaGuardado")
        self.vcTxtRutaGuardado.setEnabled(True)
        font1 = QFont()
        font1.setPointSize(11)
        self.vcTxtRutaGuardado.setFont(font1)

        self.gridLayout.addWidget(self.vcTxtRutaGuardado, 2, 1, 1, 1)

        self.vcLblTipo_2 = QLabel(GestorInformes)
        self.vcLblTipo_2.setObjectName(u"vcLblTipo_2")
        font2 = QFont()
        font2.setPointSize(11)
        font2.setBold(True)
        self.vcLblTipo_2.setFont(font2)

        self.gridLayout.addWidget(self.vcLblTipo_2, 2, 0, 1, 1)

        self.vcBtnGuardar = QPushButton(GestorInformes)
        self.vcBtnGuardar.setObjectName(u"vcBtnGuardar")
        self.vcBtnGuardar.setEnabled(True)
        self.vcBtnGuardar.setFont(font2)

        self.gridLayout.addWidget(self.vcBtnGuardar, 3, 1, 1, 1)

        self.vcLblTipo = QLabel(GestorInformes)
        self.vcLblTipo.setObjectName(u"vcLblTipo")
        self.vcLblTipo.setFont(font2)

        self.gridLayout.addWidget(self.vcLblTipo, 1, 0, 1, 1)

        self.vcCbo = QComboBox(GestorInformes)
        self.vcCbo.setObjectName(u"vcCbo")
        self.vcCbo.setEnabled(True)
        self.vcCbo.setFont(font1)

        self.gridLayout.addWidget(self.vcCbo, 1, 1, 1, 1)

        self.vcLblRutaInf = QLabel(GestorInformes)
        self.vcLblRutaInf.setObjectName(u"vcLblRutaInf")
        self.vcLblRutaInf.setFont(font2)

        self.gridLayout.addWidget(self.vcLblRutaInf, 0, 0, 1, 1)

        self.vcTxtRutaInf = QLineEdit(GestorInformes)
        self.vcTxtRutaInf.setObjectName(u"vcTxtRutaInf")
        self.vcTxtRutaInf.setFont(font1)

        self.gridLayout.addWidget(self.vcTxtRutaInf, 0, 1, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(GestorInformes)

        QMetaObject.connectSlotsByName(GestorInformes)
    # setupUi

    def retranslateUi(self, GestorInformes):
        GestorInformes.setWindowTitle(QCoreApplication.translate("GestorInformes", u"Gestor de Informes", None))
        self.vcLblImage.setText("")
        self.vcLblTitulo.setText(QCoreApplication.translate("GestorInformes", u"GENERAR INFORMES", None))
        self.vcLblTipo_2.setText(QCoreApplication.translate("GestorInformes", u"Ruta de guardado", None))
        self.vcBtnGuardar.setText(QCoreApplication.translate("GestorInformes", u"Generar", None))
        self.vcLblTipo.setText(QCoreApplication.translate("GestorInformes", u"Tipo", None))
        self.vcLblRutaInf.setText(QCoreApplication.translate("GestorInformes", u"Ruta de los informes", None))
    # retranslateUi

