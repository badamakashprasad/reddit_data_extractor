import praw
import datetime
import sqlite3


class display_data:
    def __init__(self):
        pass

    def connect_db(self,name):
        conn = sqlite3.connect(name)
        return conn

    def close_db(self,conn):
        conn.close()
        return True

    def get_subreddit_type(self,conn):
        ls = []
        csr = conn.execute("SELECT name FROM sqlite_master WHERE type = 'table'")
        for row in csr:
            if row[0] != "sqlite_sequence":
                ls.append(row[0])
        return ls

    def get_subreddit_list(self,conn,table_name,date=None):
        ls = []
        if date is not None:
            csr = conn.execute("SELECT * FROM {} WHERE DATE = {}".format(repr(table_name),str(date)))
            for row in csr:
                ls.append(row[1])
                return ls
        else:
            csr = conn.execute("SELECT * FROM {}".format(repr(table_name)))
            for row in csr:
                ls.append(row[1])
            return ls






