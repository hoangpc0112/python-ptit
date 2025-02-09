def solve():
    s = input()
    print("YES" if s[:2] == s[-2:] else "NO")


t = int(input())
for i in range(t):
    solve()
