def solve():
    s = input()

    for i in range(0, len(s) - 1):
        if s[i] > s[i + 1]:
            print("NO")
            return

    print("YES")


for i in range(int(input())):
    solve()
