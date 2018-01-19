import sqlite3 as lite
import app


class Models:

    con = lite.connect('patient.db')

    with con:
        cur = con.cursor()
        cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
