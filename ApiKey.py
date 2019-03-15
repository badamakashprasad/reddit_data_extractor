import sqlite3
import pickle


class ApiKey:
    def __init__(self, name):
        self.name = name
        using = [False] * (int(self.total_col()) + 1)
        self.using = using
        self.total = self.total_col()
        pass

    def total_col(self):
        conn = sqlite3.connect(str(self.name) + '.db')
        t = conn.execute("SELECT name FROM sqlite_master WHERE name = {}".format(repr(self.name)))
        if t.fetchone() is None:
            print(True)
            conn.execute(
                "CREATE table " + repr(self.name) + " (SR_NO INTEGER PRIMARY KEY AUTOINCREMENT,PUBLIC_KEY TEXT NOT "
                                                    "NULL,PRIVATE_KEY TEXT NOT NULL)")
        else:
            cur = conn.execute("SELECT COUNT(*) FROM {}".format(repr(self.name)))
            return cur.fetchone()[0]

    def putApiKey(self, publicKey, privateKey):
        conn = sqlite3.connect(str(self.name) + '.db')
        t = conn.execute("SELECT name FROM sqlite_master WHERE name = {}".format(repr(self.name)))
        if t.fetchone() is None:
            conn.execute(
                "CREATE table " + repr(self.name) + "(SR_NO INTEGER PRIMARY KEY AUTOINCREMENT,PUBLIC_KEY TEXT NOT "
                                                    "NULL,PRIVATE_KEY TEXT NOT NULL)")
            conn.execute(
                "INSERT INTO " + repr(self.name) + " (PUBLIC_KEY,PRIVATE_KEY) VALUES ({},{})".format(repr(publicKey),
                                                                                           repr(privateKey)))
        else:
            conn.execute(
                "INSERT INTO " + repr(self.name) + " (PUBLIC_KEY,PRIVATE_KEY) VALUES ({},{})".format(repr(publicKey),
                                                                                                     repr(privateKey)))
        conn.commit()
        conn.close()
        return True

    def getApikey(self, sr):
        conn = sqlite3.connect(str(self.name) + '.db')
        t = conn.execute("SELECT name FROM sqlite_master WHERE name = {}".format(repr(self.name)))
        if t.fetchone() is None or self.using is self.total:
            print(20 * '-' + ' No key stored or All keys in use ' + 20 * '-' + '/n DataBase name:' + str(self.name))
        else:
            cur = conn.cursor()
            if self.using[sr] is False:
                cur.execute("SELECT * FROM {} WHERE SR_NO = {}".format(repr(self.name),sr))
                row = cur.fetchone()
                print(self.using)
                self.using[sr] = True
                file = open('using_' + self.name, 'wb')
                pickle.dump(self.using, file)
                return row[1], row[2]
            else:
                while self.using[sr] is True:
                    sr = (sr + 1) % self.total
                cur.execute("SELECT * FROM {} WHERE SR_NO = {}".format(repr(self.name), sr))
                row = cur.fetchone()
                print(self.using)
                self.using[sr] = True
                print(self.using)
                file = open('using_' + self.name, 'wb')
                pickle.dump(self.using, file)
                return row[1], row[2]

    def closeApikey(self, sr):
        if sr <= -1:
            file = open('using_' + self.name, 'wb')
            using = [False]*(self.total_col() + 1)
            pickle.dump(using, file)
        else:
            file = open('using_' + self.name, 'wb')
            self.using[sr] = False
            pickle.dump(self.using, file)
        return True




o = ApiKey('reddit')
#o.putApiKey('fvvpnpautWtOjw','8kfhlBWC7kfb-oPV7olF9AMsXmw')
#o.putApiKey('Xmm_vdEyxElYAA','Xnsi_OfZJRtWr1qfhTrXegTK8w4')
#o.putApiKey('eVsX8DWj4ROI2g','2KeWSXUEpfKsYAlCt7KyDi1XjHA')
#o.putApiKey('IKTHloOciMmR8g','iIAZqQ1nkD4L60Ya08Vj-4OlWls')
