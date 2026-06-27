"""
github_service.py
-----------------

Servicio encargado de consultar la API pública de GitHub.

No guarda información en la base de datos.
Su única responsabilidad es obtener datos desde GitHub.
"""

import requests

from modelo.repositorio import Repositorio
from modelo.follower import Follower


class GithubService:

    BASE_URL = "https://api.github.com/users"

    def obtener_repositorios(self, usuario):

        url = f"{self.BASE_URL}/{usuario}/repos"

        respuesta = requests.get(url)

        respuesta.raise_for_status()

        return respuesta.json()

    def obtener_followers(self, usuario):

        url = f"{self.BASE_URL}/{usuario}/followers"

        respuesta = requests.get(url)

        respuesta.raise_for_status()

        return respuesta.json()

    def obtener_repositorios_objeto(self, usuario):

        datos = self.obtener_repositorios(usuario)

        repos = []

        for repo in datos:

            repos.append(

                Repositorio(

                    nombre=repo["name"],
                    descripcion=repo["description"],
                    lenguaje=repo["language"],
                    estrellas=repo["stargazers_count"],
                    forks=repo["forks_count"],
                    url=repo["html_url"],
                    fecha_creacion=repo["created_at"]

                )

            )

        return repos

    def obtener_followers_objeto(self, usuario):

        datos = self.obtener_followers(usuario)

        followers = []

        for follower in datos:

            followers.append(

                Follower(

                    id=follower["id"],
                    login=follower["login"],
                    avatar_url=follower["avatar_url"],
                    url=follower["html_url"],
                    tipo=follower["type"]

                )

            )

        return followers