#100% fibonacci solution
#matrix exponention is used 
#after n =60 the pattern start to repeat. so devide n by 60

import numpy as np
def model(n):
    F = np.array([[1,1],[1,0]])
    if (n == 0):
        return 0
    k = np.linalg.matrix_power(F,(n%60))

    return int(k[0,0])%10



n = int(input())
ans =[]
for i in range(n):
    k = int(input())
    ans.append(model(k))
    
    
for items in ans:
    print(items)





