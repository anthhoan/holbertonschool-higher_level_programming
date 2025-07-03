#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


def all_cities(username, password, database):
    """Script to connect to database and run SQL query"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities "
                "INNER JOIN states "
                "ON cities.state_id = states.id "
                "ORDER BY cities.id ASC;")
    result = cur.fetchall()
    for row in result:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    """Main function"""
    all_cities(sys.argv[1], sys.argv[2], sys.argv[3])
