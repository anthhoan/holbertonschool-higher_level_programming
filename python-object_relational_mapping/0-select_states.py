#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


def get_all_states(username, password, database):
    """Script to run to list all state from the database"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC;")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    """main function"""
    get_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
