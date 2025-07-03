#!/usr/bin/python3
"""Script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def filter_cities(username, password, database, state_name):
    """Script to connect to database and run SQL query"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities "
                "INNER JOIN states "
                "ON cities.state_id = states.id "
                "WHERE states.name LIKE BINARY %s "
                "ORDER BY cities.id ASC;", (state_name,))
    result = cur.fetchall()
    for i, row in enumerate(result):
        print(row[0], end="")
        if i < len(result) - 1:
            print(", ", end="")
    print()
    cur.close()
    db.close()


if __name__ == "__main__":
    """Main function"""
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
