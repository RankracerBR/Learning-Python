X,Y=list(map(int,input().split()))
if(X == 1):
    price  = (float) (4.00 * Y)
elif(X == 2):
    price  = (float) (4.50 * Y)
elif(X == 3):
    price  = (float) (5.00 * Y)
elif (X == 4):
    price  = (float) (2.00 * Y)
elif (X == 5):
    price  = (float) (1.50 * Y)
print(f"Total: R$ {price:.2f}")


#X,Y = map(int,input().split())
#Item = {1:4.0,2:4.5,3:5.0,4:2.0,5:1.5}
#X = float(Item[X])*Y
p#rint(f"Total: R$ {X:.2f}")
