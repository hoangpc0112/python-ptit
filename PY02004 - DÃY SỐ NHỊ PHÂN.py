def solve():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0

    for i in range(n - 1):
        if a[i] != a[i + 1]:
            res += 1

    print(res)


solve()
