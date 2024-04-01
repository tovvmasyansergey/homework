import argparse
import xlsxwriter
def get_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("-f","--filename",required = True,help = "help me")
	parser.add_argument("-x","--xlsxfile",required = True,help = "help me")
	parser.add_argument("-p","--profession",help = "help me")
	args = parser.parse_args()
	file_name = args.filename
	xlsx_file = args.xlsxfile
	prof = args.profession
	return file_name,xlsx_file,prof
def open_file(file):
	with open(file) as f:
		return f.readlines()
def get_inform(ml):
	ml1 = []
	for i in ml:
		ml1.append(i)
	return ml1
def write_in_xlsx(cnt,file,profession):
	workbook = xlsxwriter.Workbook(file)
	worksheet = workbook.add_worksheet("Sheet")
	worksheet1 = workbook.add_worksheet("Sheet1")
	bold_green_format = workbook.add_format({'bg_color' : 'green','bold': True})
	yellow_format = workbook.add_format({'bg_color' : 'yellow'})
	for row, i in enumerate(cnt):
		ml = i.strip().split()
		for col,m in enumerate(ml):
			worksheet.write(row,col,m)
			if row == 0:
				worksheet.write(row,col,m,bold_green_format)
			elif int(ml[2]) > 35:
				worksheet.write(row,col,m,yellow_format)
			elif ml[-2] == profession:
				worksheet1.write(row,col,m)
			else:
				worksheet.write(row,col,m)
	workbook.close()
filename,xlxsfile,profesion = get_arguments()
cnt = open_file(filename)
write_in_xlsx(cnt,xlxsfile,profesion)












