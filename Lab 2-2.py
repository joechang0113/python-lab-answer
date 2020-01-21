while True:
    print("請輸入收入金額:", end="")
    money = int(input())
    if money >= 0:
        if money > 2000000:
            print("付稅金額 :", money*0.3)
        elif money > 1000000 and money < 1999999:
            print("付稅金額 :", money*0.21)
        elif money > 600000 and money < 999999:
            print("付稅金額 :", money * 0.13)
        elif money > 300000 and money < 599999:
            print("付稅金額 :", money*0.06)
        else:
            print("付稅金額 : 0")
