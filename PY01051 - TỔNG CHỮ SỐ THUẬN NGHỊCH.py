def solve():
    s = input()
    sum = 0

    for i in s:
        sum += int(i)

    print("YES" if len(str(sum)) > 1 and str(sum) == str(sum)[::-1] else "NO")


for i in range(int(input())):
    solve()
