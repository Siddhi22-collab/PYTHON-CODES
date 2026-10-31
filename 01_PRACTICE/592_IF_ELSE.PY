marks = int(input("Enter your marks: "))

if marks >= 90 and marks <= 100:
    print("Grade A")

elif marks >= 75 and marks < 90:
    print("Grade B")

elif marks >= 60 and marks < 75:
    print("Grade C")

elif marks >= 35 and marks < 60:
    print("Grade D")

elif marks < 35 and marks >= 0:
    print("Fail")

else:
    print("Invalid Marks")