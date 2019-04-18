'''
    Author:Lu Fanshen
    Function:Homework
    Version:1
    Date:
    Comments:
'''

import numpy as np
import matplotlib.pyplot as plt

#打开csv文件提取数据
_ = dict(
    fname = '三5.csv',
    encoding = 'utf-8',
    dtype = 'str',
    delimiter = ',',
    usecols = range(0,-1),
    unpack = True
)
s5 = np.loadtxt(**_)
print(s5)

#提取某个学生的信息
i = input('请输入学生学号：')
student = {s5[0][0]:s5[0][i],s5[3][0]:s5[3][i]}
for j in range(5,20):
    student[s5[j][0]] = s5[j][i]
print(student)

#绘制图表
x = student.keys()
print(x)
y = student.values()
print(y)
plt.plot(x,y)
plt.show()
