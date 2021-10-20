#50% fibonacci solution

def model(n):
    out = [1,1]
    for i in range(2, n + 1):
        out.append(out[i - 1] + out[i - 2])

    return out[n]%10





n = int(input())
for i in range(n):
    k = int(input())
    ans = model(k)
    print(ans)
