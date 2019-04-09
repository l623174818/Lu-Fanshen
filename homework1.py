'''
    Author:Lu Fanshen
    Function:Homework
    Version:1
    Date:
    Comments:
'''

import random
a = []
for _ in range(50):
    r = random.randint(1,100)
    a.append(r)
print('随机数列：' + str(a))
a.sort()
print('由小到大：' + str(a))
b = open(r'C:\Users\Administrator\Study\Python\homework6\homework1.txt','w')
for i in range(50):
    b.write(str(a[i]) + '\n')
b = open(r'C:\Users\Administrator\Study\Python\homework6\homework1.txt','r')
b.read()
a.sort(reverse = True)
print('由大到小：' + str (a))
b = open(r'C:\Users\Administrator\Study\Python\homework6\homework1.txt','a')
for i in range(50):
    b.write(str(a[i]) + '\n')
b = open(r'C:\Users\Administrator\Study\Python\homework6\homework1.txt','r')
b.read()