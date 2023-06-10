import json
def update(id, to_change, changed):
    with open("students.json", "r+") as file:
        data = json.loads(file.read())
        # Filter the list of students by the given id

        student_data = list(filter(lambda x: x['id'] == id, data))
        if student_data:
             # If a student with the given id is found
            # Get the index of the student in the list
            index = data.index(student_data[0])
        #mini .index() concept
        # list = [w, x, y, z]
        # index = list.index(y) //The result (index) is 2
            data[index][to_change] = changed

            #MINI OUTPUT EXAMPLE, look at the code above and this comment simultaneously
            #data = [{id: 1 , name: ''},{id: 2 , name: ''},{id: 3 , name: ''}]
            #say user input is 3 then, student_data will be [{id: 3 , name: ''}]
            #  i.e the last dict INSIDE a list
            #since student_data is still inside a list, indexing 0 or student_data[0] must 
            # be done to just get dictionary
            # the index = data.index(student_data[0]) will give us the index of student_data in the overall data
            # i.e in this pseudo code 2
            #then say to_change is name
            # data[index][to_change] = changed is data[2]["name"] = "prakash"
            # now the updated data is
            #data = [{id: 1 , name: ''},{id: 2 , name: ''},{id: 3 , name: 'prakash'}]




            file.seek(0)

            # Now we move the pointer back to the beginning and overwrite every value 

            file.write(json.dumps(data, indent = 2))
            print("File has been updated successfully !")
        else:
            print("Invalid student id")
    choice = input("Do you still wish to continue? (y/n)")
    return True if choice.lower() == "y" else False


