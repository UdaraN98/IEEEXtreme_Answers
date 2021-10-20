#40 points math problem solution
import math
import os

def cal(a,b,c):
    m = 1000000007
    k = b-c
    power = math.comb(b,c)

    answer = pow(a,power,m)
    
    return answer





n = int(input())
results =[]
for i in range(n):
    a,b,c = map(int,input().split())
    results.append(cal(a,b,c))



for items in results:
    print(items)
