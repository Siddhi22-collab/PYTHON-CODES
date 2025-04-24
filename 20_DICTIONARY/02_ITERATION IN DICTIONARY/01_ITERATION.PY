Student={"Name":"Siddhi","Age":21,"Gender":"Female"}
#PRINT ALL THE KEY NAMES ONE BY ONE
for x in Student:
    print(x)

#PRINTING ALL THE VALUE NAMES ONE BY ONE
for x in Student:
    print(Student[x])

#USING VALUE FUNCTION
for x in Student.values():
    print(x)

#USING ITEM FUNCTION
for x,y in Student.items():
    print(x,":",y)