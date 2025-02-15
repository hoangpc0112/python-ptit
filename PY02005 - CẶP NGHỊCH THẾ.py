def solve():
    n = int(input())
    a = list(map(int, input().split()))
    res = 0

    for i in range(n):
        for j in range(i + 1, n):
            if i < j and a[i] > a[j]:
                res += 1

    print(res)


solve()
