def convert_base(n, b):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = ""

    while n > 0:
        res = digits[n % b] + res
        n //= b

    return res


def solve():
    n, b = map(int, input().split())
    print(convert_base(n, b))


for i in range(int(input())):
    solve()
