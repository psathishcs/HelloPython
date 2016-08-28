#!/usr/bin/python

import sys
import cx_Oracle

def printf(format, *args):
    sys.stdout.write(format % args)

def printException(exception) :
    error, = exception.args
    printf("Error code = %s\n", error.code)
    printf("Error message = %s\n", error.message)
    
username = 'scott'
password = 'tiger'
databaseName = 'localhost:1521/orcl'

try :
    connection = cx_Oracle.connect(username, password,  databaseName)
    cursor = connection.cursor()
except  cx_Oracle.DatabaseError, exception:
      printf ('Failed to connect to %s\n',databaseName)
      printException (exception)
      exit (1)

sql = 'SELECT * FROM emp'
try :
    cursor.execute(sql)
except  cx_Oracle.DatabaseError, exception:
      printf ('Failed to execute Select statement to %s\n',sql)
      printException (exception)
      exit (1)
      
result = cursor.fetchall()
for row in result:
    printf("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n",row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])
