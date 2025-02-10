def solve():
    n = int(input())
    cnt = 0

    while n % 7 != 0 and cnt <= 1000:
        n += int(str(n)[::-1])
        cnt += 1

    print(n if cnt <= 1000 else -1)


for i in range(int(input())):
    solve()
