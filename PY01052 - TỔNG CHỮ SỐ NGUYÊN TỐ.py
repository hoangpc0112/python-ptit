def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def solve():
    s = input()
    sum = 0

    for i in s:
        sum += int(i)

    print("YES" if is_prime(sum) else "NO")


for i in range(int(input())):
    solve()
