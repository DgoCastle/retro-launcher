from pathlib import Path
import json


class RomManager:

    def __init__(self, config_path):

        self.config_path = Path(config_path)

        self.console_paths = self.load_config()

    # ==========================================
    # CARGAR CONFIGURACIÓN
    # ==========================================

    def load_config(self):

        with open(
            self.config_path,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    # ==========================================
    # OBTENER ROMS
    # ==========================================

    def get_roms(self, console):

        # Comprobar que la consola existe
        if console not in self.console_paths:
            return []

        path = Path(self.console_paths[console]).expanduser()

        # Comprobar que la carpeta existe
        if not path.exists():
            return []

        # Obtener archivos
        roms = [
            file
            for file in path.iterdir()
            if file.is_file()
        ]

        # Ordenar alfabéticamente
        return sorted(
            roms,
            key=lambda file: file.name.lower()
        )