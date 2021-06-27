try:
    n = int(input())
    for i in range(0, n):
        a, b, c = input().split(" ")
        a = int(a)
        b = int(b)
        c = int(c)
        total_time = (a + 180) * 2
        left_time = b + c
        print(total_time - left_time)
except EOFError as e:
    pass

# 3
# 10 0 2
# 11 2 1
# 12 192 192
