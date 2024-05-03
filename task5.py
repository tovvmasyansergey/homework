import argparse

"""
This file is for count of words:
Create by: Sergey Tovmasyan
Date: 29.04.2024
"""

def get_arguments():
    """
    Function: get_arguments()
    Brief: The function for input file name and count of numbers for print
    Params: file: file name of text,number: how words is print
    Return: return filename and number
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help="This is a input file option")
    parser.add_argument('-n', '--number', default= 10, help="The number of list of words")
    args = parser.parse_args()
    filename = args.file
    numb = args.number
    return filename, numb


def open_file(filename):
    """
    Function: open_file
    Brief: Tthe function open the file and read text
    Params: filename of file with text
    Return: returns the list of sentensies
    """

    with open(filename) as ffile:
        return ffile.readlines()

def take_words(cnt):
    list_of_line = []
    for word in cnt:
        for letter in word:
            if not letter.isalpha() and letter != " " and letter != "-":
                word = word.replace(letter,"")
        list_of_line.append(word)
    list_of_word = []
    for line in list_of_line:
        words = line.split()
        for word in words:
                list_of_word.append(word)
    list_of_words = []
    for ind_word in range(len(list_of_word)):
        word = ""
        if list_of_word[ind_word][-1] == "-":
                word = list_of_word[ind_word][:ind_word - 1] + list_of_word[ind_word + 1]
                list_of_words.append(word)
        else:
                list_of_words.append(list_of_word[ind_word])
    return list_of_words



def sorted_dict(words,numb):
    """
    Function: sorted_dict
    Brief: The function create dictinary and words add in dictainary,and sorted dictinary
    Params: dc_words list of words,numb our number for print
    Return: no return,its print
    """

    numbs = int(numb)
    dict_words = {}
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:dict_words[word] = 1
    new_dc = dict(sorted(dict_words.items(),key = lambda item: item[1],reverse=True))
    for i,value in new_dc.items():
        print(new_dc[i],i)
        numbs -= 1
        if numbs == 0:
            break


def main():
    """
    Function: main
    Brief: print result
    """
    fname,numb = get_arguments()
    cnt = open_file(fname)
    content = take_words(cnt)
    sorted_dict(content,numb)
if __name__ == "__main__":
	main()

