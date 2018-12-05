import json
import os

global database

def loadJsonFile():
	flag = os.path.isfile("D:\\untitled1\\Include\\database.json")
	if flag == True:
		with open ('database.json', 'r') as f:
			for line in f:
				database = json.loads(line)
	elif flag == False:
		database = {}
	return database


def saveJsonFile(data:dict):#save dict to json
	with open('database.json','w') as outfile:
		json.dump(data,outfile,ensure_ascii=False)
		outfile.write('\n')


def main(database:dict):
	while True:
		print(' STAFF INFO DATABASE\n'
		      '=====================\n'
		      '1.ADD Staff INFO\n'
		      '2.DELETE Staff INFO\n'
		      '3.UPDATE Staff INFO\n'
		      '4.Find Staff INFO\n'
		      '5.Show\n'
		      '6.Quit')
		Select = input('Please enter the serial number')
		if Select.isdigit():
			Select =int(Select)
			if Select > 6:
				print('Please enter number smaller than 6')
		if   Select == 1:  # add
			addStaffInfo()
		elif Select == 2:
			staffInfo = input ('Please enter the staff Name')
			deleteStaffInfo (database, staffInfo)
		elif Select == 3:
			staffInfo = input ('Please enter the staff Name')
			updateStaffInfo(database,staffInfo)
		elif Select == 4:
			staffInfo = input ('Please enter the staff Name')
			findStaffInfo(database,staffInfo)
		elif Select == 5:
			if database:
				print(database)
			else:
				print('No data, need to write')
		elif Select == 6:
			print('Goodbye')
			break


def addStaffInfo():
	NewStaffInfo_input =input('please enter staff info:Name/Job/Birthday')
	newStaffInfoList = NewStaffInfo_input.split('/')
	if  newStaffInfoList[0] in database:
		print('The Name already exists，please enter agian')
	else:
		if  len(newStaffInfoList) != 3:
			print('Please input right type string:Job/Birthday EXM:IT/1997-01-01')
		else:
			database[newStaffInfoList[0]] = {'Job': newStaffInfoList[1], 'Birthday': newStaffInfoList[2]}
			print('Add Successful')
			saveJsonFile(database)


def deleteStaffInfo(database:dict,staffInfo:str):
	if len(database) == 0:
		print('No data, need to write')
	else:
		if staffInfo in database:
			del database[staffInfo]
			print('Delete success')
			saveJsonFile(database)
		else:
			print('Library does not have this people')


def findStaffInfo(database:dict,staffInfo:str):
	if len (database) == 0:
		print ('No data, need to write')
	else:
		if staffInfo not in database:
			print('This person is not in library')
		else:
			print(database[staffInfo])


def updateStaffInfo(database:dict,staffInfo:str):
	if len(database) == 0:
		print('No data, need to write')
	else:
		if staffInfo not in database:
			print('This person is not in library')
		else:
			changeInfo_input = input('please input you want change info EXM:QA/1990-01-01')
			changeInfo =changeInfo_input.split('/')
			if len(changeInfo) != 2:
				print('Please input right type string:Job/Birthday EXM:QA/1990-01-01')
			else:
				database[staffInfo] ={'Job':changeInfo[0],'Biryhday':changeInfo[1]}
				print('Update Success')
				saveJsonFile(database)

if __name__ =="__main__":
	database = loadJsonFile()
	main(database)