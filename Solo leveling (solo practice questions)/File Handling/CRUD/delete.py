import json
fileName = "students.json"
def delete(id):
    with open(fileName, "r+") as file:
        data = json.loads(file.read())
        student_data = list(filter(lambda x: x['id'] == id, data))
        if student_data:
            data.remove(student_data[0])
            file.seek(0)
            json_data = json.dumps(data)
            file.write(json_data)
        else:
            print("Invalid student id")
    choice = input("Do you still wish to comtinue? (y/n)")

    return True if choice.lower() == "y" else False
