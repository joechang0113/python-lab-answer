dic = {"台北市": 6, "新北市": 2, "桃園市": 5, "台中市": 8, "台南市": 3, "高雄市": 9}

option= 0
while(option!=2):
	option= int(input("1.pm2.5\n2.exit\n"))
	if(option==1):
		print(dic.get(input("city: "), "not listed"))
