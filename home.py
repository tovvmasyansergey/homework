
word = "hello world nr     bxbxb sbbsbs"
emp = ""
result = []
index = 0
count = 0
while index < len(word):
	if word[index] != ' ':
		emp += word[index]
	elif word[index] == ' ' and emp:
		result.append(emp)
		emp = ""
	index+=1
result.append(emp)
print(result)

