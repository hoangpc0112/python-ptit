def solve():
    s = input()

    if not len(s) & 1 or s[0] == s[1]:
        print("NO")
        return

    for i in range(0, len(s) - 1, 2):
        if s[i] != s[0]:
            print('NO')
            return

    print('YES')


for i in range(int(input())):
    solve()
