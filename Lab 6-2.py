num=set()
tmp=int(input("num: "))
while(tmp!=-9999):
	num.add(tmp)
	tmp=int(input("num: "))
print("length: {0}".format(len(num)))
print("max: {0}".format(max(num)))
print("min: {0}".format(min(num)))
print("sum: {0}".format(sum(num)))