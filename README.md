# Chat Servidor - Cliente en Python

## Programación Concurrente

Trabajo práctico desarrollado en Python que implementa un sistema de chat Cliente-Servidor utilizando sockets TCP, hilos (threading), MySQL y la API pública de GitHub.

---

# Objetivos

Desarrollar una aplicación cliente-servidor que permita:

- Comunicación entre múltiples clientes.
- Autenticación de usuarios.
- Procesamiento de comandos.
- Persistencia de información en MySQL.
- Consumo de una API REST (GitHub).

---

# Tecnologías utilizadas

- Python 3.14
- Socket TCP
- Threading
- MySQL
- mysql-connector-python
- Requests
- Git
- GitHub

---

# Arquitectura del proyecto

```
ChatServidorClientePython/

cliente/
    cliente.py

servidor/
    main_servidor.py
    cliente_handler.py
    comandos.py
    gestor_clientes.py

services/
    github_service.py

dao/
    usuario_dao.py
    repositorio_dao.py
    follower_dao.py

modelo/
    repositorio.py
    follower.py

database/
    conexion.py

requirements.txt
README.md
```

---

# Funcionalidades implementadas

## Fase 1

- Comunicación Cliente - Servidor mediante sockets TCP.

## Fase 2

- Soporte para múltiples clientes utilizando hilos (threading).

## Fase 3

- Chat bidireccional.

## Fase 4

Comandos implementados:

| Comando | Descripción |
|----------|-------------|
| /hora | Devuelve la hora del servidor |
| /usuarios | Lista los usuarios conectados |
| /todos mensaje | Envía un mensaje a todos los clientes |
| /help | Muestra los comandos disponibles |
| /adios | Finaliza la conexión |

## Fase 5

Integración con la API pública de GitHub.

Comandos:

| Comando | Descripción |
|----------|-------------|
| /repos usuario | Consulta los repositorios públicos del usuario y los almacena en MySQL |
| /followers usuario | Consulta los seguidores del usuario y los almacena en MySQL |

## Fase 6

Persistencia de datos utilizando MySQL mediante el patrón DAO.

Se almacenan:

### Repositorios

- Usuario consultado
- Nombre
- Descripción
- Lenguaje
- Estrellas
- Forks
- URL
- Fecha de creación

### Followers

- Usuario consultado
- Login
- ID
- Avatar
- URL
- Tipo de cuenta

---

# Base de datos

El proyecto utiliza MySQL.

Debe existir una base de datos llamada:

```
chat_concurrente
```

Tablas:

- usuarios
- repositorios
- followers

---

# Instalación

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Configurar la conexión en:

```
database/conexion.py
```

---

# Ejecución

## Iniciar el servidor

```bash
python -m servidor.main_servidor
```

## Iniciar un cliente

```bash
python cliente/cliente.py
```

Se pueden ejecutar múltiples clientes simultáneamente.

---

# Ejemplo de uso

```
Usuario:
juan

Contraseña:
1234

Bienvenido juan

/hora

/usuarios

/todos Hola a todos

/repos torvalds

/followers torvalds

/help

/adios
```

---

# Concurrencia

Cada cliente conectado es atendido mediante un hilo independiente (`threading.Thread`), permitiendo que múltiples usuarios interactúen simultáneamente con el servidor.

---

# Autor

Yuske

Analista de Control de Calidad

Trabajo práctico desarrollado para la materia Programación Sobre Redes.