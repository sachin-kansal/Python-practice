from collections import deque
from typing import List
def averageWaitingTime(customers: list[list[int]]) -> float:
        arr= 0 #customer Arrive
        start=0 #chef start
        prep=0 #time taken by chef
        tot=0 #total time
        wait=0 #cust wait for 
        sum=0 #total sum of wait time for avg
        for i in customers:
            arr=i[0]
            prep=i[1]
            if tot <arr: #if somecust arrives late 
                start=arr
            else: #if cust is waitting for chef
                start=tot
            tot = start+prep
            wait=tot-arr 
            sum=sum+wait
            print(arr,prep,start,tot,wait,sum)
        return  round(sum/len(customers),5) #avg rounded to Y.XXXXX
#print(averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
#print(averageWaitingTime([[1,2],[2,5],[4,3]]))

def minOperations(logs: List[str]) -> int:
    c=0
    for i in logs:
        if i == "../" and c==0:
            c=0
        elif i=="../" and c!=0:
            c=c-1
        elif i=="./":
            c=c
        else:
            c=c+1
    return c

def reverseParentheses(s: str):
    index =[]
    r=[]
    for i in range(len(s)):
        if s[i]=="(":
            index.append(len(r))
        #    print(index)
        elif s[i]==")":
            start = index.pop()
            r[start:] =r[start:][::-1]
            #print(r, start)
        else:
            r.append(s[i])
        #print(r)
    return "".join(r)

def maximumGain(s: str, x, y):
    s = [j for j in s]
    print(s)
    i=0
    g=0
    if x>y:
        g,s=finder(s,x,["a","b"])
        g=g+finder(s,y,["b","a"])[0]
        
    else:
        g,s=finder(s,y,["b","a"])
        g=g+finder(s,x,["a","b"])[0]
    #cleanup

    return g
    
def finder(s,x,v):
    i=0
    g=0
    while i <= len(s) :
        if s[i:i+2] == v:
            s=s[:i]+s[i+2:]
            g=g+x
            i=i-2
        i=i+1
    return g,s


def robotclass( positions, healths, directions):
    dic = {positions[i]:[healths[i],directions[i]] for i in range(len(positions))}
    sl = sorted(dic)
    for i in sl:
        print(dic[i][1])

robotclass([3,5,2,6],[10,10,15,12],"RLRL")
#reverseParentheses("(ed(et(oc))el)")
#print(maximumGain("cdbcbbaaabab",4,5))
#print(maximumGain("aabbaaxybbaabb",4,5))