"""
main_servidor.py
-----------

Servidor principal del sistema.

Su responsabilidad es escuchar conexiones entrantes y
crear un hilo independiente para cada cliente conectado.

Gracias al uso de hilos múltiples, el servidor puede
atender varios clientes simultáneamente.Mantiene la lista de clientes conectados y acepta nuevas
conexiones de manera concurrente.
"""
import socket

from servidor.cliente_handler import ClienteHandler

HOST = "0.0.0.0"
PUERTO = 5000


def iniciar():

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    servidor.bind((HOST, PUERTO))

    servidor.listen()
    print("""
        ========================================
         CHAT SERVIDOR CLIENTE
         Programación Concurrente
         Python + MySQL + GitHub API
         Alumna: Yuskeyli Avila  
        ========================================
        """)

    print(f"Servidor escuchando en puerto {PUERTO}")

    while True:

        socket_cliente, direccion = servidor.accept()

        print(f"Cliente conectado {direccion}")

        hilo = ClienteHandler(socket_cliente)

        hilo.start()


if __name__ == "__main__":
    iniciar()