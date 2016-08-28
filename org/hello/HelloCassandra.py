'''
Created on Aug 28, 2016

@author: Sathish
'''
import sys
from cassandra.cluster import Cluster

if __name__ == '__main__':
    cluster = Cluster()
    session = cluster.connect('tp')
    resultSet = session.execute('SELECT * FROM emp')
    for row in resultSet:
        print(row.emp_id,row.emp_name,row.emp_email,row.emp_city,row.emp_phone,row.emp_sal)

