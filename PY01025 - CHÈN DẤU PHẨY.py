def solve():
    s = input()
    res = ""
    cnt = 0

    for i in range(len(s) - 1, -1, -1):
        res += s[i]
        cnt += 1

        if cnt == 3 and i != 0:
            res += ","
            cnt = 0

    print(res[::-1])


solve()
