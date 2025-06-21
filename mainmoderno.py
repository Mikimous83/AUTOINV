import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QGridLayout, QPushButton, QLabel,
                             QLineEdit, QSpinBox, QDoubleSpinBox, QComboBox,
                             QCheckBox, QTextEdit, QTabWidget, QTableWidget,
                             QTableWidgetItem, QMessageBox, QFrame, QScrollArea)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont, QPalette, QColor, QIcon
from modules.clases.auto import Auto
from modules.clases.cliente import Cliente
from modules.clases.concesionario import Concesionario


class ModernCard(QFrame):
    """Widget de tarjeta moderna con sombra y bordes redondeados"""

    def __init__(self, title="", parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.Shape.StyledPanel)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border: 1px solid #e0e0e0;
                border-radius: 12px;
                padding: 20px;
            }
            QLabel {
                color: #2c3e50;
            }

        """)

        self.layout = QVBoxLayout(self)
        if title:
            title_label = QLabel(title)
            title_label.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
            title_label.setStyleSheet("color: #2c3e50; margin-bottom: 15px;")
            self.layout.addWidget(title_label)


class ModernButton(QPushButton):
    """Botón moderno con estilo personalizado"""

    def __init__(self, text, style="primary", parent=None):
        super().__init__(text, parent)
        self.setMinimumHeight(45)
        self.setFont(QFont("Segoe UI", 10, QFont.Weight.Medium))

        if style == "primary":
            self.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 12px 24px;
                    font-weight: 600;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
                QPushButton:pressed {
                    background-color: #21618c;
                }
            """)
        elif style == "success":
            self.setStyleSheet("""
                QPushButton {
                    background-color: #27ae60;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 12px 24px;
                    font-weight: 600;
                }
                QPushButton:hover {
                    background-color: #229954;
                }
                QPushButton:pressed {
                    background-color: #1e8449;
                }
            """)
        elif style == "danger":
            self.setStyleSheet("""
                QPushButton {
                    background-color: #e74c3c;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    padding: 12px 24px;
                    font-weight: 600;
                }
                QPushButton:hover {
                    background-color: #c0392b;
                }
                QPushButton:pressed {
                    background-color: #a93226;
                }
            """)


class ModernLineEdit(QLineEdit):
    """Campo de entrada moderno"""

    def __init__(self, placeholder="", parent=None):
        super().__init__(parent)
        self.setPlaceholderText(placeholder)
        self.setMinimumHeight(40)
        self.setStyleSheet("""
            QLineEdit {
                color: black;  /* Color del texto ingresado */
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 6px;
                padding: 6px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #0078d7;
            }
        """)


class VehiculoTab(QWidget):
    """Tab para registro de vehículos"""
    vehiculo_registrado = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        # Título
        title = QLabel("Registrar Nuevo Vehículo")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        # Formulario en tarjeta
        card = ModernCard()
        form_layout = QGridLayout()

        # Campos del formulario
        self.marca_edit = ModernLineEdit("Ingrese la marca del vehículo")
        self.modelo_edit = ModernLineEdit("Ingrese el modelo")
        self.año_spin = QSpinBox()
        self.año_spin.setRange(1950, 2030)
        self.año_spin.setValue(2024)
        self.año_spin.setMinimumHeight(40)

        self.precio_spin = QDoubleSpinBox()
        self.precio_spin.setRange(0, 999999.99)
        self.precio_spin.setSuffix(" USD")
        self.precio_spin.setMinimumHeight(40)

        self.vin_edit = ModernLineEdit("Número VIN del vehículo")
        self.puertas_spin = QSpinBox()
        self.puertas_spin.setRange(2, 5)
        self.puertas_spin.setValue(4)
        self.puertas_spin.setMinimumHeight(40)


        self.combustible_combo = QComboBox()
        self.combustible_combo.addItems(["Gasolina", "Diésel", "Híbrido", "Eléctrico", "GLP"])
        self.combustible_combo.setStyleSheet("color: #2c3e50; background-color: white;")
        self.combustible_combo.setMinimumHeight(40)


        self.automatico_check = QCheckBox("Transmisión automática")
        self.automatico_check.setStyleSheet("QCheckBox { font-size: 11px; }")

        # Agregar campos al formulario
        labels = ["Marca:", "Modelo:", "Año:", "Precio:", "VIN:", "Puertas:", "Combustible:"]
        widgets = [self.marca_edit, self.modelo_edit, self.año_spin,
                   self.precio_spin, self.vin_edit, self.puertas_spin, self.combustible_combo]

        for i, (label_text, widget) in enumerate(zip(labels, widgets)):
            label = QLabel(label_text)
            label.setFont(QFont("Segoe UI", 10, QFont.Weight.Medium))
            form_layout.addWidget(label, i, 0)
            form_layout.addWidget(widget, i, 1)

        form_layout.addWidget(self.automatico_check, len(labels), 0, 1, 2)

        # Botón registrar
        self.registrar_btn = ModernButton("Registrar Vehículo", "success")
        self.registrar_btn.clicked.connect(self.registrar_vehiculo)
        form_layout.addWidget(self.registrar_btn, len(labels) + 1, 0, 1, 2)

        card.layout.addLayout(form_layout)
        layout.addWidget(card)
        layout.addStretch()

    def registrar_vehiculo(self):
        try:
            auto = Auto(
                marca=self.marca_edit.text(),
                modelo=self.modelo_edit.text(),
                año=self.año_spin.value(),
                precio=self.precio_spin.value(),
                vin=self.vin_edit.text(),
                puertas=self.puertas_spin.value(),
                combustible=self.combustible_combo.currentText(),
                automatico=self.automatico_check.isChecked()
            )

            if not all([auto.marca, auto.modelo, auto.vin]):
                QMessageBox.warning(self, "Error", "Por favor complete todos los campos obligatorios.")
                return

            self.vehiculo_registrado.emit(auto)
            self.limpiar_formulario()
            QMessageBox.information(self, "Éxito", "Vehículo registrado correctamente.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al registrar vehículo: {str(e)}")

    def limpiar_formulario(self):
        self.marca_edit.clear()
        self.modelo_edit.clear()
        self.año_spin.setValue(2024)
        self.precio_spin.setValue(0)
        self.vin_edit.clear()
        self.puertas_spin.setValue(4)
        self.combustible_combo.setCurrentIndex(0)
        self.automatico_check.setChecked(False)


class ClienteTab(QWidget):
    """Tab para registro de clientes"""
    cliente_registrado = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        # Título
        title = QLabel("Registrar Nuevo Cliente")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        # Formulario en tarjeta
        card = ModernCard()
        form_layout = QGridLayout()

        # Campos del formulario
        self.nombre_edit = ModernLineEdit("Nombre del cliente")
        self.apellido_edit = ModernLineEdit("Apellido del cliente")
        self.dni_edit = ModernLineEdit("DNI del cliente")
        self.telefono_edit = ModernLineEdit("Teléfono de contacto")
        self.email_edit = ModernLineEdit("Correo electrónico")

        # Agregar campos al formulario
        labels = ["Nombre:", "Apellido:", "DNI:", "Teléfono:", "Email:"]
        widgets = [self.nombre_edit, self.apellido_edit, self.dni_edit,
                   self.telefono_edit, self.email_edit]

        for i, (label_text, widget) in enumerate(zip(labels, widgets)):
            label = QLabel(label_text)
            label.setFont(QFont("Segoe UI", 10, QFont.Weight.Medium))
            form_layout.addWidget(label, i, 0)
            form_layout.addWidget(widget, i, 1)

        # Botón registrar
        self.registrar_btn = ModernButton("Registrar Cliente", "success")
        self.registrar_btn.clicked.connect(self.registrar_cliente)
        form_layout.addWidget(self.registrar_btn, len(labels), 0, 1, 2)

        card.layout.addLayout(form_layout)
        layout.addWidget(card)
        layout.addStretch()

    def registrar_cliente(self):
        try:
            cliente = Cliente(
                nombre=self.nombre_edit.text(),
                apellido=self.apellido_edit.text(),
                dni=self.dni_edit.text(),
                telefono=self.telefono_edit.text(),
                email=self.email_edit.text()
            )

            if not all([cliente.nombre, cliente.apellido, cliente.dni]):
                QMessageBox.warning(self, "Error", "Por favor complete todos los campos obligatorios.")
                return

            self.cliente_registrado.emit(cliente)
            self.limpiar_formulario()
            QMessageBox.information(self, "Éxito", "Cliente registrado correctamente.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al registrar cliente: {str(e)}")

    def limpiar_formulario(self):
        self.nombre_edit.clear()
        self.apellido_edit.clear()
        self.dni_edit.clear()
        self.telefono_edit.clear()
        self.email_edit.clear()


class VentaTab(QWidget):
    """Tab para realizar ventas"""

    def __init__(self, concesionario, clientes, parent=None):
        super().__init__(parent)
        self.concesionario = concesionario
        self.clientes = clientes
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)

        # Título
        title = QLabel("Realizar Venta")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        # Formulario de venta
        card = ModernCard()
        form_layout = QGridLayout()

        self.vin_edit = ModernLineEdit("VIN del vehículo a vender")
        self.dni_edit = ModernLineEdit("DNI del cliente comprador")

        # Labels y campos
        form_layout.addWidget(QLabel("VIN del Vehículo:"), 0, 0)
        form_layout.addWidget(self.vin_edit, 0, 1)
        form_layout.addWidget(QLabel("DNI del Cliente:"), 1, 0)
        form_layout.addWidget(self.dni_edit, 1, 1)

        # Botón vender
        self.vender_btn = ModernButton("Realizar Venta", "primary")
        self.vender_btn.clicked.connect(self.realizar_venta)
        form_layout.addWidget(self.vender_btn, 2, 0, 1, 2)

        card.layout.addLayout(form_layout)
        layout.addWidget(card)
        layout.addStretch()

    def realizar_venta(self):
        try:
            vin = self.vin_edit.text()
            dni = self.dni_edit.text()

            if not vin or not dni:
                QMessageBox.warning(self, "Error", "Por favor complete todos los campos.")
                return

            cliente = self.clientes.get(dni)
            if not cliente:
                QMessageBox.warning(self, "Error", "Cliente no encontrado. Regístrelo primero.")
                return

            if self.concesionario.vender_vehiculo(vin, cliente):
                QMessageBox.information(self, "Éxito", "¡Venta realizada con éxito!")
                self.vin_edit.clear()
                self.dni_edit.clear()
            else:
                QMessageBox.warning(self, "Error", "Vehículo no disponible o VIN incorrecto.")

        except Exception as e:
            QMessageBox.critical(self, "Error inesperado", f"Ocurrió un error: {str(e)}")


class ReportesTab(QWidget):
    """Tab para mostrar reportes"""

    def __init__(self, concesionario, parent=None):
        super().__init__(parent)
        self.concesionario = concesionario
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        # Título
        title = QLabel("Reportes del Sistema")
        title.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        title.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        layout.addWidget(title)

        # Botón actualizar reportes
        self.actualizar_btn = ModernButton("Actualizar Reportes", "primary")
        self.actualizar_btn.clicked.connect(self.actualizar_reportes)
        layout.addWidget(self.actualizar_btn)

        # Área de texto para reportes
        self.reportes_text = QTextEdit()
        self.reportes_text.setFont(QFont("Consolas", 10))
        self.reportes_text.setStyleSheet("""
            QTextEdit {
                background-color: #ffffff;
                color: #2c3e50;
                font-family: 'Consolas', 'Segoe UI', monospace;
                font-size: 13px;
                border: 1px solid #dcdcdc;
                border-radius: 10px;
                padding: 20px;
                line-height: 1.5em;
            }
        """)

        layout.addWidget(self.reportes_text)

        self.actualizar_reportes()

    def actualizar_reportes(self):
        # Aquí capturamos la salida del método generar_reportes
        import io
        import sys

        # Redirigir stdout para capturar la salida
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()

        try:
            self.concesionario.generar_reportes()
            output = buffer.getvalue()
            self.reportes_text.setPlainText(output)
        except Exception as e:
            self.reportes_text.setPlainText(f"Error al generar reportes: {str(e)}")
        finally:
            sys.stdout = old_stdout


class AutolandMainWindow(QMainWindow):
    """Ventana principal de la aplicación AUTOLAND"""

    def __init__(self):
        super().__init__()
        self.concesionario = Concesionario("AUTOLAND", "Av. La Marina 123, Lima")
        self.clientes = {}
        self.setup_ui()
        self.setup_style()

    def setup_ui(self):
        self.setWindowTitle("AUTOLAND - Sistema de Concesionario")
        self.setMinimumSize(1000, 700)

        # Widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout principal
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)

        # Header
        header = QLabel("🚗 AUTOLAND")
        header.setFont(QFont("Segoe UI", 24, QFont.Weight.Bold))
        header.setStyleSheet("color: #2c3e50; margin-bottom: 20px;")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(header)

        # Tabs
        self.tab_widget = QTabWidget()
        self.tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #bdc3c7;
                border-radius: 8px;
                background-color: #ecf0f1;
            }
            QTabBar::tab {
                background-color: #bdc3c7;
                padding: 12px 20px;
                margin-right: 2px;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
                font-weight: 600;
            }
            QTabBar::tab:selected {
                background-color: white;
                color: #2c3e50;
            }
            QTabBar::tab:hover {
                background-color: #d5dbdb;
            }
        """)

        # Crear tabs
        self.vehiculo_tab = VehiculoTab()
        self.cliente_tab = ClienteTab()
        self.venta_tab = VentaTab(self.concesionario, self.clientes)
        self.reportes_tab = ReportesTab(self.concesionario)

        # Conectar señales
        self.vehiculo_tab.vehiculo_registrado.connect(self.agregar_vehiculo)
        self.cliente_tab.cliente_registrado.connect(self.agregar_cliente)

        # Agregar tabs
        self.tab_widget.addTab(self.vehiculo_tab, "🚙 Vehículos")
        self.tab_widget.addTab(self.cliente_tab, "👥 Clientes")
        self.tab_widget.addTab(self.venta_tab, "💰 Ventas")
        self.tab_widget.addTab(self.reportes_tab, "📊 Reportes")

        layout.addWidget(self.tab_widget)

    def setup_style(self):
        self.setStyleSheet("""
            QMainWindow {
                background-color: #ecf0f1;
            }
            QWidget {
                font-family: 'Segoe UI';
            }
        """)

    def agregar_vehiculo(self, auto):
        self.concesionario.agregar_vehiculo(auto)
        self.reportes_tab.actualizar_reportes()

    def agregar_cliente(self, cliente):
        if cliente.dni in self.clientes:
            QMessageBox.warning(self, "Error", "Cliente ya registrado.")
            return

        self.concesionario.registrar_cliente(cliente)
        self.clientes[cliente.dni] = cliente
        self.reportes_tab.actualizar_reportes()


def main():
    app = QApplication(sys.argv)

    # Configurar estilo de la aplicación
    app.setStyle('Fusion')

    # Crear y mostrar ventana principal
    window = AutolandMainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()