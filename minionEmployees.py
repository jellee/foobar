# returns max minion employees a company following the "no more than 7 direct reports" theory can have, with no more than x levels of supervision
# Prof Boolean highest level
# each employee has exactly 1 manager

def maxEmployees (x) :
	if x == 0 : return 1
	total, temp = 1, x

	while (temp >= 1) :
		total += 7**temp
		temp -= 1
	return total

print answer(2)
print answer(1)