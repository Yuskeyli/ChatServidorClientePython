"""
follower_dao.py
---------------

Acceso a datos de los followers de GitHub.
"""

"""
follower_dao.py
---------------

Acceso a la tabla followers.
"""

from database.conexion import ConexionBD


class FollowerDAO:

    @staticmethod
    def guardar(usuario_consultado, follower):

        conexion = ConexionBD.conectar()

        cursor = conexion.cursor()

        sql = """
              INSERT IGNORE INTO followers
        (
            usuario_consultado,
            follower_id,
            login,
            avatar_url,
            url,
            tipo_cuenta
        )

        VALUES (%s,%s,%s,%s,%s,%s) \
              """

        cursor.execute(

            sql,

            (

                usuario_consultado,
                follower.id,
                follower.login,
                follower.avatar_url,
                follower.url,
                follower.tipo

            )

        )

        conexion.commit()

        cursor.close()

        conexion.close()

    @staticmethod
    def guardar_todos(usuario_consultado, followers):

        contador = 0

        for follower in followers:

            FollowerDAO.guardar(usuario_consultado, follower)

            contador += 1

        return contador