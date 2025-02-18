is_prime = [1] * (10**6 + 5)
emirp = []


def sieve():
    is_prime[0] = is_prime[1] = 0

    for i in range(2, 10**6):
        if is_prime[i]:
            for j in range(i*i, 10**6 + 5, i):
                is_prime[j] = 0

    for i in range(10, 10**6):
        if i != int(str(i)[::-1]) and is_prime[i] and is_prime[int(str(i)[::-1])]:
            emirp.append(i)


def solve():
    n = int(input())
    res = [i for i in emirp if i < n]

    for i in res[:]:
        rev = int(str(i)[::-1])

        if rev in res:
            print(i, rev,  end=" ")

            res.remove(rev)
            res.remove(i)

    print()


sieve()
for i in range(int(input())):
    solve()
