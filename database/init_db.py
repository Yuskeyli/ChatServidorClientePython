"""
init_db.py
----------

Crea automáticamente la base de datos y las tablas
necesarias para el funcionamiento del sistema.
"""

from conexion import ConexionBD


def iniciar_bd():
    """
    Inicializa la estructura de la base de datos.

    Crea las tablas si todavía no existen.
    """

    print("Inicializando base de datos...")