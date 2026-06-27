"""
conexion.py
------------

Responsabilidad
---------------
Administra la conexión con la base de datos MySQL.

Este módulo centraliza toda la configuración necesaria para
establecer conexiones con la base de datos, evitando repetir
código en el resto del proyecto.

Autor:
Yuske

Materia:
Programación sobre Redes
"""

import mysql.connector


class ConexionBD:
    """
    Clase encargada de crear conexiones con MySQL.
    """

    HOST = "localhost"
    PUERTO = 3306
    USUARIO = "root"
    PASSWORD = "Root2026!"
    BASE = "chat_socket"

    @staticmethod
    def conectar():
        """
        Crea y devuelve una conexión a MySQL.

        Returns
        -------
        mysql.connector.connection.MySQLConnection
            Conexión abierta a la base de datos.
        """

        return mysql.connector.connect(
            host=ConexionBD.HOST,
            port=ConexionBD.PUERTO,
            user=ConexionBD.USUARIO,
            password=ConexionBD.PASSWORD,
            database=ConexionBD.BASE
        )