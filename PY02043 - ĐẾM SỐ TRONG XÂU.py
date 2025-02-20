def solve():
    s = input()
    n = input()

    count = 0
    i = 0

    while i <= len(s) - len(n):
        if s[i:i + len(n)] == n:
            count += 1
            i += len(n)
        else:
            i += 1

    print(count)


for i in range(int(input())):
    solve()
