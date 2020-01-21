
while True:
    print("Input a integer : ", end=" ")
    data = int(input())
    count = 0
    if data >= 0:
        for i in range(1, data+1):
            if data % i == 0:
                count = count + 1
        if count == 2:
            print(data, "Is Prime number\n")
        else:
            print(data, "Not Prime number\n")





