num= []
for i in range(10):
	num.append(int(input("num[{0}]: ".format(i))))

mode = 0
for i in num:
	if(num.count(i)>num.count(num[mode])):
		mode= num.index(i)
print("\nmode: {0} for {1} times".format(num[mode], num.count(num[mode])))
