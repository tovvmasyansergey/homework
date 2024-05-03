import os
import argparse
"""
This file is soted all files and create directory by sorted and replace files in directories
Create by: Sergey Tovmasyan
Date: 30 april 2024
"""

def get_arguments():

    """
    Function: get_arguments
    Brief: The functions is input our path of files or directory
    Params: path : name of path
    Return: return path of file
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path', required=True, help="This is a input path")
    args = parser.parse_args()
    path = args.path
    return path


def get_files(path):
#path = os.getcwd()

    """
    Function: get_files
    Brief: The functions is sorted all files by type in dictinary
    Params: path : path of file or directory
    Return: return dictinary of files
    """

    dict_file = {}
    dict_file["other_files"] = []
    list_file = os.listdir(path = path)
    for line in list_file:
        if os.path.isfile(line) and "." in line:
            extension = line[line.rfind("."):]
            if extension in dict_file:
                dict_file[extension].append(line)
            else:
                dict_file[extension] = [line]
        elif os.path.isfile(line):
            dict_file["other_files"].append(line)
    return dict_file


def create_directory(dict_file,path):

    """
    Function: create_directory
    Brief: The functions is create directory and replace file by type
    Params: path : name of paty and dictinary of files
    Return: return nothing
    """


    for key in dict_file:
        if key != "other_files":
            p = os.path.join(path,key[1:])
            os.makedirs(p,exist_ok = True)
            for file_name in dict_file[key]:
                path1 = os.path.join(path,file_name)
                path2 = os.path.join(p,file_name)
                os.replace(path1,path2)
        else:
            p = os.path.join(path,key)
            os.makedirs(p, exist_ok = True)
            for file_name in dict_file[key]:
                path1 = os.path.join(path,file_name)
                path2 = os.path.join(p,file_name)
                os.replace(path1,path2)
def main():
    """
    Function: main
    Brief: main function
    """
    path = get_arguments()
    dict_files = get_files(path)
    create_directory(dict_files,path)
if __name__ == "__main__":
	main()

