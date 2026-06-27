"""
cliente_handler.py
------------------

Representa un cliente conectado al servidor.

Cada cliente es atendido en un hilo independiente, lo que
permite que varios usuarios utilicen el chat de forma
simultánea.

Responsabilidades
-----------------
- Autenticar usuarios.
- Procesar mensajes recibidos.
- Ejecutar comandos del sistema.
- Administrar la conexión del cliente.
"""

import threading

from dao.usuario_dao import UsuarioDAO
from servidor.gestor_clientes import agregar, eliminar


class ClienteHandler(threading.Thread):
    """
    Gestiona la comunicación con un cliente conectado.

    Cada instancia de esta clase se ejecuta en un hilo
    independiente.
    """

    def __init__(self, socket_cliente):
        """
        Inicializa el hilo asociado al cliente.
        """
        super().__init__()

        self.socket = socket_cliente
        self.usuario = ""

    def enviar(self, mensaje: str):
        """
        Envía un mensaje al cliente.

        Si el cliente ya cerró la conexión, el error se
        ignora para evitar detener el servidor.
        """
        try:
            self.socket.send((mensaje + "\n").encode())
        except OSError:
            pass

    def recibir(self):
        """
        Espera y devuelve un mensaje enviado por el cliente.
        """
        return self.socket.recv(1024).decode().strip()

    def run(self):
        """
        Ejecuta el ciclo de vida completo del cliente.

        1. Solicita usuario y contraseña.
        2. Valida las credenciales en MySQL.
        3. Registra al usuario como conectado.
        4. Procesa mensajes y comandos.
        5. Libera los recursos al finalizar.
        """

        try:

            self.enviar("Usuario:")
            usuario = self.recibir()

            self.enviar("Contraseña:")
            password = self.recibir()

            if not UsuarioDAO.validar(usuario, password):
                self.enviar("ERROR: Usuario o contraseña incorrectos.")
                return

            self.usuario = usuario

            agregar(self)

            print(
                f"[{threading.current_thread().name}] "
                f"Usuario conectado: {usuario}"
            )

            self.enviar(f"Bienvenido {usuario}")

            while True:

                mensaje = self.recibir()

                if not mensaje:
                    break

                if mensaje.startswith("/"):

                    from servidor.comandos import ejecutar

                    ejecutar(mensaje, self)

                else:

                    print(
                        f"[{threading.current_thread().name}] "
                        f"{self.usuario}: {mensaje}"
                    )

                    self.enviar(
                        f"Servidor recibió: {mensaje}"
                    )

        except Exception as e:

            print(
                f"[{threading.current_thread().name}] "
                f"Error con el cliente {self.usuario}: {e}"
            )

        finally:

            eliminar(self)

            try:
                self.socket.close()
            except OSError:
                pass

            print(
                f"[{threading.current_thread().name}] "
                f"Usuario desconectado: {self.usuario}"
            )