def hammingDistance(x, y):	two_x = []	two_y = []	ans = 0	if x == 0:		for i in range(33):			two_x.append(0)	if y == 0:		for i in range(33):			two_y.append(0)	while x != 0:		for i in range(33):			if x/2**(32-i) == 1:				two_x.append(1)				x -= 2**(32-i)			else:				two_x.append(0)	while y != 0:		for i in range(33):			if y/2**(32-i) == 1:				two_y.append(1)				y -= 2**(32-i)			else:				two_y.append(0)	for i in range(33):		if two_x[i] != two_y[i]:			ans += 1		else:			pass	print anshammingDistance(4,1)