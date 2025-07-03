#!/usr/bin/python3
"""Script that lists all states wit a name starting
with N from database hbtn_0e_0_usa"""
import MySQLdb
import sys


def filter_states(username, password, database):
    """script to connect to database and executes a SQL query"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
    "WHERE name LIKE BINARY 'N%' ORDER BY id ASC;")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    """main function"""
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
