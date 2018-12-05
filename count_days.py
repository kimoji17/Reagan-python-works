import datetime
import time
import calendar


def input_check(timeStr):
    Birthday = datetime.datetime.strptime(timeStr, '%Y-%m-%d')
    if Birthday >= datetime.datetime.now():
        print('Are you kidding me?')
        exit()
    else:
        print('Aha,you are still alive')


def is_valid_date(timeStr):
    try:
        datetime.datetime.strptime(timeStr, "%Y-%m-%d")
        return True
    except:
        return False

def is_valid_datetime(timeStr):
    try:
        datetime.datetime.strptime(timeStr, "%Y-%m-%d %H:%M:%S %f")
        return True
    except:
        return False

def compareTime(timestr1:datetime,timestr2:datetime):
    # d1 = datetime.datetime.strptime(timestr1,'%Y-%m-%d %H:%M:%S')
    # d2 = datetime.datetime.strptime(timestr2,'%Y-%m-%d %H:%M:%S')
    delta = timestr1 - timestr2
    return delta.days


def liveTo75(birthday:datetime,today:datetime):
    delta = datetime.timedelta(days=27393)
    birthday = birthday + delta
    time_range = birthday - today
    return time_range.days


def getTodayStr():
    todayStr = datetime.date.today()
    print(todayStr)
    return todayStr


def getYestodayStr():
    yesterdayStr = (datetime.date.today () - datetime.timedelta (days=1)).strftime('%Y-%m-%d')
    print(yesterdayStr)
    return yesterdayStr


def strConvertTimestamp(timestr:str):
    Time = time.strptime(timestr,"%Y-%m-%d %H:%M:%S %z")
    timestamp = time.mktime(Time)
    return timestamp


def convertUTC(timestr:str):
	# UTCtime = datetime.datetime.fromtimestamp(timestamp)
    Time = datetime.datetime.strptime(timestr, "%Y-%m-%d %H:%M:%S %z")
    UTCtime = datetime.datetime.timetuple(Time)
    print(UTCtime)
    print(type(UTCtime))
    UTC_dt = datetime.datetime.fromtimestamp(time.mktime(UTCtime), None)
    return UTC_dt


def timestampConvertStr(timestamp):
    time_local = time.localtime(timestamp)
    timestr = datetime.datetime.strftime(time_local,"%Y-%m-%d %H:%M:%S %z")
    return timestr


def getFirstDayAndLastDay():
	year = datetime.datetime.today().year
	month = datetime.datetime.today().month
	if year:
		year = int (year)
	else:
		year = datetime.date.today ().year
	if month:
		month = int (month)
	else:
		month = datetime.date.today ().month
	firstDay = datetime.date(year = year, month = month, day = 1)
	firstDayWeekDay,monthrange = calendar.monthrange(year,month)
	lastDay = datetime.date(year = year,month = month,day= monthrange)
	return firstDay,lastDay


def timeToStr(time:tuple):
	outPutTimeStr0 = datetime.datetime.strftime(time[0], '%Y-%m-%d')
	outPutTimeStr1 = datetime.datetime.strftime(time[1], '%Y-%m-%d')
	return outPutTimeStr0,outPutTimeStr1


if __name__ == '__main__':

    input('Can you provide your birthday：exm 1990-08-08')
    Birthday = input()
    is_valid_date(Birthday)
    input_check(Birthday)
    today = datetime.datetime.today()
    userBirthday =datetime.datetime.strptime(Birthday,'%Y-%m-%d')
    print(userBirthday)
    timeToBirthday = compareTime(today,userBirthday)
    print('You are already alive {} days'.format(timeToBirthday))
    print('If you want to live to 75, you still need {} days'.format(liveTo75(userBirthday,today)))
    input('please input a time')
    usersInputTime = input()
    is_valid_datetime(usersInputTime)
    print(strConvertTimestamp(usersInputTime))
    print(convertUTC(usersInputTime))
    print(timeToStr(getFirstDayAndLastDay()))


