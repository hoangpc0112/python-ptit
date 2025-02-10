def solve():
    s = input() + "@"

    i = 0
    c = ''
    fre = 0
    res = ""

    while i < len(s):
        while s[i].isalpha():
            c = s[i]
            i += 1

        while s[i].isdigit():
            fre = fre * 10 + int(s[i])
            i += 1

        for j in range(fre):
            res += c

        if s[i] == '@':
            break

        fre = 0

    print(res)


for i in range(int(input())):
    solve()
