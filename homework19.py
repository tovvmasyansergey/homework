import os
import argparse
def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--filename",required = True,help = "help me")
	args = parser.parse_args()
	file_name = args.filename
	return file_name
def open_file(name):
	with open(name) as f:
		return f.readlines()
def check_directory(file):
	ml = []
	for dirs in file:
#		cwd = os.getcwd()
#		path = cwd + "/" + dirs
		if os.path.isdir(dirs.strip()):
			ml.append(dirs)
	return ml
def write_file(file):
	with open("file_of_dir_19.txt","w") as f:
		for i in file:
			f.write(i + "\n") 
filename = get_arguments()
cnt = open_file(filename)
list_dir = check_directory(cnt)
write_file(list_dir)

