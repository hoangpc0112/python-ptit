def solve():
    n = input()

    while len(n) % 3 != 0:
        n = "0" + n

    tmp = ""
    res = ""

    for i in n[::-1]:
        tmp = i + tmp

        if len(tmp) == 3:
            res = str(int(tmp, 2)) + res
            tmp = ""

    print(res)


solve()
