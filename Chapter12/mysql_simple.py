#!/usr/bin/python
__author__ = "Bassim Aly"
__EMAIL__ = "basim.alyy@gmail.com"

import MySQLdb

SQL_IP = "10.10.10.130"
SQL_USERNAME = "root"
SQL_PASSWORD = "EnterpriseAutomation"
SQL_DB = "TestingPython"

sql_connection = MySQLdb.connect(SQL_IP, SQL_USERNAME, SQL_PASSWORD, SQL_DB)
# print sql_connection

cursor = sql_connection.cursor()
cursor.execute("show tables")

output = cursor.fetchall()
print(output)
