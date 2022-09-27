def CheckIfWeekend(int: day):
    if day // 6 < 1:  
        return False
    else:
        return True


day = int(input())

CheckIfWeekend(day)