import xlrd as x
from matplotlib import pyplot as mpl
import numpy as np
 
loc = "USvideos.xls"

def time(row):
	wb = x.open_workbook(loc)
	sheet = wb.sheet_by_index(0)
	sheet.cell_value(0, 0)

	num = str(sheet.cell_value(row, 5))
	if len(num) == 24:
		return(num[11:13])
	else:
		num = 0
		return(num)

def views(row):
	wb = x.open_workbook(loc)
	sheet = wb.sheet_by_index(0)
	sheet.cell_value(0, 0)

	num = str(sheet.cell_value(row, 7))
	
	if len(num) <= 9 and len(num) >= 2:
		return(num)
	else:
		num = 0
		return(num)

timenum = [0]
for i in range(1, 80):
	timenum.append(time(i))

viewsnum = [0]
for i in range(1, 80):
	viewsnum.append(views(i))

print(timenum)
print(viewsnum)
mpl.scatter(timenum, viewsnum)
mpl.xlabel("time (military time)")
mpl.ylabel("views")
mpl.show()