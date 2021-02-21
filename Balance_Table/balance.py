import numpy as np
import math as math

# checks the center of gravity (cog) of a table by computing it's cog in the x and y dimensions
# calculations start with the origin at the bottom left of a table (0,0)
def checkBalance(table, blocks, size):

    totalMass = sum(blocks) # total weight of all the blocks
    xLoc = 0.5
    yLoc = size - 0.5
    momentTableX = [[0] * (size) for _ in range(size)] # table of moments in the x dimension
    momentTableY = [[0] * (size) for _ in range(size)] # table of moments in the y dimension
    perfectBalanceX = size/2
    perfectBalanceY = size/2

    # determine the safe zone for the table
    # 2x2 for even, 4x4 for odd
    if (size % 2 == 0):
        topLeft = [size/2 - 1, size/2 + 1]
        topRight = [size/2 + 1, size/2 + 1]
        bottomLeft = [size/2 - 1, size/2 - 1]
        bottomRight = [size/2 + 1, size/2 - 1]
        safeZone = [topLeft, topRight, bottomLeft, bottomRight]
        print("Safe Zone: ", safeZone, "\n")
    else:
        topLeft = [size/2 - 2, size/2 + 2]
        topRight = [size/2 + 2, size/2 + 2]
        bottomLeft = [size/2 - 2, size/2 - 2]
        bottomRight = [size/2 + 2, size/2 - 2]
        safeZone = [topLeft, topRight, bottomLeft, bottomRight]
        print("Safe Zone: ", safeZone, "\n")

    # determine x center of gravity
    for x in range(size):
        for y in range(size):
            momentTableX[x][y] = table[x][y] * xLoc
            xLoc = xLoc + 1
        xLoc = 0.5
    momentsX = np.sum(momentTableX)
    cogX = momentsX/totalMass
    print("Center of Gravity X: ", cogX)

    # determine y center of gravity
    for x in range(size):
        for y in range(size):
            momentTableY[y][x] = table[y][x] * yLoc
            yLoc = yLoc - 1
        yLoc = size - 0.5
    momentsY = np.sum(momentTableY)
    cogY = momentsY/totalMass
    print("Center of Gravity Y: ", cogY, "\n")

    if (cogX < topLeft[0] or cogX > topRight[0]):
        return False
    elif (cogY < bottomLeft[1] or cogY > topLeft[1]):
        return False
    else:
        return True


# This method tests a grid to see if it is a magic square
# Rows, columns, and diagonals must equal the same number, the magic constant
# Returns True or False
def isMagicSquare(grid):

    magic = True

    n = np.size(grid, 0)
    magicConstant = n * ((math.pow(n, 2) + 1)) / 2   # n[(n^2+1)/2], formula to find the magic constant

    # check rows
    for x, row in enumerate(grid):
        if sum(row) != magicConstant:
            magic = False
            return magic


    # check columns
    gridT = np.transpose(grid)
    for y, column in enumerate(gridT):
        if sum(column) != magicConstant:
            magic = False
            return magic

    # check diagonals
    total = 0
    for x in range(0, n, 1):
        element = grid[x][x]
        total = total + element
    if total != magicConstant: magic = False

    y = 0
    total = 0
    for x in range(n-1, -1, -1):
        element = grid[x][y]
        total = total + element
        y = y + 1
    if total != magicConstant: magic = False

    return magic

# This method tests the isMagicSquare method
# first grid is a magic square, second grid is not
def testMagicSquare():

    test = [[4, 9, 2],
            [3, 5, 7],
            [8, 1, 6]]
    print(np.matrix(test))
    print(isMagicSquare(test));

    test2 = [[2, 9, 2],
             [3, 3, 7],
             [8, 1, 7]]
    print(np.matrix(test2))
    print(isMagicSquare(test2));
# end testMagicSquare method



#to print magic square of double order
def doublyEven(n):

	# 2-D matrix with all entries as 0
	table = [[(n*y)+x+1 for x in range(n)]for y in range(n)]

	# Change value of array elements at fix location
	# as per the rule (n*n+1)-arr[i][[j]

	# Corners of order (n/4)*(n/4)
	# Top left corner
	for i in range(0,n//4):
		for j in range(0,n//4):
			table[i][j] = (n*n + 1) - table[i][j];

	# Top right corner
	for i in range(0,n//4):
		for j in range(3 * (n//4),n):
			table[i][j] = (n*n + 1) - table[i][j];

	# Bottom Left corner
	for i in range(3 * (n//4),n):
		for j in range(0,n//4):
			table[i][j] = (n*n + 1) - table[i][j];

	# Bottom Right corner
	for i in range(3 * (n//4),n):
		for j in range(3 * (n//4),n):
			table[i][j] = (n*n + 1) - table[i][j];

	# Centre of matrix,order (n/2)*(n/2)
	for i in range(n//4,3 * (n//4)):
		for j in range(n//4,3 * (n//4)):
			table[i][j] = (n*n + 1) - table[i][j];

	return table
#end doublyEven

# odd sized magic squares
def generateSquare(n):

	# 2-D array with all
	# slots set to 0
	table = [[0 for x in range(n)]
					for y in range(n)]

	# initialize position of 1
	i = n / 2
	j = n - 1

	# Fill the magic square
	# by placing values
	num = 1
	while num <= (n * n):
		if i == -1 and j == n: # 3rd condition
			j = n - 2
			i = 0
		else:

			# next number goes out of
			# right side of square
			if j == n:
				j = 0

			# next number goes
			# out of upper side
			if i < 0:
				i = n - 1

		if table[int(i)][int(j)]: # 2nd condition
			j = j - 2
			i = i + 1
			continue
		else:
			table[int(i)][int(j)] = num
			num = num + 1

		j = j + 1
		i = i - 1 # 1st condition

	return table

#end of odd-magic square

# start of the singly even function
#msut build an odd magic square first
def build_odd(n):
    if n % 2 == 0:
        n += 1
    table = [[0 for j in range(n)] for i in range(n)]
    p = 1
    i = n // 2
    j = 0
    while p <= (n * n):
        table[i][j] = p
        ti = i + 1
        if ti >= n: ti = 0
        tj = j - 1
        if tj < 0: tj = n - 1
        if table[ti][tj] != 0:
            ti = i
            tj = j + 1
        i = ti
        j = tj
        p = p + 1

    return table, n


# build singly even magic square
def build_sems(n):
    if n % 2 == 1:
        n += 1
    while n % 4 == 0:
        n += 2

    table = [[0 for j in range(n)] for i in range(n)]
    z = n // 2
    b = z * z
    c = 2 * b
    d = 3 * b
    o = build_odd(z)

    for j in range(0, z):
        for i in range(0, z):
            a = o[0][i][j]
            table[i][j] = a
            table[i + z][j + z] = a + b
            table[i + z][j] = a + c
            table[i][j + z] = a + d

    lc = z // 2
    rc = lc
    for j in range(0, z):
        for i in range(0, n):
            if i < lc or i > n - rc or (i == lc and j == lc):
                if not (i == 0 and j == lc):
                    t = table[i][j]
                    table[i][j] = table[i][j + z]
                    table[i][j + z] = t

    return table
