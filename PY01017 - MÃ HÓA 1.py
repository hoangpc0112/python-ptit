def solve():
    s = input() + "@"

    fre = 1
    res = ""

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            fre += 1
        else:
            res += str(fre) + s[i]
            fre = 1

    print(res)


t = int(input())
for i in range(t):
    solve()
