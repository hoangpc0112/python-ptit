def solve():
    p = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

    while True:
        str = input()

        if str == '0':
            break

        k, s = str.split()
        k = int(k)

        for i in range(len(s) - 1, -1, -1):
            print(p[(p.index(s[i]) + k) % 28], end='')

        print()


solve()
