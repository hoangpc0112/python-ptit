def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def solve():
    n = input()

    if not is_prime(int(n)):
        print("No")
        return

    if not is_prime(int(n[::-1])):
        print("No")
        return

    if not is_prime(sum(map(int, n))):
        print("No")
        return

    if not all(c in "2357" for c in n):
        print("No")
        return

    print("Yes")


for i in range(int(input())):
    solve()
