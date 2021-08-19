import sqlite3
import pandas as pd


def makeTableWithNameColumn(name, col):
    conn = sqlite3.connect(name+".db")
    c = conn.cursor()
    cols = ''
    for content in col:
        cols = cols + content + ", "
    c.execute("CREATE TABLE IF NOT EXISTS " + name + " (" + cols[0:-2] + ")")
    conn.commit()
    c.close()


def insertNameAndCode(name, data):
    conn = sqlite3.connect(name + ".db")
    c = conn.cursor()
    c.executemany("INSERT INTO " + name + " VALUES(?, ?)", data)
    print("insertNameAndCode Complete!")
    conn.commit()
    c.close()
