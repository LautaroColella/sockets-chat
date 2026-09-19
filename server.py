import sqlite3

DB = "chat.db"


def db():
    try:
        with sqlite3.connect(DB) as conn:
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


def start():
    db_on = db()

    if db_on == False:
        print("Error durante la conexión a la base de datos")
        return

    print("Exito")


if __name__ == "__main__":
    start()
