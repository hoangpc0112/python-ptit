def solve():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    k = int(input())

    sum_upper, sum_lower = 0, 0

    for i in range(n):
        for j in range(n):
            if j > i:
                sum_upper += a[i][j]
            elif j < i:
                sum_lower += a[i][j]

    res = abs(sum_upper - sum_lower)

    print("YES" if res <= k else "NO")
    print(res)


solve()
