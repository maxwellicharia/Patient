import sqlite3 as lite
import app


class Models:

    con = lite.connect('patient.db')

    with con:
        cur = con.cursor()
