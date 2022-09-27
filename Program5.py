import math

def Distance(A, B):
    return math.sqrt(pow(A[0] - B[0], 2) + pow(A[1] - B[1], 2))

A = [3, 6]
B = [2, 1]
print(f'Distance between point A{A} and point B{B} is ', str((Distance(A, B)))[:4])

A = [7, -5]
B = [1, -1]
print(f'Distance between point A{A} and point B{B} is ', str((Distance(A, B)))[:4])