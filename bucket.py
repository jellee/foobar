# equal passengers in each car of train
# given x: array of passengers in each car (len 2-100)
# can manipulate passengers in x
# return max equal elements (max cars with equal passengers)
# total passengers: [0,1000000]

def maxEqualBuckets (x) :
	# check for edge cases
	if sum(x) == 0 : raise Exception("There are no passengers!")
	if len(x) < 2 or len(x) > 100 : raise Exception("Train is the wrong size!")
 
 	# some numbers we might want for later
	remainder = sum(x) % len(x)
	total = len(x) - remainder

	# handles case where there is less cars with less passengers
	# this means that the cars with less passengers can be combined to add to total
	if remainder > len(x)/2 :
		extraBucketBunnies = sum(x) / len(x)
		extraBunnies = extraBucketBunnies * total
		normalBucketBunnies = extraBucketBunnies + 1
		total = remainder + (extraBunnies / normalBucketBunnies)

	return total

print answer([1,2])
print answer([1,4,1])
print answer([4, 6, 6, 6, 6])
print answer([50, 2, 30, 5, 10, 9, 7])
print answer([937, 4325, 746765, 98, 4359, 96873])
print answer([0])