"""
Agente Organizador de Archivos con IA (Claude).
Escanea una carpeta, clasifica archivos con Claude y los organiza automáticamente.
"""
import os
import json
import shutil
from pathlib import Path

import anthropic


def escanear_carpeta(ruta_carpeta: str) -> list[str]:
    """
    Escanea una carpeta y retorna la lista de archivos (no carpetas).
    
    Args:
        ruta_carpeta: Ruta a la carpeta que se desea escanear.
    
    Returns:
        Lista con los nombres de los archivos encontrados.
    """
    carpeta = Path(ruta_carpeta)
    
    if not carpeta.exists():
        print(f"❌ Error: La carpeta '{ruta_carpeta}' no existe.")
        return []
    
    if not carpeta.is_dir():
        print(f"❌ Error: '{ruta_carpeta}' no es una carpeta.")
        return []
    
    # Listar solo archivos (no subcarpetas)
    archivos = [f.name for f in carpeta.iterdir() if f.is_file()]
    
    if not archivos:
        print(f"⚠️ La carpeta '{ruta_carpeta}' está vacía.")
        return []
    
    print(f"📂 Se encontraron {len(archivos)} archivos en '{ruta_carpeta}':")
    for archivo in sorted(archivos):
        print(f"   📄 {archivo}")
    
    return archivos


# --- Prueba rápida ---
if __name__ == "__main__":
    archivos = escanear_carpeta("desordenada")
    print(f"\nTotal: {len(archivos)} archivos")