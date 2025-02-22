import mysql.connector  # pip install mysql-connector-python


class MySql:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="project_dan_dung"
        )
        self.cursor = self.conn.cursor()

    def select(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def call_proc(self, proc_name, args):
        try:
            self.cursor.callproc(proc_name, args)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

    def execute(self, query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False

    def execute2(self, query1, query2):
        try:
            self.cursor.execute(query1)
            last_id = self.cursor.lastrowid
        except Exception as e:
            print(e)
            self.conn.rollback()
            return False
        query2 = query2.format(last_id)
        self.cursor.execute(query2)
        self.conn.commit()
        return True

    def execute_without_commit(self, query):
        self.cursor.execute(query)
        return self.cursor.lastrowid

    def rollback(self):
        self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()
