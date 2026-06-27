"""
repositorio_dao.py
------------------

Acceso a la tabla repositorios.
"""

from database.conexion import ConexionBD


class RepositorioDAO:

    @staticmethod
    def guardar(usuario, repo):

        conexion = ConexionBD.conectar()

        cursor = conexion.cursor()

        sql = """
              INSERT IGNORE INTO repositorios
        (
            usuario,
            nombre_repo,
            descripcion,
            lenguaje,
            estrellas,
            forks,
            url,
            fecha_creacion
        )

        VALUES (%s,%s,%s,%s,%s,%s,%s,%s) \
              """

        cursor.execute(

            sql,

            (

                usuario,
                repo.nombre,
                repo.descripcion,
                repo.lenguaje,
                repo.estrellas,
                repo.forks,
                repo.url,
                repo.fecha_creacion.replace("T", " ").replace("Z", "")

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    @staticmethod
    def guardar_todos(usuario, repositorios):

        contador = 0

        for repo in repositorios:

            RepositorioDAO.guardar(usuario, repo)

            contador += 1

        return contador