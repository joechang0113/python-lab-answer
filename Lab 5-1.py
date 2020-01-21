def conpute(a, b):
    return pow(a, b)


while True:

    num1, num2 = map(int, input("plz input two numbers: ").split())
    if num1 and num2 >= 0:
        print(conpute(num1, num2))#呼叫compute 執行指數命令
    else:
        break
