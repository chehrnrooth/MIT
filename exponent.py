#author chehrnrooth
def recurPower(base, exp):
	'''
	Finds the exponential iteration of a number through recursion
	'''
   	if exp == 0:
   		return 1
   	else:
   		return base*recurPower(base, exp-1)
print recurPower(3, 3)
