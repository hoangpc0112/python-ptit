def solve():
    n = input()

    if n[0] == n[1]:
        print("NO")
        return

    for i in range(2, len(n)):
        if n[i] != n[i & 1]:
            print("NO")
            return

    print("YES")


for i in range(int(input())):
    solve()
