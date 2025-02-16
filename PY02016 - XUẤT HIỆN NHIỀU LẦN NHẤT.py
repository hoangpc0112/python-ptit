def solve():
    n = int(input())
    a = list(map(int, input().split()))

    f_max = 0
    f = [0] * (10**6 + 5)

    for i in a:
        f[i] += 1
        f_max = max(f_max, f[i])

    if f_max <= n // 2:
        print('NO')
        return

    for i in range(1, 10**6 + 5):
        if f[i] == f_max:
            print(i)
            return


for i in range(int(input())):
    solve()
