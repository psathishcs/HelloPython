'''
Created on Feb 10, 2017

@author: sparthasarathy
'''

if __name__ == '__main__':
    tup1 = (1, 2, 3, 5,6, 36, 36)
    tup2 = 'a', 'b', 'c', 'd', 'e'
    tup3 = ('physics', 'chemistry', 1997, 2000)
    tup4 = ()
    tup5 = (50,)
    print tup1
    print tup2
    print tup3
    print tup4
    print tup5
    print tup1[4]
    print tup2[1:4]
    tup2 = tup1 + tup2
    print tup2
    tup5 = tup5 * 5
    print tup5
    tup2 = tup2 * 3
    print tup2
    flag = 3 in tup2
    print flag
    flag = 3.0 in tup2
    print flag
    flag = 3.1 in tup2
    print flag
    for t in tup2:
        print t
    print len(tup2)
    print max(tup2)
    print min(tup2)
    List1 = [3453, 3632,7567, 'reena', 'Sangeetha']
    print List1
    tup6 = tuple(List1)
    print tup6
    