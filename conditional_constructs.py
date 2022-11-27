# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 14:05:31 2022

@author: Sachin Kansal
"""

import math
#%%browing problem  calculate cost of browsing
def browsing_cost(hrs=0,mins=0):
    cost=0
    if hrs<0:
        raise Exception('hours value must lie between 0 and 7')
    elif hrs<7 or (hrs==7 and mins==0):
        while hrs>0:
            if hrs >= 5:
                cost+=200
                hrs-=5
            elif hrs >= 1:
                cost+=50*hrs
                hrs=0
        if mins>=60 or mins<0:
            raise Exception('minutes values must lie between 0 and 60 ')
        else:
            cost+=mins
            return cost
    else:
        raise Exception('Browsing limit exceeded cost=300+')

#%% Scholarship eligibility
def is_eligibile(isfirstgraduate=False, Maths_score=0, Physics_score=0,Chemistry_score=0):
    if isfirstgraduate and (Maths_score+Physics_score+Chemistry_score)/3 >= 98:
        return 'Eligebile'
    else:
        return 'Not Eligebile'
#%%Odd or Even
def is_even(a=None):
    try:
        if a%2 == 0:
            print('iseven')
        else:
            print('odd')
    except:
        raise TypeError('invalid input or missing input')
#%% Leap Year
def is_LeapYear(year=None):
    try:
        if year%4 == 0:
            if year%100 != 0:
                print('leap')
            elif year%400 == 0 :
                print('leap')
            else:
                print('not leap')
        else:
            print('NOT leap')
    except:
        raise TypeError('invalid input or missing input' )
#%% roots of equaion Write a python  code in finding the roots of a quadratic equation?
def Quad_roots(a=0,b=0,c=0,d=0):
    c=c-d
    e=b**2-4*a*c
    if d >=0:
        r1=(-b+math.sqrt(e))//(2*a)
        r2=(-b-math.sqrt(e))//(2*a)
        return r1 , r2
    else:
        return 'complexvalue',
