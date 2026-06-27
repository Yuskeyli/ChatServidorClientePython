"""
cliente.py
----------

Cliente TCP del sistema de chat.

Responsabilidades
-----------------
- Establecer conexión con el servidor.
- Autenticarse mediante usuario y contraseña.
- Enviar mensajes al servidor.
- Recibir mensajes del servidor de forma concurrente.

Autor:
Yuske
"""

import socket
import threading


class Cliente:
    """
    Representa un cliente conectado al servidor de chat.
    """

    def __init__(self, host: str = "localhost", puerto: int = 5000):
        """
        Inicializa el cliente.

        Parameters
        ----------
        host : str
            Dirección IP o nombre del servidor.

        puerto : int
            Puerto del servidor.
        """

        self.host = host
        self.puerto = puerto

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        """
        Conecta el cliente con el servidor.
        """

        self.socket.connect((self.host, self.puerto))

        print("Conectado al servidor.")

        threading.Thread(
            target=self.recibir,
            daemon=True
        ).start()

        self.enviar()

    def recibir(self):
        """
        Escucha continuamente mensajes enviados por el servidor.
        """

        while True:

            try:

                mensaje = self.socket.recv(1024).decode()

                if not mensaje:
                    break

                print(mensaje)

            except:

                break

    def enviar(self):
        """
        Lee mensajes desde el teclado y los envía al servidor.
        """

        while True:

            mensaje = input()

            self.socket.send((mensaje + "\n").encode())


if __name__ == "__main__":

    Cliente().conectar()