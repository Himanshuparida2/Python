L=[i for i in range(1,101)]
def is_divisible_by_5(x):
	if(x%5==0):
		return True
	return False
L_Filter=list(filter(is_divisible_by_5,L))
print(L_Filter)
