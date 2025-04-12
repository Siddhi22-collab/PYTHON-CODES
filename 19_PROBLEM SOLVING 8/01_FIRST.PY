#CONVERT THE FOLLOWING DICTIONARY INTO JSON FORMAT
import json
Student_data={"name": "David","age": 13,"marks": 87}
data= json.dumps(Student_data)
print(data)
print(type(data))