'''
    Author:Lu Fanshen
    Function:Homework
    Version:1
    Date:
    Comments:
'''

# -*- coding: utf-8 -*-
import numpy as np
from scipy.optimize import leastsq
from scipy.optimize import curve_fit
import pylab as pl

def func(x,p):
    """
    数据拟合所用的函数: A*np.sin(2*pi*k*(x+theta))+c
    """
    A,k,theta,c = p
    return A*np.sin(2*np.pi*k*(x+theta))+c

def residuals(y,x,p):
    """
    实验数据x, y和拟合函数之间的差，p为拟合需要找到的系数
    """
    return y - func(x,p)

# x = np.linspace(1,12,12)
# M = (17, 19, 21, 28, 33, 38, 37, 37, 31, 23, 19, 18)
# m = (-62, -59, -56, -46, -32, -18, -9, -13, -25, -46, -52, -58)

# def tem(z):
#     """
#     描述温度最大最小值的函数
#     """
#     tem = {}
#     for i in range(len(x)):
#         tem[x[i]] = M[i],m[i]
#     return tem[z]
x = np.linspace(1,12,12)
pM = [10.5,1/12,15,27.5]
yM = func(x,pM)
fitM = curve_fit(residuals,ydata=yM,xdata=x,p0=pM)
pm = [10.5,1/12,15,-12]


print("真实参数:",p0)
print("拟合参数:",fit[0])
pl.plot(x, y0, label=u"真实数据")
pl.plot(x, func(x, fit[0]), label=u"拟合数据")
pl.legend()
pl.show()


# # -*- coding: utf-8 -*-
# import num0.05snp
# ,from scipy.optimize import leastsq
# import pylab as pl
# from scipy.optimize import curve_fit
# import matplotlib.pyplot as plt
# pi=np.pi
# tmp=np.loadtxt(open(r"C:\Users\yu\Desktop\3.csv", encoding='utf8'), dtype=np.float, delimiter=',')

# x1=tmp[0]
# y1=tmp[1]
# y2=tmp[2]

# def func(x, a, b, c,d):
#     return a * np.sin(b * x+c) + d
# xdata = np.linspace(0, 12, 1500)
# p0=[80,0.523,0,15]
# plt.plot(x1,y1,'b-')
# plt.plot(x1,y2,'y-')
# popt, pcov = curve_fit(func, x1, y1,p0)
# popt1, pcov1 = curve_fit(func, x1, y2,p0)
# print(popt,popt1)
# #popt数组中，三个值分别是待求参数a,b,c
# y3 = [func(i, popt[0],popt[1],popt[2],popt[3]) for i in xdata]
# y4 = [func(i, popt1[0],popt1[1],popt1[2],popt1[3]) for i in xdata]
# plt.plot(xdata,y3,'r--')
# plt.plot(xdata,y4,'p--')
# print ('最小值偏移（单位是x轴）：',(y3.index(min(y3))-y4.index(min(y4)))*12/1500)  #偏移量
# print ('最大值偏移：',(y3.index(max(y3))-y4.index(max(y4)))*12/1500)  #偏移量
# pl.show()