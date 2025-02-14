def solve():
    s = input()
    sum, mul, zero = 0, 1, 0

    for i in range(len(s)):
        if i & 1:
            if s[i] == '0':
                zero += 1
            else:
                mul *= int(s[i])
        else:
            sum += int(s[i])

    print(sum, mul if zero < len(s) // 2 else 0)


for i in range(int(input())):
    solve()
