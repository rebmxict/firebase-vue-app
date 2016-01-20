import subprocess
import shlex
from numpy import random

start_day = "2016 1 5"
end_day = "2017 12 24"

# start_day = "2018 4 9"
# end_day = "2018 10 11"

# start_day = "2018 10 11"
# end_day = "2019 7 12"

def isLeapYear(year):
    if year % 4 == 0:
        return True
    else:
        return False

x = random.randint(0, 31, size=50)
test = {}

monthSize = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

monthKey = {
        1: 1,
        2: 4,
        3: 4,
        4: 0,
        5: 2,
        6: 5,
        7: 0,
        8: 3,
        9: 6,
        10: 1,
        11: 4,
        12: 6
    }

def determine_day_of_week(year, month, day):
    step = int(str(year)[2:]) // 4
    step += day
    step += monthKey.get(month)
    if isLeapYear(year) and month < 3:
        step -= 1
    step += 6
    step += int(str(year)[2:])
    step = step % 7
    return step

def getMonthSize(year, month):
    day = monthSize.get(month)
    if month == 2:
        if isLeapYear(year):
            day += 1
    return day

def preSetGit(year, month, day):
    global x
    if determine_day_of_week(year, month, day + 1) == 1:
        return
    else:
        if day + 1 not in x:
            setGit(year, month, day + 1)
        else:
            return

def doSome(year, start_month, start_day, end_month, end_day):
    global x
    day = getMonthSize(year, start_month)
    x = random.randint(0, 31, size=50)
    for i in range(start_day, day + 1):
        preSetGit(year, start_month, i - 1)
    for month in range(start_month + 1, end_month):
        day = getMonthSize(year, month)
        x = random.randint(0, 31, size=50)
        for i in range(day):
            preSetGit(year, month, i)

    x = random.randint(0, 31, size=50)
    for i in range(1, end_day + 1):
        preSetGit(year, end_month, i - 1)

def setGit(year, month, day):
    f = open("./commits.txt", "a")
    f.write("Now the file has more content!")
    global test
    date = str(year) + ' ' + str(month) + ' ' + str(day)
    if test.get(date) == None:
        test.update({date: 1})
    else:
        test.update({date: test.get(date) + 1})
    month_str = str(month)
    if month <= 9:
        month_str = "0" + month_str
    day_str = str(day)
    if day <= 9:
        day_str = "0" + str(day)
    time_1 = random.randint(10, 18)
    time_2 = random.randint(10, 60)
    time = str(time_1) + str(time_2)
    shlex_str = "sudo date -u " + month_str + day_str + time + str(year)[2:]
    print(shlex_str)
    subprocess.call(shlex.split(shlex_str))
    subprocess.call(shlex.split("git add ."))
    subprocess.call(shlex.split("git commit -m 'commits'"))


start_day = start_day.split()
end_day = end_day.split()
day_of_week = determine_day_of_week(int(start_day[0]), int(start_day[1]), int(start_day[2]))

doSome(int(start_day[0]), int(start_day[1]), int(start_day[2]), 12, 30)
for year in range(int(start_day[0]) + 1, int(end_day[0])):
    doSome(year, 1, 4, 12, 28)
doSome(int(end_day[0]), 1, 18, int(end_day[1]), int(end_day[2]))

#subprocess.call(shlex.split("git push -u origin master"))
print(test)
print(len(test))