import argparse
import random
"""
This file is game by words
Create by: Sergey Tovmasyan
Date: 29.04.2024
"""

def questions_answers():
    """
    Function: questions_answers
    Brief: The functions random choose question with answers
    Params: only list of questions and answers
    Return: returns random choice question and answer
    """

    list_quest = ["what is the capital of england:london",
                   "what is the capital of france:paris",
                    "what is the capital of usa:new york"]
    random_word = random.choice(list_quest)
    return random_word


def input_letter(line):
    """
    Function: input_letter
    Brief: The functions is input letter and examination that his letter in word if in word continue
    Params: line of question and answer
    Return: return sucess or no sucees if you win
    """

    word = line[line.index(":")+1:]
    word1 = len(word)*"_"
    count = 0
    while word != word1:
        letter = input("Please input letter: ")
        if letter.lower() not in word:
            count+=1
        if count == 3:
            break
        else:
            for i in range(len(word)):
                if letter == word[i]:
                    word1 = word1[:i] + letter + word1[i+1:]
        print(word1)
    if word == word1:
        print("sucess!!!")
    elif count == 3:
        print("no sucess")

def main():
    """
    Function: main
    Brief: print result
    """
    cnt = questions_answers()
    print(cnt[:cnt.index(":")])
    input_letter(cnt)
if __name__ == "__main__":
        main()
