
while True:
    num = str(input("Input something... : "))
    if num != "":
        if num == 0:
            print("0")
        else:
            num_str = str(num)
            num_inv_str = num_str[::-1]
            print(str(num_inv_str))
    else:
        break
