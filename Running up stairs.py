
#100% solution for running up stairs problem

def model(n):
    out = [1,1]
    for i in range(2, n + 1):
        out.append(out[i - 1] + out[i - 2])

    return out[n]

n = int(input())

for i in range(n):
    l = int(input())
    print(model(l))
