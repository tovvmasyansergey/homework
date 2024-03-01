#30
def big_name(ml):
	name = ""
	for i in ml:
		if len(list(i.keys())[0]) > len(name):
			name = i.keys()
	return list(name)[0]
print(big_name([{'eph': 456},{'npuagb':67},{'ysmu hh':78}]))
#29
def sort_res(ml):
	for i in range(len(ml)):
		for j in range(len(ml) - i - 1):
			if list(ml[j].values()) > list(ml[j+1].values()):
				ml[j],ml[j+1] = ml[j+1],ml[j]
	return ml
print(sort_res([{'jack':30},{'john':34},{'Ann':25}]))
#28
def age(ml):
	max = 0
	for i in ml:
		for value in i.values():
			if value > max:
				max = value
				ml1 = i
	return ml1
print(age([{'john':23},{'Bob':45}]))
#27
def max_num(mstr):
	ml = mstr.split()
	max_n = 0
	for i in ml:
		if i.isdigit() :
			max_n = i
	for i in ml:
		if i.isdigit() and i>max_n:
			max_n = i
	return max_n
print(max_num("hello 23 good -1 23 45"))
#26
def many_words(ml):
	max_words = ""
	max_len = 0
	for i in ml:
		if max_len < len(i):
			max_len = len(i)
			max_words = i
	return max_words
print(many_words(["hello good world","google"]))
#25
def max_vowels(ml1):
	dc = {}
	ml = []	
	vowels = "aeyuio"
	max_num = 0
	word = ""
	for i in ml1:
		if type(i) == str:
			ml.append(i)

	for i in ml:
		tmp = i
		count = 0
		for j in tmp:
			if j in vowels:
				count += 1
		dc[i] = count
	for i in dc:
		if dc[i] > max_num:
			max_num = dc[i]
			word = i
	return word
print(max_vowels(['hello','goood',2]))
#23
def sort_num(ml):
	ml1 = []
	for i in ml:
		if type(i) == int:
			ml1.append(i)
	for i in range(len(ml1)):
		for j in range(len(ml1) - i -1):
			if ml1[j] > ml1[j+1]:
				ml1[j],ml1[j+1] = ml1[j+1],ml1[j]
	return ml1
print(sort_num([2,1,100,6,'a']))
#22
def len_str(ml):
	ml1 = []
	for i in ml:
		if type(i) == str:
			ml1.append(len(i))
	return ml1
print(len_str(['hello','good']))
#24
def sort_len(ml):
	ml1 = len_str(ml)
	return sort_num(ml1)
print(sort_len(['hello',4,34,'good']))
#21
def middle(ml):
	result = 0 
	count = 0
	for i in ml:
		if type(i) == int:
			result += i
			count += 1
	return result/count
print(middle([1,2,3,4,'a']))
#20
def bin_even(ml):
	ml1 = []
	for i in ml:
		if type(i) == int and i%2 == 0 and 10 <= i <= 98 :
			ml1.append(i)
	return ml1
print(bin_even([34,45,'a',8,0,32]))
#19
def max_num(ml):
	maxn = 0
	ind = 0
	for i in range(len(ml)):
		if type(ml[i]) == int:
			maxn = ml[i]
			ind = i
			break
	for i in range(i+1,len(ml)):
		if type(ml[i]) == int and ml[i] > maxn:
			maxn = ml[i]
	return maxn
print(max_num(['a',-3,4,4,2,4,56,78,'a']))
#18
def check_str(ml):
	count = 0 
	for i in ml:
		if type(i) is str:
			count+=1
	return count
print(check_str([1,2,3,'a','f']))
#17
def start_end(num):
	if 0 <= num <= 9:
		return "num < 9"
	count = 0
	num1 = num
	while num > 0:
		num = num // 10
		count += 1
	return num1%10 * (num1//(10**(count-1)))
print(start_end(45))
#16
def poll(num):
	ml = []
	pollindrom = True
	num1 = num
	num2 = num
	while pollindrom:
		if str(num1) == str(num1)[::-1]:
			return num1
			pollindrom = False
		else:
			num1 += 1
		if str(num2) == str(num2)[::-1]:
			return num2
			pollindrom = False
		else:
			num2 -= 1
print("pollindrom")
print(poll(15))
#15
def is_pollindrom(num):
	num1 = num
	ml = []
	count = 0
	while num > 0:
		num = num // 10
		count += 1
	for i in range(0,count):
		a = num1 // 10**i
		ml.append(a%10)
	for i in range(len(ml)//2):
		if ml[i] == ml[-(i+1)]:
			continue
		else:
			return 'no pollindrom'
	return 'pollindrom'
print(is_pollindrom(45654))

#13
def ind_word(mstr,num):
	ml = ""
	ml += mstr[num]
	ml += mstr[-num-1]
	return ml
print(ind_word("hello golod",2))
#11
def letter(mstr):
	ml = {}
	for i in mstr:
		if i not in ml:
			ml[i] = 1
		else:
			ml[i] += 1
	count = 0
	let = ''
	for i in ml:
		if ml[i] > count:
			count = ml[i]
			let = i
	return let
print(letter("hello good world"))
#10
def maxword(mstr):
	ml = mstr.split()
	maxword = ""
	for i in ml:
		if len(i) > len(maxword):
			maxword = i
	return maxword
print(maxword("hello good worllld"))
#12
def maxlett(mstr):
        mw = maxword(mstr)
        return letter(mw)
print(maxlett("hello good"))
#9
def str_2(mstr,num1,num2):
	return mstr[num1:num2]
print(str_2("hello good world",2,6))
#8
def rev(mstr):
	tmp= ""
	for i in mstr:
		tmp = i + tmp
	return tmp
print(rev("hello good world"))
#7
def tittle_1(mstr):
        for i in range(len(mstr)):
                if i == 0 or (mstr[i-1] == ' ' and mstr[i] != ' '):
                        if 96 < ord(mstr[i+1]) < 123:
                                mstr = mstr[:i] + chr(ord(mstr[i]) - 32) + mstr[i+1:]
        return mstr
print(tittle_1("hello good "))
#6
def lower_1(mstr):
        ml = ""
        for i in mstr:
                if ord(i) > 64 and ord(i) < 91:
                        ml +=chr(ord(i) + 32)
                else:
                        ml += i
        return ml
print(lower_1("HELLo good day"))
#5
def upper_1(mstr):
        ml = ""
        for i in mstr:
                if ord(i) > 96 and ord(i) < 122:
                        ml += chr(ord(i) - 32)
                else:
                        ml += i
        return ml
print(upper_1("hello good world"))
#4
def matem(num1,num2):
	ml = {'sum':0,'minus':0,'devide':0,'multiplay':0}
	ml['sum'] = num1+num2
	ml['minus'] = num1-num2
	if num1 != 0:
		ml['devide'] = num1/num2
	else:
		return 'num1 == 0'
	ml['multiplay'] = num1*num2
	return ml
print(matem(2,3))
#3
def middle(*args):
	result = 0
	for i in args:
		result += i
	return result/len(args)
print(middle(1,2,3,4))
#2
def count_str(*args):
	count = 0
	for i in args:
		if type(i) == str:
			count += 1
	return count
print(count_str('a','d',43,4))
#1
def sum_num(*args):
	result = 0
	for i in args:
		if str(i).isdigit():
			result += i
	return result
print(sum_num(1,2,3,4,'a'))
