# Chat

Servidor y cliente de chat implementados en Python utilizando sockets TCP y SQLite.

## Requisitos

- Python 3
- SQLite3

## Ejecución

Iniciar el servidor:

```bash
python server.py
```

Iniciar el cliente:

```bash
python client.py
```

El cliente permite enviar múltiples mensajes y recibe la respuesta del servidor.

Para salir del cliente se debe escribir: "éxito"

## Base de datos

El servidor usa SQLite y guarda cada mensaje con los campos:

- `id`
- `contenido`
- `fecha_envio`
- `ip_cliente`

La base de datos y la tabla se crean automáticamente al iniciar el servidor.

## Comunicación

La comunicación entre cliente y servidor usa **TCP mediante sockets IPv4**.

El servidor responde a cada mensaje con:

```text
Mensaje recibido: <timestamp>
```
