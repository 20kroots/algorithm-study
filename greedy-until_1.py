# n = 25
# k = 3
n, k = map(int, input().split())

result = 0

while True:
    target = (n // k) * k
    print("n",n)
    print("target",target)
    result += (n - target)
    n = target
    if n < k:
        break
    result += 1
    print("result",result)
    n //= k

result += (n - 1)
print (result)