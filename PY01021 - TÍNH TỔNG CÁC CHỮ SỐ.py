def solve():
    s = "".join(sorted(input()))
    print(''.join(c for c in s if c.isalpha()) + str(sum(int(c)
                                                         for c in s if c.isdigit())))


for i in range(int(input())):
    solve()
