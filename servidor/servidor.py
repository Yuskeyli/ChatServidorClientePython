"""
servidor.py
-----------

Servidor principal del sistema.

Su responsabilidad es escuchar conexiones entrantes y
crear un hilo independiente para cada cliente conectado.

Gracias al uso de hilos múltiples, el servidor puede
atender varios clientes simultáneamente.
"""

import socket
import threading

from cliente_handler import ClienteHandler


HOST = "0.0.0.0"

PUERTO = 5000


def iniciar():

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor.bind((HOST, PUERTO))

    servidor.listen()

    print("Servidor iniciado...")

    while True:

        cliente, direccion = servidor.accept()

        print(f"Nueva conexión desde {direccion}")

        hilo = ClienteHandler(cliente)

        hilo.start()


if __name__ == "__main__":

    iniciar()