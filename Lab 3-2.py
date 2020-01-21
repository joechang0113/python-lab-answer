while True:
    n = int(input('Enter an number: '))
    while n >= 0:
        u = n
        print(' ' * (u - n) + '* ' * n)
        n -= 1
