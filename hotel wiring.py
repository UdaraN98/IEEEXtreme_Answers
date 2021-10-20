#100% solution for hotel wiring problem

import numpy as np

n = int(input())
#creating the array
for i in range(n):
    c_rooms = []
    tots = []
    tot = 0
    m,n,k = map(int, input().split())
    for j in range(m):
        c_rooms.append(int(input()))
#sorting em
    c_rooms = np.array(c_rooms)
    w_rooms = n - c_rooms

    c_rooms.sort()
    c_rooms = c_rooms[::-1]
    w_rooms.sort()
    w_rooms = w_rooms[::-1]
#taking the sum
    if m == k:
        tot= sum(w_rooms)
        print(tot)
    else:
        
        for i in range(m-k):
            tot += c_rooms[i]

        for i in range(k):
            tot += w_rooms[i]
            
        print(tot)
