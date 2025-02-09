def solve():
    s = input()
    for i in s:
        if i != '4' and i != '7':
            print("NO")
            return

    print("YES")


t = int(input())
for i in range(t):
    solve()
