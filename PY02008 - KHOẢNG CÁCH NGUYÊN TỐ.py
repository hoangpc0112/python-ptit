prime = [True] * 10**6


def sieve():
    prime[0] = prime[1] = False

    for i in range(2, 10**6):
        if prime[i]:
            for j in range(i * i, 10**6, i):
                prime[j] = False


def solve():
    n, x = map(int, input().split())
    a = []

    for i in range(2, 10**6):
        if prime[i]:
            a.append(i)

            if len(a) == n:
                break

    cur = x
    print(cur, end=' ')

    for i in a:
        cur += i
        print(cur, end=' ')


sieve()
solve()
