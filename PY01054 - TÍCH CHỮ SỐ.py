def solve():
    s = input()
    res = 1

    for i in s:
        if i != '0':
            res *= int(i)

    print(res)


for i in range(int(input())):
    solve()
