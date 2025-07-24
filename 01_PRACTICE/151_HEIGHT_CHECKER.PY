
height = float(input("Enter your height in centimeters: "))
if height < 150:
    print("You are considered Short.")
elif 150 <= height <= 170:
    print("You have Average height.")
elif 170 < height <= 190:
    print("You are Tall.")
else:
    print("You are Very Tall.")
