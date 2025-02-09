def solve():
    a, k, n = map(int, input().split())
    check = False
    start = (k - (a % k)) % k

    for i in range(start, n - a + 1, k):
        if i > 0:
            print(i, end=' ')
            check = True

    if not check:
        print(-1)


solve()
