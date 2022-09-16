height = [4,2,0,3,2,5]
maxi = 0
max_left, max_right = [], []

for i in range(len(height)):
	max_left.append(maxi)
	if height[i] > maxi:
		maxi = height[i]

maxi = 0
for i in range(len(height)-1, -1, -1):
	max_right.append(maxi)
	if height[i] > maxi:
		maxi = height[i]
max_right.reverse()

units = 0
for i in range(len(height)):
	addition = min(max_left[i], max_right[i]) - height[i]
	if addition > 0:
		units += addition
	else:
		continue

print(units)
