#WRITE A PROGRAM TO CREATE AREA CALCULATOR
print(""" press 1 to get area of square , press 2 to get area of rectangle, press 3 to get area of circle, press 4 to get area of trinagle""" )
choice=int(input("Enter a number between 1-4:"))
if choice==1:
    side=float(input("Enter a length of one side"))
    area=side**2
    print("the area of square is:",area)
elif choice==2:
    length=float(input("Enter the length of rectangle"))
    width=float(input("Enter a width of one rectangle"))
    area=length*width
    print("the area of rectangle is:",area)
elif choice==3:
    radius=float(input("Enter a radius of circle"))
    area=((22/7)*(radius**2))
    print("the area of circle is",area)
elif choice==4:
    base=float(input("Enter a base of traingle"))
    height=float(input("Enter a height of triangle"))
    area=0.5*base*height
    print("the area of triangle is:",area)
