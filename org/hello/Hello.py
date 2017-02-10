'''
Created on Feb 7, 2017

@author: sparthasarathy
'''
import sys

if __name__ == '__main__':
    print "Hello, World!"
    a = b = c = 1
    print a
    print b
    print c
    a, b, c = 20, 35, 'adam'
    print a, b,c 
    if 1:
        print 'true'
    else:
        print 'false'
    list = ['sbc', 35, 3636.35, "Sbv"]
    print list
    print list[3]
    list[3] = 'sbvv'
    
    print list[2:4]
    counter = 100
    miles = 1000.00
    firstName = 'Sathish Kumar '
    lastName = "Parthasarathy"
    print firstName + lastName
    print (firstName + lastName)[3:8] 
    print (firstName + lastName)[3:] 
    print (firstName + lastName)[3:8] * 3
    
    tuple = (5235, 534.3452, 'dfgwertweg')
    print tuple
    print tuple[1]
    
    a1 = int('35334')
    print a1 + 3345
    b1 = long('53665364337275424345346363456336236346203647458685868584337374733730343636236362626234626143263626262346262626336236262626262642626262262346236262362262626262632461262342423623423642362626262626362437')
    print b1 
    print b1 + a1
    
    print sys.maxint
    print sys.maxsize
    
    c1 = float('2363632624647209762762672807289620670267268767620670672868760366346362.346362637227172788580923467329676206267263894564576458956787699587367587343745736848737484784742883872428383488569605435838823458')
    print c1
    
    if (c1 < 2): 
        print "C1 is greater 2"
    else: 
        print "C2 is less that 2"
    count = 0
    while (count < 9):
        print count
        count = count + 1
    print "Bye bye.....!"
    var = 10
    while var <> 1:
        var = int(raw_input("Enter a number(1) : "))
        print "you entered: ", var
    else: print "Ended loop"
    
    fruits =['banana', 'apple', 'mango']
    for fruit in fruits:
        print fruit
        
        
    for letter in 'PYTHON':
        print letter
    
    for x in range(10,20):
        for y in range(1,x):
            print x * y
            
    x = 0
    while x <= 10:
        y = 0
        while y <= 10:
            print "X: " , x, "Y: ", y
            y = y + 1
        x = x + 1
    