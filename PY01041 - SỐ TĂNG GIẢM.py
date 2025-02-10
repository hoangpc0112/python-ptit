def solve():
    n = input()

    if len(n) < 3:
        print("NO")
        return

    i = 1

    while i < len(n) and n[i] > n[i - 1]:
        i += 1
    while i < len(n) and n[i] < n[i - 1]:
        i += 1

    print("YES" if i == len(n) else "NO")


for i in range(int(input())):
    solve()
