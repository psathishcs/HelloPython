'''
Created on Feb 10, 2017

@author: sparthasarathy
'''

if __name__ == '__main__':
    List1 = ['Physics', 'chemistry', 2535, 351.345345]
    List2 = [1, 3, 2, 5, 4, 3, 35, 336]
    List3 = List1 + List2
    print List1
    print len(List1)
    print len(List1[1:])
    print len(List1[2:5])
    print List1 + List2
    print List1 * 4
    print 3 in List1
    print 3 in List2
    print (List1 + List2)[-2]
    print len((List1 + List2))
    print cmp(List1, List2)
    print cmp(List2, List2)
    print cmp(List2, List1)
    if cmp(List1, List2) == 0:
        print "Equal!"
    else:
        print "Not Equal!"
    print max(List2)
    print max(List1)
    List2.append(3542346)
    print List2
    print List2.count(3)
    List2.extend(List1)
    print List2
    print List2.index(2)
    List2.reverse()
    print List2
    List2.remove(3)
    print List2
    List2.sort()
    print List2
    List2.insert(5,6)
    print List2
        
