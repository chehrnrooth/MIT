def gcdRecur(a, b):
	if a > b:
		big = a
		small = b
	else: 
		big = b
		small = a
	remainder = big%small
	if remainder == 0:
		return small
	else:
		b = remainder
		a = small
		return gcdRecur(a, b) 
print gcdRecur(12, 17)
