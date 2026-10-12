square_area=lambda a:a**2
rectangle_area=lambda l,b:l*b
traingle_area=lambda ba,h:0.5*ba*h

a=int(input("Enter the side length of Square:"))
print("Area of the square :",square_area(a))

l=int(input("Enter the length:"))
b=int(input("Enter the breadth:"))
print("Area of  Rectangle:",rectangle_area(l,b))

ba=int(input("Enter the base:"))
h=int(input("Enter the heigth:"))
print("Area of the Traingle:",traingle_area(ba,h))
