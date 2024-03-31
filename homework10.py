ml = "{[]}()()()[(((())))]"
nm = []
flag = True
dc = {'(':')','[':']','{':'}'}
for i in ml:
	if i in dc:
		nm.append(dc[i])
	elif i in dc.values():
		if nm == []:
			print(ml.index(i),i)
			flag = False
			break
		elif nm[-1] == i:
			nm.remove(i)
		elif nm[-1] != i:
			print(ml.index(i),i)
			flag = False
			break
if nm != [] and flag:
	for key in dc:
		if nm[-1] ==dc[key]:
			print(key,ml.rindex(key))
if flag and nm == []:
	print('good')
