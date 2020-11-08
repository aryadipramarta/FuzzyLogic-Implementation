import matplotlib.pyplot as plt
import pandas as pd
import csv

#membacaFile
dfile = pd.read_excel("Mahasiswa.xls");


#Design Membership Function
def calc_high(value,x,y):
    high = (value - x / y - x)
    return high

def calc_low(value,x):
    low = (x - value / x - 1)
    return low

def calc_med_one(value,x,y):
    med_one = (value - 1/x - 1)
    return med_one

def calc_med_two(value,x,y):
    med_two = (y-value/y-x)
    return med_two

def func_High(value):
    if (value<=limit[]):
        return 0;
    elif(value>limit[]):
        return 1;
    elif(value > limit[] and value <= limit[]):
        calc_high(value,lim[],lim[]); 

def func_Low(value):
    if(value <= limit[]):
        return 1;
    elif(value > limit[]):
        return 0;
    elif(value <= limit[] and value > limit[]):
        calc_low(value,lim[],lim[])

def func_Med(value):
    if(value <= limit[])