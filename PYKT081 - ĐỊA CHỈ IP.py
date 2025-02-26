def solve():
    try:
        n = input()
        a = n.split(".")

        if len(a) != 4:
            print("NO")
            return

        for i in a:
            if int(i) > 255 or int(i) < 0:
                print("NO")
                return

        print("YES")
    except:
        print("NO")


for i in range(int(input())):
    solve()
