# thequickbrownfoxjumpsoverthelazydog
string= input("Enter ur string: ")
dic= {}
for i in sorted(string):# 加上sorted()先行排序字串, 在進行判斷
	dic[i]= dic.setdefault(i, 0)+1
	#print(dic[i])

for i in dic:
	if(dic[i]>= 1):
		print("{0}: {1}".format(i, dic[i]))
