import random
ml = [["- ","- ","- "],["- ","- ","- "],["- ","- ","- "]]


def board(ml):
	for i in range(3):
		for j in range(3):
			print(ml[i][j],end = " ")
		print()


def user_check():
	choose = input("Please choose x or o: ")
	if choose == "x":
		return "x "
	elif choose == "o":
		return "o "
	else:
		return user_check()


def computer_check(user):
	if user == "x ":
		return "o "
	else:
		return "x "

def user_step(user):
	numb_ls = "012"
	simvol = input("adress")
	if len(simvol) == 2 and (simvol[0] in numb_ls and simvol[1] in numb_ls):
		num1 = int(simvol[0])
		num2 = int(simvol[1])
		if ml[num1][num2] == "- ":
			ml[num1][num2] = user
		else:
			user_step(user)
	else:
		print("only adress")
		user_step(user)


def computer_step(comp):
	m = [0,1,2]
	flag1 = True
	while flag1:
		num1 = random.choice(m)
		num2 = random.choice(m)
		if ml[num1][num2] == "- ":
			ml[num1][num2] = comp
			flag1 = False


def who_win(ml,simvol):
	for i in range(3):
		if all([ml[i][j] == simvol for j in range(3)]):
			return True
	for j in range(3):
		if all([ml[i][j] == simvol for i in range(3)]):
			return True
	if all(ml[i][i] == simvol for i in range(3)) or all(ml[i][2 - i] == simvol for i in range(3)):
		return True


def check_two_player1():
	player1 = input("player1 input x or o: ")
	if player1 == "x":
		return "x "
	elif player1 == "o":
		return "o "
	else:
		check_two_player1()


def check_two_player2(player):
	if player == "x ":
		return "o "
	else:
		return "x "

def steps_of_players(player):
	simvol = input()
	num1 = int(simvol[0])
	num2 = int(simvol[1])
	if ml[num1][num2] == "- ":
		ml[num1][num2] = player

num = input("if you want play with comp enter 0,else enter 1")
if int(num) == 0:
	flag = True
	user = user_check()
	comp = computer_check(user)
	while flag:
		user_step(user)
		player = [user,comp]
		if who_win(ml,player[0]):
			board(ml)
			print("win user")
			flag = False
			break
		computer_step(comp)
		if who_win(ml,player[1]):
			board(ml)
			print("comp win")
			flag = False
			break
		board(ml)

elif int(num) == 1:
	player = check_two_player1()
	player2 = check_two_player2(player)
	board(ml)
	flag = True
	while flag:
		steps_of_players(player)
		if who_win(ml,player):
			board(ml)
			print("player user")
			flag = False
			break
		board(ml)
		steps_of_players(player2)
		if who_win(ml,player2):
			board(ml)
			print("player2 user")
			flag = False
			break
		board(ml)
else:
	print("read attention")
