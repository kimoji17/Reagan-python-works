import os
import json


global userNeedInfoTuple

USERCASH                                      =1
USERHOUSEAREA                                 =2
BUYCARORNOT                                   =3
BUYCARMONEY                                   =4
LOANORNOT                                     =5
LOANMONEY                                     =6

path = "D:\\untitled1\\Include\\argPrice.json"

def load_JsonFile(path:str):
	flag = os.path.exists(path)
	if flag:
		with open(path, 'r') as f:
			for line in f:
				price = json.loads(line)
	else:
		price = {}
	return price


def get_input(flag):
	if flag == USERCASH:
		deposit = input('How many your cash,please enter number exm:2000000')
		print(deposit)
	elif flag == USERHOUSEAREA:
		houseArea = input ("How big do you want to buy a house?please enter number exm:100")
		print(houseArea)
	elif flag == BUYCARORNOT:
		carflag = input ('Do you want buy car?please enter Y or N')
		print(carflag)
	elif flag == BUYCARMONEY:
		buyCarMoney = input ('Please enter buy car money. if you not buy,please enter 0')
		print(buyCarMoney)
	elif flag == LOANORNOT:
		loanFlag = input ('Do you want loan? please enter Y or N')
		print(loanFlag)
	elif flag == LOANMONEY:
		monthlyRevenue = input('How much your or you and your couple month revence,if you not buy,please enter 0')
		print(monthlyRevenue)

def input_info():
	while True:
		print (
			'Please input these Info\n'
			'1.Your cash\n'
			'2.You want buy house area\n'
			'3.Buy car or not\n'
			'4.Buy car money\n'
			'5.Loan or not\n'
			'6.Loan Money\n'
		)
		serialNumber = input ('Please enter the serial number of the info you want to enter first.')
		if is_number (serialNumber) == True:
			serialNumber = int (serialNumber)
			if serialNumber > 6:
				print ('please enter the right serial number')
			elif serialNumber < 1:
				print ('please enter the number bigger than 1')
			else:
				flag = serialNumber

	return flag

def is_number(number):
	try:
		int_a = int (number)
		print(int_a)
		if int_a < 1:
			return False
		else:
			return True
	except ValueError:
		print ('str_a cannot be converted to integer')
	return False


def get_users_deposit_houseArea():
	while True:
		deposit = input("How many your money,please enter number exm:2000000")
		if is_number(deposit) == True:
			deposit = int(deposit)
			houseArea = input ("How big do you want to buy a house?please enter number exm:100")
			is_number (houseArea)
			if is_number (houseArea) == True:
				houseArea = int (houseArea)
				return deposit, houseArea
			break
		else:
			continue


def loan_or_not():
	while True:
		Flag = input('Do you want loan? please enter Y or N')
		if Flag =='Y' or Flag == 'y':
			loanflag = True
			break
		elif Flag =='N' or Flag == 'n':
			loanflag = False
			break
		else:
			print('please enter Y or N')
	return loanflag


def month_revenue():
	monthRevenue= input('How much your or you and your couple month revence')
	if is_number(monthRevenue) == True:
		monthRevenue =int(monthRevenue)
	else:
		print ('please enter number')
	return monthRevenue


def buy_car_or_not():
	while True:
		Flag = input('Do you want buy car?please enter Y or N')
		if Flag =='Y' or Flag == 'y':
			carFlag = True
			break
		elif Flag =='N' or Flag == 'n':
			carFlag = False
			break
		else:
			print('please enter Y or N')
	return carFlag


def get_buy_car_money(carFlag:bool):
	if carFlag == True:
		buyCarMoney = input('Please enter buy car money exm:2000000  ')
		if is_number(buyCarMoney) == True:
			buyCarMoney = int(buyCarMoney)
		else:
			print('please enter number')
	else:
		buyCarMoney = 0
	return buyCarMoney


def total_money(loanFlag:bool):
	if loanFlag == True:
		monthMoney = month_revenue()# get month Money
		loanMoney = int(monthMoney) * 30 #get loan money
		userTotalMoney = loanMoney + userNeedInfoTuple[0]
	else:
		userTotalMoney = userNeedInfoTuple[0]
	return userTotalMoney


def main():
	cityDict = load_JsonFile (path)#load house Price Info
	buyCarOrNot = buy_car_or_not ()#get user want buy car result or not
	buyCarMoney = get_buy_car_money (buyCarOrNot)#get car money if flag == false, buyCarMoney = 0
	loanFlag = loan_or_not ()#get user loan or not result
	userTotalMoney = total_money (loanFlag)#get user cash and loan money if loan_flag ==Flase loan money = 0
	if buyCarOrNot ==False:
		for values in cityDict.values ():
			argHouseAndCarMoney = values * userNeedInfoTuple[1] + buyCarMoney
			farHouseAndCarMoney = int (values * 0.5 * userNeedInfoTuple[1]) + buyCarMoney
			cenHouseAndCarMoney = 2 * values * userNeedInfoTuple[1] + buyCarMoney
			bieHouseAndCarMoney = 3 * values * userNeedInfoTuple[1] + buyCarMoney
			if userTotalMoney > farHouseAndCarMoney and userTotalMoney < argHouseAndCarMoney:
				for key in cityDict:
					if cityDict[key] == values:
						print ('you can buy far house in {0} '.format (key))
			elif userTotalMoney > argHouseAndCarMoney and userTotalMoney < cenHouseAndCarMoney:
				for key in cityDict:
					if cityDict[key] == values:
						print ('you can buy near house in {0} '.format (key))
			elif userTotalMoney > cenHouseAndCarMoney and userTotalMoney < bieHouseAndCarMoney:
				for key in cityDict:
					if cityDict[key] == values:
						print ('you can buy cen house in {0} '.format (key))
			elif userTotalMoney > bieHouseAndCarMoney:
				for key in cityDict:
					if cityDict[key] == values:
						print ('you can buy bie house in {0} '.format (key))
	elif buyCarOrNot ==True:
		for values in cityDict.values():
			argHouseAndCarMoney = values * userNeedInfoTuple[1] + buyCarMoney
			farHouseAndCarMoney = int(values *0.5 *userNeedInfoTuple[1]) + buyCarMoney
			cenHouseAndCarMoney = 2 * values * userNeedInfoTuple[1] + buyCarMoney
			bieHouseAndCarMoney = 3 * values * userNeedInfoTuple[1] + buyCarMoney
			if userTotalMoney >farHouseAndCarMoney and userTotalMoney<argHouseAndCarMoney:
				for key in cityDict:
					if cityDict[key] == values:
						print('you can buy far house and car in {0} '.format(key))
			elif userTotalMoney >argHouseAndCarMoney and userTotalMoney<cenHouseAndCarMoney:
				for key in cityDict:
					if cityDict[key] == values:
						print('you can buy near house and car in {0} '.format(key))
			elif userTotalMoney > cenHouseAndCarMoney and userTotalMoney < bieHouseAndCarMoney:
				for key in cityDict:
					if cityDict[key] == values:
						print('you can buy cen house and car in {0} '.format(key))
			elif userTotalMoney>bieHouseAndCarMoney:
				for key in cityDict:
					if cityDict[key] == values:
						print('you can buy bie house and car in {0} '.format(key))


if __name__ =="__main__":

	# userNeedInfoTuple = get_users_deposit_houseArea () #GLOBAL  get user cash and want house area
	# main()
	flag = input_info()
	get_input(flag)




