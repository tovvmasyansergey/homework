import random

def read_file(ffile):
	f = open(ffile)
	mstr = f.readlines()
	ml = []
	for i in mstr:
		ml.append(i.strip())
	return ml
#print(read_file("homework14.txt"))
def input_name():
	name = input("please input your name")
	return name
def index_list(ml):
	ind = []
	while len(ind) < 5:
		i = random.randint(0, len(read_file("homework14.txt")) -1)
		if i not in ind:
			ind.append(i)
	return ind
def quest_list(ml):
#print(index_list(questions))
	quests = []
	for i in index_list(read_file("homework14.txt")):
		quests.append(read_file("homework14.txt")[i])
	return quests
#print(quest_list(questions))
def quest_dict(ml):
	questions_dict = {}
	for question in quest_list(read_file("homework14.txt")):
		q,a = question.split("?")
		questions_dict[q] = a.split(",")
	return questions_dict
#print(quest_dict(questions))
def quest_print(ml):
	count = 0
	for q,a in quest_dict(read_file("homework14.txt")).items():
		print( q + "?")
#print(quest_print(questions))
		correct = a[0]
		random.shuffle(a)
		for el in a:
			print(el)
#quest_print(questions)
		answer = input("Enter your answer: ")
#quest_print(questions)
		if answer.lower() == correct.lower():
			print("Corect")
			count += 1
		else:
			print("Wrong. The correct answer was:", correct)
	print("You got %d/%d" %(count, len(quest_dict(read_file("homework14.txt")))))
	return count
def write_result(ffname):
	f = open(ffname,"a")
	f.write(input_name()+":"+ str(quest_print(read_file("homework14.txt"))) + "\n")
	f.close()
write_result("point.txt")
def open_file(ffname):
	dc = {}
	f = open(ffname)
	mstr = f.read()
	ml = mstr.split()
	for i in ml:
		dc[i[:i.index(":")]] = i[i.index(":")+1:]
	return dc
dc_point = open_file("point.txt")
def sort_result(md):
	ml1 = list(md.items())
	ml1.sort(key=lambda x: x[1],reverse = True)
	return ml1
def write_result_file(fname):
	sort_list = sort_result(dc_point)
	with open(fname,"w") as f:
		for k, v in sort_list:
			f.write(k + ":" + str(v) + "\n")
#write_result("point.txt")
write_result_file("point1.txt")
#write_result("point.txt")
