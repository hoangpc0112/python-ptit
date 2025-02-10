def solve():
    n, x, m = list(map(float, input().split()))
    res = 0

    while n < m:
        res += 1
        n += n * x / 100

    print(res)


for i in range(int(input())):
    solve()
