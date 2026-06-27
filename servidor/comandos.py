"""
comandos.py

Procesa los comandos enviados por los clientes.
"""
from services.github_service import GithubService
from dao.repositorio_dao import RepositorioDAO
from dao.follower_dao import FollowerDAO
from datetime import datetime

from servidor.gestor_clientes import (
    usuarios_conectados,
    enviar_a_todos,
)


def ejecutar(comando, cliente):

    if comando == "/hora":
        cliente.enviar(
            "Hora del servidor: " +
            datetime.now().strftime("%H:%M:%S")
        )

        return

    if comando == "/usuarios":

        cliente.enviar(

            usuarios_conectados()

        )

        return

    if comando.startswith("/todos "):
        texto = comando[7:].strip()
        if not texto:
            cliente.enviar("Debe escribir un mensaje.")
            return

        enviar_a_todos(
            cliente.usuario,
            texto
        )
        return


    if comando.startswith("/repos "):

        usuario = comando[7:].strip()

        if not usuario:

            cliente.enviar(
                "Uso: /repos <usuario_github>"
            )

            return

        try:

            github = GithubService()

            repos = github.obtener_repositorios_objeto(usuario)

            cantidad = RepositorioDAO.guardar_todos(
                usuario,
                repos
            )
            print(
                f"[INFO] {cliente.usuario} consultó los repositorios de GitHub del usuario '{usuario}'."
            )

            mensaje = (
                "\n====================================\n"
                "CONSULTA GITHUB\n"
                "====================================\n\n"
                f"Usuario: {usuario}\n"
                f"Repositorios encontrados: {cantidad}\n\n"
                "Primeros repositorios:\n"
            )

            for repo in repos[:3]:
                mensaje += f"- {repo.nombre} ⭐ {repo.estrellas}\n"

            mensaje += "\nRepositorio(s) almacenado(s) correctamente en MySQL.\n"

            cliente.enviar(mensaje)


        except Exception as e:

            cliente.enviar(
                f"Error consultando GitHub: {e}"
            )

        return

    if comando.startswith("/followers "):

        usuario = comando[11:].strip()

        if not usuario:

            cliente.enviar(
                "Uso: /followers <usuario_github>"
            )

            return

        try:

            github = GithubService()

            followers = github.obtener_followers_objeto(usuario)
            cantidad = FollowerDAO.guardar_todos(
                usuario,
                followers
            )
            print(
                f"[INFO] {cliente.usuario} consultó los followers de GitHub del usuario '{usuario}'."
            )


            mensaje = (
                "\n====================================\n"
                "FOLLOWERS\n"
                "====================================\n\n"
                f"Usuario: {usuario}\n"
                f"Followers encontrados: {cantidad}\n\n"
                "Primeros followers:\n"
            )

            for follower in followers[:3]:
                mensaje += f"- {follower.login}\n"

            mensaje += "\nFollower(s) almacenado(s) correctamente en MySQL.\n"

            cliente.enviar(mensaje)

        except Exception as e:

            cliente.enviar(
                f"Error consultando GitHub: {e}"
            )

        return

    if comando == "/help":
        cliente.enviar("""

        ================ COMANDOS =================
        
        /hora
            Muestra la hora del servidor.
        
        /usuarios
            Lista los usuarios conectados.
        
        /todos <mensaje>
            Envía un mensaje a todos.
        
        /repos <usuario>
            Consulta los repositorios públicos de GitHub.
        
        /followers <usuario>
            Consulta los seguidores de GitHub.
        
        /adios
            Finaliza la conexión.
            
        /help
        Muestra esta ayuda.
    
        /adios
        Finaliza la conexión.
        
        ==========================================
        
        """)

        return


    if comando == "/adios":

        cliente.enviar(

            f"Hasta luego {cliente.usuario}"

        )

        cliente.socket.close()

        return

    cliente.enviar("Comando no reconocido.")