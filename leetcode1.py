from typing import List


def mergeAlternately( word1: str, word2: str) -> str:
    s= ''
    w1l = len(word1)
    w2l = len(word2)
    if w1l<=w2l:
        for i in range(w1l):
            s=s+word1[i]+word2[i]
            k= word2[i+1:]
        s= s+k
    else:
        for i in range(w2l):
            s=s+word1[i]+word2[i]
            k= word1[i+1:]
        s= s+k
    print(s)

def findTheDifference( s: str, t: str) -> str:
        d={i:t.count(i) for i in t}
        e = {i:s.count(i) for i in t}
        for i in d.keys():
             if d[i] != e[i]:
                  print(i)

  
def strStr(haystack: str, needle: str) -> int:
        out = -1
        k=len(needle)
        for i in range(0,len(haystack)-len(needle)+1):
            m= haystack[i:k]
            if m == needle:
                 return i
            else:
                 k=k+1
        return out    

def isanagram(a,b):
    if len(a)==len(b):
        for i in b:
            if b.count(i) != a.count(i):              
                 return False
        return True
    return False

def passThePillow( n: int, time: int) -> int:
    flag =0
    c=1
    for i in range(time):
        if flag ==0:
            c=c+1
        if flag ==1:
            c=c-1
        if c==n:
            flag = 1
        if c==1:
            flag = 0
    return c
        
def threeConsecutiveOdds(arr: List[int]) -> bool:
    def isodd(a):
        if a%2 == 1:
            return True
    i=0
    while i <= len(arr)-1-2:
        print(arr[i])
        if isodd(arr[i]) and isodd(arr[i+1]) and isodd(arr[i+2]):
            return True
        i=i+1
    return False

def plusOne(digits: List[int]) -> List[int]:
    if digits[-1] < 9:
        digits[-1] = digits[-1] + 1
        return digits
    else:
        i=-1
        while (digits[i]==9 and i>=(-1*len(digits))+1):
            digits[i]=0
            i=i-1
        else:
            digits[i] = digits[i]+1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0,1)
        return digits    


def findTheWinner(n: int, k: int) -> int:
        l = [i for i in range(1,n+1)]
        ci=-1 # first friend
        while len(l)!=1: #until only 1 person left
            for i in range(1,k+1):
                ci=ci+1 #count+1
                if ci >= len(l): #reset to zero
                    ci =0
            del l[ci] # remove kth friend
            ci=ci-1 # index -1 as element is deleted
        return l[0]

def moveZeroes(nums: List[int]) -> None:
    for j in nums:
        for i in range(len(nums)-1):
            if nums[i]==0 and nums[i+1]!=0:
                nums[i],nums[i+1] = nums[i+1],nums[i]
    print(nums)
 
print(findTheWinner(6,5))  #1
print("-"*55)
print(findTheWinner(5,2))
print("-"*55)
print(findTheWinner(3,1))
# print(passThePillow(4,5))
# a = [1,1,1,5,4,3,5]
# print(a[2:])
# print(a.remove(1))
# a=set([1,2,2,1])
# b = set([2,2])
# print(a.intersection(b))

# print(plusOne([1,2,3]))
# print(plusOne([9,9,9]))
# print(plusOne([5,8,9,9]))
# print(plusOne([1,0,1]))


