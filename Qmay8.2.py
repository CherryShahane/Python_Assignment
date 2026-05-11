'''2)	WAP to print Square, Cube and Square Root of all numbers from 1 to N'''
import math
n=int(input("enter the number"))
square=0
cube=0
for i in range(1,n+1):
    square=i*i
    cube=i*i*i
    square_root=math.sqrt(i)
    print("square",i,square,end=" ")
    print( )
    print("cube",i,cube,end=" ")
    print()
    print("square root",i,square_root,end=" ")
    print()

