def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def solve():
    s = input()
    prime = 0

    for i in s:
        if is_prime(int(i)):
            prime += 1

    print("YES" if is_prime(len(s)) and prime >= len(s) // 2 else "NO")


for i in range(int(input())):
    solve()
