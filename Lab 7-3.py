my_string= "Python is the best language for String manipulation!"
print(my_string+ "\n")

lst= list(my_string)
lst.reverse()
for i in lst:
	print(i, end= (""))
print("\n")

for i in range(len(lst)):
    if(i%2== 0):
        print(lst[i], end= (""))
print("\n")

print(my_string.swapcase()+ "\n")

print("The sentence '"+ my_string+"' contains\n{0} 'a' letters, and\n{1} 'A' letters!".format(my_string.count('a'), my_string.count('A'))+ "\n")

print("The {0} 'a' are at".format(my_string.count('a')))
tmp= 1
for i in range(len(my_string)):
	if(my_string[i]== 'a'):
		print("a({0}) : {1}".format(tmp, i))
		tmp+= 1
print()

print(my_string.replace(' ', '\n')+ "\n")

print(my_string.replace(' ', '\n').upper())