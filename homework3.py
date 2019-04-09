'''
    Author:Lu Fanshen
    Function:Homework
    Version:1
    Date:
    Comments:
'''

import csv
with open('aapl.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    a = []
    for line in reader:        
        a.append(line[5])
    del a[0]
    a = list(map(int,a))
    print(a)
    def ave(a):
        sum = 0
        for i in a:
            sum += i
        return sum/len(a)
    print(ave(a))