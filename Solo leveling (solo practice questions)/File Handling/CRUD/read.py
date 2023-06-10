import json

def read(student_id): #student_id is the id we got from user from main.py
    with open("students.json", "r") as file:
        data = file.read()
        data = json.loads(data)
        student_data = list(filter(lambda x: x["id"] == student_id, data))
        #this filters out all the data in "data" where the value of key
        #  of the dictionary is equal to student_id(user input)

        if student_data: #if student_data exists (not empty/ null) then print that data 
            print(student_data[0])
        else:
            print("Invalid data")
        choice = input("Do you still wish to continue? (y/n)")  
        return True if choice.lower() == "y" else False