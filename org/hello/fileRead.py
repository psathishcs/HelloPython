'''
Created on Feb 8, 2017

@author: sparthasarathy
'''

if __name__ == '__main__':
    file = open("HelloOracleDatabase.py", 'r')
    print file.read()
    with open("HelloOracleDatabase.py", 'r') as lines:
        array = []
        for line in lines:
            array.append(line)
        print array