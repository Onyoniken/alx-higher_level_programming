#!/usr/bin/pyton3

"""
scripts lists from the database all states starting with letter "N"
"""
import MySQLdb as db
from sys import argv

"""
gets states from database
"""
if __name__ == '__main__':
    db_connet = db.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3])

    db_cursor = db.connect.cursor()

    db_cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' \ ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

