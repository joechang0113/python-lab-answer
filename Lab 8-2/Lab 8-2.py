text= ''
with open("Lab 8-2/台南大學校歌.txt", 'r', encoding="UTF-8") as file:
    text=file.read()

option= 0
while(option!= -99):
    option= int(input("line: "))
    if(option== 0):
        print(text)
    elif(option<=10 and option!= -99):
        print(text.strip().split('\n')[option-1])
