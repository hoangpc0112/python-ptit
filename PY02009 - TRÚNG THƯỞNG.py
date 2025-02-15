def solve():
    n = int(input())
    f = [0] * 1005
    f_max = 0
    a = []

    for i in range(n):
        a += [int(input())]
        f[a[i]] += 1
        f_max = max(f_max, f[a[i]])

    for i in range(1, 1001):
        if f[i] == f_max:
            print(i)
            return


for i in range(int(input())):
    solve()
