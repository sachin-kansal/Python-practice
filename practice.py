def isPrime(num):
    if type(num) is int :
        count = 1
        for i in range(2,int(num)):
            if int(num) % i == 0:
                count=count+1
        if count ==1 and num not in [0,1]:
            return [int(num),1]
        else:
            return [num,0]
    else:
        return 0

def ireverse(s: list, i: int):
    if i == len(s)/2:
        return s
    else:
        k =s[i]
        s[i] = s[len(s)-1-i]
        s[len(s)-1-i] = k
        return ireverse(s,i+1)
    
def ispalindrome(s:str,i:int):
    if len(s)/2 <= i:
        return True
    elif s[i] != s[len(s)-i-1]:
        return False
    else:
        return ispalindrome(s,i+1)
        
def fibonaci(n:int): # n is index of fibonacci number
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaci(n-2)+fibonaci(n-1)


print(isPrime(5),isPrime(0),isPrime(1),isPrime(22),isPrime(6.5),isPrime(3.5),isPrime(2.5),sep="\n")

print(ireverse([1,2,80,4,5,6],2))
print(ispalindrome("asksa",0))
print(ispalindrome("abcd",0))
print(fibonaci(7))