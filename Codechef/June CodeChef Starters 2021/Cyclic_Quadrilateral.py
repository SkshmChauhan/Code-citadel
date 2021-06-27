# cook your dish here
try:
    n = input()
    n = int(n)
    for i in range(0, n):
        a, b, c, d = input().split(" ")
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        if a + c == 180 and b + d == 180:
            print("Yes")
        else:
            print("No")
except EOFError as e:
    pass
