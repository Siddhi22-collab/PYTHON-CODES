#ACCESS THE VALUE OF AGE FROM THE GIVEN DATA
import json
Student_data={"name": "David","age": 13,"marks": 87}
data=json.dumps(Student_data)
print(data["age"])