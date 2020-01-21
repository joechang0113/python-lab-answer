def GCD1(a, b, *argv):
	while(b != 0):
		a %= b
		(a, b) = (b, a)
	return a


def GCD2(a, b, *argv):
	if(b != 0):
		return GCD2(b, a % b)
	return a


m = int(input("m: "))
n = int(input("n: "))
print("\niterative GCD({0}, {1}): {2}".format(m, n, GCD1(m, n)))
print("recursion GCD({0}, {1}): {2}".format(m, n, GCD2(m, n)))
