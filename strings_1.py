# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 10:18:40 2022

@author: Sachin Kansal
"""

#Strings --> immutable

#%%

def lengthOfLongestSubstring(self, S: str) -> int:
    ls=[]
    for j in range(len(S)):
        i=j
        a=''
        while i<len(S):
            if  S[i] not in a:
                a=a+S[i]
                ls.append(len(a))
                i=i+1            
                #print(a,ls)
            else:
                break
        if ls!=[]:
            return max(ls)
        else:
            return len(S)
#%% longest palindromic substring
def is_palenndrom(S):
    if S==S[::-1]:
        return True
    else:
        return False
def longest(ls):
    l=len(ls[0])
    a=ls[0]
    for i in ls:
        if l<len(i):
            l=len(i)
            a=i
    return a
def longest_palindrom(S):
    ls=[]
    for i in range(len(S)):
        for j in range(i,len(S)):
            if is_palenndrom(S[i:j+1]):
                a=S[i:j+1]
                #b=len(S[i:j+1])
            else:
                continue
        ls.append(a)
            
    return longest(ls)
#%% alike strings
'''
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

 

Example 1:

Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.
Example 2:

Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
 

Constraints:

2 <= s.length <= 1000
s.length is even.
s consists of uppercase and lowercase letters
'''

def no_of_vowels(S):
    count=0
    vowels=['a','e','i','o','u']
    for i in S:
        if i.lower() in vowels:
            count+=1
    return count
def alike(S):
    a=S[:len(S)//2]
    b=S[len(S)//2:]
    if no_of_vowels(a)==no_of_vowels(b):
        return True
    else:
        return False

#%%

