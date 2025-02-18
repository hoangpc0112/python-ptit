def solve():
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    print(*(a[d:] + a[:d]))


for i in range(int(input())):
    solve()
