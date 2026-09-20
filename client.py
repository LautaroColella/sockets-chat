import socket

HOST = "127.0.0.1"
PORT = 5000


def client():
    try:
        # https://docs.python.org/3/library/socket.html#socket.socket
        # "socket.AF_INET" se usa para ipv4, "AF_INET6" se usa para ipv6.
        # "socket.SOCK_STREAM" es el tipo de socket "STREAM" que equivale a una conexión TCP.
        client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client_conn.connect((HOST, PORT))

        print("Conectado")

        while True:
            message = input("Mensaje: ")

            if message.lower() == "éxito":
                break

            client_conn.sendall(message.encode("utf-8"))
            data = client_conn.recv(128)

            if not data:
                break

            print(data.decode("utf-8"))

        client_conn.close()

    except KeyboardInterrupt:
        print("Cliente detenido manualmente")

    except Exception as err:
        print(f"Error en el cliente: {err}")


if __name__ == "__main__":
    client()
