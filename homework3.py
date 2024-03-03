#0.exersize 1
#print("What is the capital of France")
#word = "erevan"
#newword = "_"*len(word)
#while newword != word:
#	letter = input("Please input letter ")
#	for i in range(len(word)):
#		if word[i] == letter:
#			newword = newword[:i] + letter + newword[i + 1:]
#	print(newword)


#1. upper()
#2. lower()


#mstr ="HEllo world  good  day         "
#print("Upper ",end = '')
#for i in mstr:
#	if ord(i) > 96 and ord(i) < 122:
#		print(chr(ord(i) - 32),end = '')
#	else:
#		print(i,end = '')
#print()
#print("Lower ",end = '')
#for i in mstr:
#	if ord(i) > 64 and ord(i) < 91:
#		print(chr(ord(i) + 32),end = '')
#	else:
#		print(i,end = '')
#print()


#3.strip()


mstr = "    Hello     world  good day"
index = 0
count = 1
while mstr[index] == ' ':
	index+=1
while mstr[-count] == ' ':
	count -=1
if index == 0 and count == 1:
	print(mstr)
else:
	print(mstr[index:(len(mstr) - count+1)])


#4.swapcase()


#print("big is small and small is big ")
#print(mstr)
#for i in mstr:
#	if ord(i) > 96 and ord(i) < 122:
#		print(chr(ord(i) - 32),end = '')
#	if ord(i) > 64 and ord(i) < 91:
#		print(chr(ord(i) + 32),end = '')
#	if ord(i) == 32:
#		print(i,end = '')


#5 split()
mstr = input("Please enter a sentence: ")#hello good world
ml = [] 
tmp = ""
for el in mstr:
	if el == " ":
		ml.append(tmp)
		tmp  = "" 
	else:
		tmp += el
if tmp:
	ml.append(tmp)

print(ml)

#print()
#mstr = "  Hello world     good    day     "
#index = 0
#count = len(mstr) - 1
#while mstr[index] == ' ':
#        index+=1
#while mstr[index] == ' ':
#        count -=1
#if index == 0 and count == 1:
#        word = mstr
#else:
#        word = mstr[index:count + 1]
#word = mstr.strip()
#emp = ""
#result = []
#index_1 = 0
#count_1 = 0
#while index_1 < len(word):
#        if word[index_1] != ' ':
#                emp += word[index_1]
#        elif word[index_1] == ' ' and emp:
#                result.append(emp)
#                emp = ""
#        index_1+=1
#result.append(emp)
#print(result)


#6 tittle()
#mstr = "hello        world     "
#for i in range(len(mstr)):
#	if i == 0 or (mstr[i-1] == ' ' and mstr[i] != ' '):
#		if 96 < ord(mstr[i+1]) < 123:
#			mstr = mstr[:i] + chr(ord(mstr[i]) - 32) + mstr[i+1:]
#print(mstr)

#7.count()


#mstr = "hello world"
#count = 0
#simvol = input("enter simvol ")
#for i in mstr:
#	if i == simvol:
#		count += 1
#print(count)


#8.isalpha()


#mstr = "hello"
#count = 0
#for i in mstr:
#	if ord(i) > 96 and ord(i) < 123 or (ord(i) > 64 and ord(i) < 91):
#		count += 1
#if count == len(mstr):
#	print(True)
#else:
#	print(False)


#9.isdigit()


#mstr = "df"
#count = 0
#num = "0123456789"
#for i in mstr:
#	if i in num:
#		count += 1
#if count == len(mstr):
#      print(True)
#else:
#       print(False)


#10.startswith()


#mstr = " hello world"
#simvol = input("input simvol")
#if mstr[0] == simvol:
#	print(True)
#else:
#	print(False)
