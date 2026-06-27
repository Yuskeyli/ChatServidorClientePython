"""
gestor_clientes.py

Administra la lista de clientes conectados al servidor.
"""

clientes = []


def agregar(cliente):
    clientes.append(cliente)
    print(f"DEBUG -> Clientes conectados: {len(clientes)}")


def eliminar(cliente):
    """Elimina un cliente."""
    if cliente in clientes:
        clientes.remove(cliente)


def listar():
    """Devuelve la lista de clientes."""
    return clientes


def usuarios_conectados():

    print(clientes)

    texto = "\n===== USUARIOS =====\n"

    for i, cliente in enumerate(clientes, start=1):
        texto += f"{i}. {cliente.usuario}\n"

    return texto


def enviar_a_todos(remitente, mensaje):

    for cliente in clientes:
        cliente.enviar(f"[{remitente}] {mensaje}")