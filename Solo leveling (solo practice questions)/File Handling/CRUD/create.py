import os
import json
filename = "students.json"

def create():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    data = {"id": id, "name": name, "age": age}
    if not os.path.exists(filename):
    # If the file doesn't exist, create a new file and write the data

        with open(filename, "w") as file:
            json_data = json.dumps([data], indent = 2) 
           # Convert the data into JSON format
            # Putting data inside [] puts the JSON data inside a list
            # Indent makes the JSON file look nicely formatted
            file.write(json_data)
        choice = input("Do you still wish to continue? (y/n)")
        return True if choice.lower() == "y" else False
    else:
        # If the file already exists, read its contents and append the new data

        with open(filename, "r+") as file:
            addData = file.read()
            # Read the JSON data from the file
            addData = json.loads(addData)
            # Convert the JSON data to a Python data type (list)
            addData.append(data)
            # Append the new data to the list

            file.seek(0)
            # Move the file pointer to the beginning
            """
            To write the updated data, it's necessary to move the file pointer back
            to the beginning so that the new data can overwrite the existing content.
            If the file pointer remains at the end, the new data would be appended to the
            existing content instead of replacing it. This can make the json data format incorrect

            Therefore, file.seek(0) is used to move the file pointer to the beginning
            before writing the updated data using file.write(json.dumps(addData, indent=2)).
            This ensures that the new JSON data overwrites the existing content
            from the beginning of the file.

            """

            file.write(json.dumps(addData, indent = 2))

            # Write the updated list back to the file in JSON format
            print("Student added successfuly.")
            choice = input("Do you still wish to continue? (y/n)")
            return True if choice.lower() == "y" else False
            #This entire code returns either true or false



