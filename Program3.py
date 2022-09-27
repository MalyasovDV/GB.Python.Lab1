def WhichQuadrant(x, y):
    if(x > 0):
        if(y > 0):
            return 1
        else:
            return 4
    else:
        if(y > 0):
            return 2
        else:
            return 3

x = 34
y = -30
print(f'point ({x};{y}) is in quadrant {WhichQuadrant(x,y)}')

x = 2
y = 4
print(f'point ({x};{y}) is in quadrant {WhichQuadrant(x,y)}')

x = -34
y = -30
print(f'point ({x};{y}) is in quadrant {WhichQuadrant(x,y)}')