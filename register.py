import sqlite3


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('usersdata/users.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            name, telegram_id,games_total,cities_total,wins)""")
        self.conn.commit()

    def get_all_players(self):
        self.cursor.execute("""SELECT * FROM users""")
        return self.cursor.fetchall()


class Register:
    message = "Welcome back!"

    def __init__(self, name, telegram_id):
        self.telegram_id = telegram_id
        self.conn = sqlite3.connect('usersdata/users.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT * FROM users WHERE telegram_id = {telegram_id}""")
        if len(self.cursor.fetchall()) > 0:
            pass
        else:
            self.cursor.execute(f"""INSERT INTO users VALUES (NULL,?,?,0,0,0)""", (name, telegram_id,))
            self.conn.commit()
            self.message = f"Added new player! - {name}, {telegram_id}"

    def check_if_register(self):
        self.cursor.execute(f"""SELECT * FROM users WHERE telegram_id = {self.telegram_id}""")
        if len(self.cursor.fetchall()) > 0:
            return True
        else:
            return False


class Operate:
    pass
