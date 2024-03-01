def discriminant(a,b,c):
	x1 = 0
	x2 = 0
	d = 0
	d = b*b - 4*a*c
	if a != 0:
		if d > 0:
			x1 = (-b+(d**0.5))/(2*a)
			x2 = (-b-(d**0.5))/(2*a)
		elif d == 0:
			x1 = x2 = -b/(2*a)
			return x1
		elif d < 0:
			return "&"
	if a == 0:
		return "a == 0"
	return x1,x2
print(discriminant(0,2,1))
