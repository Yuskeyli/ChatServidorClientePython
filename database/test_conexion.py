from database.conexion import ConexionBD

try:
    conexion = ConexionBD.conectar()
    print("✅ Conexión exitosa")
    conexion.close()
except Exception as e:
    print("❌ Error:", e)