def CheckIfWeekend(day):
    if day // 6 < 1:  
        return False
    else:
        return True


day = 6

if CheckIfWeekend(day):
    print(day + " Yes")
else:
    print(day + " No")

day = 7

if CheckIfWeekend(day):
    print(day + " Yes")
else:
    print(day + " No")

day = 1

if CheckIfWeekend(day):
    print(day + " Yes")
else:
    print(day + " No")