import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QGridLayout,
    QWidget,
    QStackedWidget,
    QListWidget,
    QListWidgetItem,
)

from core.rom_manager import RomManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("RetroLauncher")
        self.resize(1280, 720)

        # ==========================================
        # ROM MANAGER
        # ==========================================

        self.rom_manager = RomManager("config/consoles.json")

        # ==========================================
        # STACKED WIDGET
        # ==========================================

        self.pages = QStackedWidget()
        self.setCentralWidget(self.pages)

        # ==========================================
        # PÁGINA PRINCIPAL
        # ==========================================

        self.home_page = self.create_home_page()
        self.pages.addWidget(self.home_page)

    # ==========================================
    # PÁGINA PRINCIPAL
    # ==========================================

    def create_home_page(self):

        page = QWidget()

        layout = QVBoxLayout()
        page.setLayout(layout)

        # Título
        title = QLabel("RetroLauncher")
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)

        # Grid de consolas
        grid = QGridLayout()

        consoles = [
            "NES",
            "FAMICOM",
            "SNES",
            "Game Boy",
            "Game Boy Color",
            "Game Boy Advance",
            "Nintendo 64",
        ]

        for index, console in enumerate(consoles):

            button = QPushButton(console)

            row = index // 3
            column = index % 3

            grid.addWidget(button, row, column)

            # Conectar botón
            button.clicked.connect(
                lambda checked=False, name=console:
                self.open_console(name)
            )

        layout.addLayout(grid)

        return page

    # ==========================================
    # ABRIR CONSOLA
    # ==========================================

    def open_console(self, console):

        page = self.create_console_page(console)

        self.pages.addWidget(page)

        self.pages.setCurrentWidget(page)

    # ==========================================
    # PÁGINA DE CONSOLA
    # ==========================================

    def create_console_page(self, console):

        page = QWidget()

        layout = QVBoxLayout()
        page.setLayout(layout)

        # Título
        title = QLabel(console)
        title.setAlignment(Qt.AlignCenter)

        layout.addWidget(title)

        # Lista de ROMs
        rom_list = QListWidget()

        roms = self.rom_manager.get_roms(console)

        for rom in roms:

            # Crear elemento de la lista
            item = QListWidgetItem(rom.name)

            # Guardar la ruta completa de la ROM
            item.setData(Qt.UserRole, str(rom))

            rom_list.addItem(item)

        # Doble clic en una ROM
        rom_list.itemDoubleClicked.connect(self.launch_rom)

        layout.addWidget(rom_list)

        # Botón volver
        back_button = QPushButton("← Volver")

        back_button.clicked.connect(self.go_home)

        layout.addWidget(back_button)

        return page

    # ==========================================
    # DOBLE CLIC EN ROM
    # ==========================================

    def launch_rom(self, item):

        rom_path = item.data(Qt.UserRole)

        print("ROM seleccionada:")
        print(rom_path)

    # ==========================================
    # VOLVER AL INICIO
    # ==========================================

    def go_home(self):

        self.pages.setCurrentIndex(0)


def main():

    app = QApplication(sys.argv)

    # ==========================================
    # CARGAR QSS
    # ==========================================

    with open("styles/main.qss", "r", encoding="utf-8") as file:
        app.setStyleSheet(file.read())

    # ==========================================
    # VENTANA
    # ==========================================

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()