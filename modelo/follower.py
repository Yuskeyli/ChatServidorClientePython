"""
follower.py
-----------

Representa un follower obtenido desde la API de GitHub.
"""

from dataclasses import dataclass


@dataclass
class Follower:
    id: int
    login: str
    avatar_url: str
    url: str
    tipo: str