#print("Hi, my name is %s" % "Jessica")
#print("Hi, my name is %d" % 4)
#print("hellllllo my name is %s,i m %d years old" %("serg",3))

#name = input("what is your name")
#age = int(input("when you are boarn"))
#print("hello my name is %s,i m a %d"%(name,2023 - age))
word = input("enter word")
count = 0
for  i in set(word):
	count = word.count(i)
	print("word",i,count)
