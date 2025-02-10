def solve():
    s = input()
    sum = int(s[0])

    for i in range(1, len(s)):
        if abs(int(s[i]) - int(s[i-1])) != 2:
            print("NO")
            return

        sum += int(s[i])

    print("YES" if sum % 10 == 0 else "NO")


for i in range(int(input())):
    solve()
