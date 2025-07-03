#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the 
states table of hbtn_0e_0_usa where name matches the argument."""
import MySQLdb
import sys


def states_user_inputs(username, password, database, state_searched):
    """Script to connect to database and executes a SQL query"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE '{0}' ORDER BY id ASC;".format(state_searched))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    """main function"""
    states_user_inputs(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
