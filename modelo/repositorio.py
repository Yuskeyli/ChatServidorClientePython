"""
repositorio.py
--------------

Representa un repositorio obtenido desde la API de GitHub.
"""

from dataclasses import dataclass


@dataclass
class Repositorio:
    nombre: str
    descripcion: str
    lenguaje: str
    estrellas: int
    forks: int
    url: str
    fecha_creacion: str