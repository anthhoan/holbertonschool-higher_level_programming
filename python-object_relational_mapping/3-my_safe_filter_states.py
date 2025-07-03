#!/usr/bin/python3
"""script that takes in arguments and displays all 
values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time, 
write one that is safe from MySQL injections!"""
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
                "WHERE name LIKE BINARY %s "
                "ORDER BY id ASC;",(state_searched,))
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    """main function"""
    states_user_inputs(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
