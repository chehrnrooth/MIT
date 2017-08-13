def gcdIter(a, b):
	'''
	Finds greatest common denominator
	'''
	if a > b:
		num = a-1
	else:
		num = b-1
	while num>0:
		if a % num == 0 and b % num ==0:
			return num
		num -=1
print gcd(12, 9)
