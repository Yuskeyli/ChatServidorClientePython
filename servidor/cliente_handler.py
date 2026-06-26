"""
cliente_handler.py
------------------

Representa un cliente conectado al servidor.

Cada instancia de esta clase se ejecuta dentro de un hilo
independiente.

Responsabilidades

- Autenticar usuario.
- Procesar mensajes.
- Ejecutar comandos.
- Cerrar la conexión.
"""

import threading

from dao.usuario_dao import UsuarioDAO


class ClienteHandler(threading.Thread):

    def __init__(self, socket_cliente):

        super().__init__()

        self.socket = socket_cliente

        self.usuario = None

    def run(self):
        """
        Punto de entrada del hilo.

        Ejecuta el proceso completo de autenticación y luego
        mantiene la conversación con el cliente.
        """

        print("Cliente conectado.")