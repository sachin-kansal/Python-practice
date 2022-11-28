# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 10:02:49 2022

@author: Sachin Kansal
"""

#list based Quesions
#%% 
'''
1.	Given two keys K1 & K2 as input , print all the elements between them in List. Where k1<=x<=k2 (x is the elements to be printed as output).
Example:
	(1,2,3,4,5,6,7,8,9,10) is the List
	If k1=4 and k2=9
	Output=4,5,6,7,8,9
'''
#based on value
def elem_between_value(input_list,Key1,Key2):
    return [x  for x in input_list if  x>=Key1 and x<=Key2]

# based on index where k1 and k2 are considered index
def elem_between_index(input_list,Key1,Key2):
    for i in range(len(input_list)):
        if input_list[i]==Key1:
            i1=i
        elif input_list[i]==Key2:
            i2=i+1
        else:
            continue
    return input_list[i1:i2]
            
#using in built
def elem_between_inbuilt(input_list,Key1,Key2):
    if Key1 in input_list and Key2 in input_list:
        return input_list[input_list.index(Key1):input_list.index(Key2)+1]  #list.index(elem) raises Value error if elem no in list
    else:
        raise ValueError ('Keys are not in the list')

#%%
'''
2.	In an Asian game athletic event, athletes have lined up in the ground. Each athlete is given a three digit chest number. Given a chest number ‘X’, find whether the athlete is in the lineup or not. If he is in the lineup print his position in the lineup else print 0. 
'''
def athelete_lineup(line,chest_number): 
    if chest_number in line:
        print(line.index(chest_number)+1)
    else:
        print(0)
#%%
'''
3.	You are given an array containing ‘n’ integers. You are asked to determine if the list contains two numbers that sum to some arbitrary integer, ‘k’. If such ‘k’ exists print those two numbers which sums to ‘k’ else print 0.
For example, if the list is 8, 4, 1 and 6 and k = 10, the answer is 4 6, because 4+6 = 10.
'''
def is_n1sumn2_K(lst,k):
    values=[]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i!=j and lst[i]+lst[j]==k:
                values.append((lst[i],lst[j]))
    if values == []:
        return 0
    else:
        return values
# list comprehension
def is_n1sumn2_K_list_comprehension(lst1,k):
    return [(a,k-a) for a in lst1 if k-a in lst1]  
                
#%%
'''
4.	Given a list ‘X’ as an input. Write a program that will print all the leaders in the list. An element is leader if it is greater than all the elements to its right side. And the rightmost element is always a leader. 
	For example: 
	X=   (6, 7, 4, 3, 5, 2)
	Output:    leaders are 7, 5 and 2.
'''
def leaders(X):
    Leader=[]
    for i in range(len(X)):
        c=1
        for j in range(i+1,len(X)):
            if X[i]<= X[j]:
                c=0
        if c==1:
            Leader.append(X[i])
    return Leader

def leader_comprehension(X):
    ls = [X[i] for i in range(len(X)-1) if (X[i] not in X[i+1:] and X[i]>=max(X[i+1:]))]
    ls.append(X[-1])
    return ls

#%%
'''
5.	You are given a list, write a program to print the next immediate greater element for each element. Elements for which no greater element exist, print next greater element as -1.
For any list, rightmost element always has next greater element as -1.
eg. For array [4, 15, 2, 9, 20, 11, 13] greater elements are as follows –
4 –> 15
15 –> 20
2 –> 9
20 –> -1
11 –> 13
13 –> -1
'''
def next_greater_integer(X):
    ls=[]
    for i in range(len(X)):
        for j in range(i,len(X)):
            if X[j]>X[i]:
                ls.append(X[j])
                break
            elif j==len(X)-1:
                ls.append(-1) 
                break
            else:
                continue
    return(ls)
#%%
'''6.	Given N integers, count the number of pairs of integers whose product is K. Your program should list out the pairs whose product is k along with number of such pairs. Also print “0” if no such k.
'''

def is_prod_k(lst,k):
    val = [(a,k/a) for a in lst if (k/a in lst and a!=0) ]
    if val==[]:
        return 0
    else:
        return len(val)//2