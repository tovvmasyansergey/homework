#1
snt = input()
dc = {}
max = 0
elem = []
for i in snt:
	if i in dc:
		dc[i] += 1
	else:
		dc[i] = 1
print(dc)
#2
for i in dc.values():
	elem.append(i)
	if int(i) > max:
		max = int(i)
for i, value in dc.items():
	if value == max:
		print(i)

#3
ml = list(dc.items())
for i in range(len(elem)):
	for j in range(len(elem) - i - 1):
		if ml[j][1] > ml[j + 1][1]:
			ml[j],ml[j+1] = ml[j+1],ml[j]
print(ml)
