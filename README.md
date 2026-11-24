# 🎮 RetroLauncher

Launcher de emuladores retro hecho en **Python + PySide6 (Qt)**. Organiza tus ROMs por consola en una interfaz gráfica sencilla.

> 🚧 **Beta.** La parte que abre el emulador (`core/emulator_manager.py`) está en desarrollo.

## ✨ Funciones
- Menú principal con botones por consola: NES, Famicom, SNES, Game Boy, GBC, GBA y N64.
- Detecta automáticamente las ROMs de cada carpeta configurada y las ordena alfabéticamente.
- Navegación entre páginas con `QStackedWidget`.
- Estilos personalizados con QSS (como CSS, pero para Qt).
- Configuración separada en JSON.

## 🗂️ Estructura
```
main.py                  → ventana principal y navegación
core/rom_manager.py      → lee la configuración y lista las ROMs
core/emulator_manager.py → (en desarrollo) lanzar emuladores
config/consoles.json     → carpeta de ROMs por consola
styles/main.qss          → tema visual
```

## 🚀 Cómo correrlo
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```
Edita `config/consoles.json` con las rutas de tus carpetas.

## 🗺️ Próximos pasos
- [ ] Lanzar el emulador correspondiente (RetroArch, etc.) con doble clic.
- [ ] Portadas de los juegos.
- [ ] Soporte para control.

> ⚠️ Este proyecto **no incluye ni distribuye ROMs**. Usa solo copias de juegos que te pertenezcan.
