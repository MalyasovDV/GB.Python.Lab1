def FirstExpression(x, y, z):
    return not(x or y or z)

def SecondExpression(x, y, z):
    return (not x) and (not y) and (not z)

def CheckIfBoolEquivalent(a, b):
    if a == b:
        return True
    else:
        return False


Variables = [False, True]
print('x  y  z  FE SE')
for x in Variables:
    for y in Variables:
      for z in Variables:
           print(int(x), '', int(y), '', int(z), '', int(FirstExpression(x, y, z)), '', int(SecondExpression(x, y, z)),'' , CheckIfBoolEquivalent(FirstExpression(x, y, z), SecondExpression(x, y, z)))

#for x in Variables:
#    if (x):
#        print(f'int({x})')
#    else:
#        print()