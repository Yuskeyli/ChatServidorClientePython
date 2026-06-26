"""
usuario_dao.py
--------------

Contiene las operaciones relacionadas con la tabla
usuarios.

Actualmente implementa la validación de credenciales
utilizadas por el servidor durante el proceso de login.
"""

from database.conexion import ConexionBD


class UsuarioDAO:

    @staticmethod
    def validar(usuario, password):
        """
        Verifica si un usuario existe en la base de datos.

        Parameters
        ----------
        usuario : str
            Nombre del usuario.

        password : str
            Contraseña.

        Returns
        -------
        bool
            True si las credenciales son válidas.
        """

        conexion = ConexionBD.conectar()

        cursor = conexion.cursor()

        cursor.execute(
            """
            SELECT *
            FROM usuarios
            WHERE usuario=%s
              AND password=%s
            """,
            (usuario, password)
        )

        resultado = cursor.fetchone()

        cursor.close()

        conexion.close()

        return resultado is not None