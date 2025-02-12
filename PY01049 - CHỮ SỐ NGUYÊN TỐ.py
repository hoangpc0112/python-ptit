def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return n > 1


def solve():
    s = input()

    if not is_prime(len(s)):
        print('NO')
        return

    prime = 0

    for i in s:
        if i == '2' or i == '3' or i == '5' or i == '7':
            prime += 1

    print("YES" if prime > len(s) - prime else "NO")


for i in range(int(input())):
    solve()
