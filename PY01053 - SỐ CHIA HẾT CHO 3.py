def solve():
    s = input()
    sum = 0

    for i in s:
        sum += int(i)

    print("YES" if sum % 3 == 0 else "NO")


for i in range(int(input())):
    solve()
