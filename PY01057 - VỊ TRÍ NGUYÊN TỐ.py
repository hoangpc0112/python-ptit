def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def solve():
    s = input()

    for i in range(len(s)):
        if is_prime(i) and not is_prime(int(s[i])):
            print("NO")
            return

        if not is_prime(i) and is_prime(int(s[i])):
            print("NO")
            return

    print("YES")


for i in range(int(input())):
    solve()
