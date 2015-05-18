# given: list of meeting requests (request = 2 element list)
# returns: maximum number of non-overlapping meetings that can be scheduled
# if start time of one coincides with the end time of another ==> not overlapping
# start and end times are non-negative integers no larger than 1000000
# start time is always less than end time
# number of meetings: [1, 100]
# unordered list

def maxMtgs (meetings) :
	meetings.sort()
	oldEnd, numMtgs = meetings[0][1], 1

	for start, end in meetings[1:] :
		if start >= oldEnd :
			numMtgs += 1
			oldEnd = end
	return numMtgs

print maxMtgs([[2,7], [2,3], [1,2], [3,6], [4,8], [3,5], [3,4]])