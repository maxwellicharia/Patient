import sqlite3 as lite
import app


class Models:

    con = lite.connect('patient.db')

    with con:
        cur = con.cursor()
        cur.execute("CREATE IF NOT EXISTS TABLE Patient(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO PATIENT(VALUES(?, ?)")
