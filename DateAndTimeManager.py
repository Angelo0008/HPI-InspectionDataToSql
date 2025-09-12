from Imports import *

dateToday = ""
timeNow = ""
monthNowText = ""

yearNow = ""

dateToRead = "2024/11/11"
dateToReadDashFormat = "2024-11-11"

def GetDateToday():
    global dateToday
    global monthNowText
    global monthNow
    global yearNow

    dateToday = datetime.datetime.today()
    monthNowText = dateToday.strftime("%B")
    monthNow = int(dateToday.month)
    yearNow = int(dateToday.year)
    dateToday = dateToday.strftime('%Y/%m/%d')

def GetTimeNow():
    global timeNow

    timeNow = datetime.datetime.today()
    timeNow = timeNow.strftime('%H:%M')

def GetCurrentDateTime():
    """Returns current date and time in format YYYY-MM-DD HH:MM:SS"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')