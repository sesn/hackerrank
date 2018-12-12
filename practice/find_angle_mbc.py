from math import atan2, degrees
x = int(input())
y = int(input())

print(str(round(degrees(atan2(x,y))))+'°')