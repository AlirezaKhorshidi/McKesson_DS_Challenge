
class SQL(object):

    def __init__(self, sql_connection):
        self.conn = sql_connection
        self.c = self.conn.cursor()

    def create_users_table(self):
        self.c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

    def add_user_data(self, username, password):
        self.c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
        self.conn.commit()

    def login_user(self, username, password):
        self.c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
        data = self.c.fetchall()
        return data

    def view_all_users(self):
        self.c.execute("SELECT * FROM userstable")
        data = self.c.fetchall()
        return data
