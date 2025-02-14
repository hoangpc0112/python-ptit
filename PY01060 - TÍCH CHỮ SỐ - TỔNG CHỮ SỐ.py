def solve():
    s = input()
    sum, mul = 0, 1

    for i in range(len(s)):
        if not i & 1:
            if s[i] != '0':
                mul *= int(s[i])
        else:
            sum += int(s[i])

    print(mul, sum)


for i in range(int(input())):
    solve()
