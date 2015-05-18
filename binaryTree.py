# grid of nxn rooms
# only moves down or right
# given: food # in range [1, 200]
# given: grid list of N lists, each list is a row of N rooms.
# grid sublist integer contains amount of food zombie needs
# top left room is 0
# Max N = 20, food per zombie = [1,10]
# runtime: O(N^2)

def minFoodLeft (food, grid) :
	# first get size of grid, total steps taken
	N = len(grid[0])
	sumGrid = grid[:]

	# less food than zombies, impossible
	if food < (N-1)*2 : return -1

	# first do sums on the border grid
	for i in range(N-2, -1, -1) :
		sumGrid[i][N-1] += sumGrid[i+1][N-1]
		sumGrid[N-1][i] += sumGrid[N-1][i+1]

	# now fill in the inner grid with lists
	for i in range(N-2, -1, -1) :
		for j in range(N-2, -1, -1) :
			currVal = grid[i][j]
			firstChild = sumGrid[i+1][j]
			secondChild = sumGrid[i][j+1]
			if (not isinstance(firstChild, list)) and (not isinstance(secondChild, list)) :
				sumGrid[i][j] = [currVal + firstChild, currVal + secondChild]
			else: 
				newList = firstChild
				if isinstance(firstChild, list) :
					if isinstance(secondChild, list) :
						newList = firstChild + list(set(secondChild) - set(firstChild))
					elif secondChild not in firstChild :
						newList = firstChild[:]
						newList.append(secondChild)
				elif isinstance(secondChild, list) :
					newList = secondChild[:]
					if firstChild not in secondChild :
						newList.append(firstChild)
				sumGrid[i][j] = [currVal + item for item in newList]
	
	if food in sumGrid[0][0] : return 0
	else :
		minFoodLeft = 200
		for item in sumGrid[0][0] :
			foodLeft = food - item
			if item < food and foodLeft < minFoodLeft :
				minFoodLeft = foodLeft
		if minFoodLeft == 200 : return -1
		return minFoodLeft

print minFoodLeft(7, [[0,2,5],[1,1,3],[2,1,1]])
print minFoodLeft(12, [[0,2,5],[1,1,3],[2,1,1]])

def bruteForce (food, grid) :
	# first get size of grid, total steps taken
	N = len(grid[0])
	totalSteps = (N-1)*2
	nodeList = []
	minFoodLeft = 200

	# less food than zombies, impossible
	if food < totalSteps : return -1
	nodeList.append([food, totalSteps, 0, 0])

	while (nodeList) :
		node = nodeList.pop(0)
		i, j = node[2], node[3]
		stepsLeft = node[1] - 1

		if stepsLeft < 0 :
			minFoodLeft = min(node[0], minFoodLeft)
			continue

		# get the children of current node (rt & down)
		if i+1 < N : 
			goDn = grid[i+1][j]
			tempFood = node[0] - goDn
			if tempFood >= stepsLeft :
				nodeList.append([tempFood, stepsLeft, i+1, j])
		if j+1 < N :
			goRt = grid[i][j+1]
			tempFood = node[0] - goRt
			if tempFood >= stepsLeft : 
				nodeList.append([tempFood, stepsLeft, i, j+1])
	return minFoodLeft