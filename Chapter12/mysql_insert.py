#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import MySQLdb

SQL_IP = "10.10.10.130"
SQL_USERNAME = "root"
SQL_PASSWORD = "EnterpriseAutomation"
SQL_DB = "TestingPython"

sql_connection = MySQLdb.connect(SQL_IP, SQL_USERNAME, SQL_PASSWORD, SQL_DB)

employee1 = {
    "id": 1,
    "fname": "Bassim",
    "lname": "Aly",
    "Title": "NW_ENG"
}

employee2 = {
    "id": 2,
    "fname": "Ahmed",
    "lname": "Hany",
    "Title": "DEVELOPER"
}

employee3 = {
    "id": 3,
    "fname": "Sara",
    "lname": "Mosaad",
    "Title": "QA_ENG"
}

employee4 = {
    "id": 4,
    "fname": "Aly",
    "lname": "Mohamed",
    "Title": "PILOT"
}

employees = [employee1, employee2, employee3, employee4]

cursor = sql_connection.cursor()

for record in employees:
    SQL_COMMAND = """INSERT INTO TestTable(id,fname,lname,Title) VALUES ({0},'{1}','{2}','{3}')""".format(record['id'],
                                                                                                          record[
                                                                                                              'fname'],
                                                                                                          record[
                                                                                                              'lname'],
                                                                                                          record[
                                                                                                              'Title'])

    print SQL_COMMAND
    try:
        cursor.execute(SQL_COMMAND)
        sql_connection.commit()
    except:
        sql_connection.rollback()

sql_connection.close()
