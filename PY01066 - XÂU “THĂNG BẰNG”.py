def solve():
    s = input()
    rs = s[::-1]

    for i in range(1, len(s)):
        if abs(ord(s[i]) - ord(s[i - 1])) != abs(ord(rs[i]) - ord(rs[i - 1])):
            print("NO")
            return

    print("YES")


for i in range(int(input())):
    solve()
