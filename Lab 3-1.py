while True:
    num = []
    print("plz input a number : ", end="")
    a = int(input())
    count = 0
    for i in range(1, a+1):
        if i % 5 == 0:
            count = count + i

            num.append(i)

    print("被5整除的有: ", num)
    print("總和為 : ", count)
