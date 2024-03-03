def find_pair(ml,target):
	ml.sort()
	left = 0
	right = len(ml) - 1
	while left < right:
		c_sum = ml[left] + ml[right]
		if c_sum == target:
			return ml[left],ml[right]
		elif c_sum < target:
			left += 1
		else:
			right -=1
	return []
print(find_pair([1,3,6,2,5,1],8))

