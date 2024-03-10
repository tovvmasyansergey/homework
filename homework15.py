#13
def rome(m):
	dc = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	result = 0
	i = 0
	while i < len(m):
		if m[i] in dc:
			if m[i] == "I" and m[i+1] == "V":
				result += 4
				i += 2
			elif m[i] == "I" and m[i+1] == "X":
				result += 9
				i += 2
			elif m[i] == "X" and m[i+1] == "L":
				result += 40
				i += 2
			elif m[i] == "X" and m[i+1] == "C":
				result += 90
				i += 2
			elif m[i] == "C" and m[i+1] == "D":
				result += 400
				i += 2
			elif m[i] == "I" and m[i+1] == "X":
				result += 900
				i += 2
			else:
				result += dc[m[i]]
				i += 1
	return result
print(rome("MMXLIXIV"))
#14
def pre_suf(ml):
	min_word = ml[0]
	result = ""
	for i in ml:
		if len(i) < len(min_word):
			min_word = i
	for i in range(len(min_word)):
		for j in range(len(ml)):
			flag = True
			if min_word[i] != ml[j][i]:
				flag = False
				break
			else:
				continue
		if flag:
			result += min_word[i]
	return result
print(pre_suf(["lgoogle","good","gogli"]))

#20
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
