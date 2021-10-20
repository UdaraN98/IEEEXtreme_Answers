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
    a,b,c = input().split()
    results.append(cal(int(a), int(b), int(c)))



for items in results:
    print(items)
