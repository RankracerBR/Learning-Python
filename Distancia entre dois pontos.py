import math

l1 = input().split(" ")
l2 = input().split(" ")

x1,y1 = l1
x2,y2 = l2

distancia = math.sqrt(((float(x2) - float(x1))*(float(x2) - float(x1))) + ((float(y2)-float(y1)) *(float(y2)-float(y1))))

print("%0.4f" %distancia)