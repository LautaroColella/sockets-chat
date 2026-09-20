import sqlite3
import socket
import sys
import datetime

DB_NAME = "chat.db"
HOST = "127.0.0.1"
PORT = 1337


def server():
    try:
        # https://docs.python.org/3/library/socket.html#socket.socket
        # "socket.AF_INET" se usa para ipv4, "AF_INET6" se usa para ipv6.
        # "socket.SOCK_STREAM" es el tipo de socket "STREAM" que equivale a una conexión TCP.
        sv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Se conecta el socket al host y puerto.
        sv.bind((HOST, PORT))

        sv.listen()
        return sv

    except Exception as err:
        print(f"Error en el inicio del servidor: {err}")
        return None


def db():
    try:
        # Se conecta a la DB y crea la tabla.
        with sqlite3.connect(DB_NAME) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS chat (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    contenido TEXT NOT NULL,
                    fecha_envio TEXT NOT NULL,
                    ip_cliente TEXT NOT NULL
                )
            """)
        return True

    except sqlite3.Error as err:
        print(f"Error en la base de datos: {err}")
        return False


if __name__ == "__main__":
    db_on = db()

    if db_on == False:
        print("Error durante la conexión a la base de datos")
        sys.exit()

    sv = server()
    if not sv:
        print("Error durante la inicialización del servidor")
        sys.exit()

    sv.settimeout(1)

    print(f"Servidor escuchando en el puerto {PORT}")
    try:
        while True:
            try:
                conn = sv.accept()
                client_conn = conn[0]
                client_info = conn[1]

            except socket.timeout:
                pass

            else:
                data = client_conn.recv(1024)

                if data:
                    message = data.decode("utf-8")  # send to db

                    ts = datetime.now().isoformat()
                    response = f"Mensaje recibido: {ts}"
                    client_conn.sendall(response.encode("utf-8"))

                client_conn.close()

    except KeyboardInterrupt:
        print("Servidor detenido manualmente")

    finally:
        sv.close()
        sys.exit()

    print("Exito")
