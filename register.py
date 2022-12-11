import sqlite3


class Database:
    def __init__(self, name, telegram_id):
        conn = sqlite3.connect('usersdata/users.db', check_same_thread=False)
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER UNIQUE NOT NULL AUTOINCREMENT,
                                                            name, telegram_id,games_total,cities_total,wins)""")


class Register:
    def __init__(self, name, telegram_id):
        self.telegram_id = telegram_id
        self.conn = sqlite3.connect('users.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""SELECT * FROM users WHERE telegram_id = {telegram_id}""")
        if len(self.cursor.fetchall()) > 0:
            pass
        else:
            self.cursor.execute(f"""INSERT INTO users VALUES (NULL,{name},{telegram_id},0,0,0)""")
            self.conn.commit()

    def check_if_register(self):
        self.cursor.execute(f"""SELECT * FROM users WHERE telegram_id = {self.telegram_id}""")
        if len(self.cursor.fetchall()) > 0:
            return True
        else:
            return False


class Operate:
    pass
