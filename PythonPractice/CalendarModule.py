import calendar

date=list(map(int,input().split()))#formato mm dd yyyy
day=calendar.weekday(date[2],date[0], date[1])
code={"0":"MONDAY","1":"TUESDAY", "2":"WEDNESDAY", "3":"THURSDAY", "4":"FRIDAY", "5":"SATURDAY", "6":"SUNDAY"}

print(code[str(day)])
