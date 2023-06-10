from create import create
from read import read
from update import update
from delete import delete

def inquiry():
    selection = input("Enter Your Choice C/R/U/D: ")
    selection = selection.lower()
    def exit_msg():
        print("Thank you for your choice")
    if selection == "c":
        Continue = create()
    #if code from create.py returns true then continue is executed

        inquiry() if Continue else exit_msg()
        #else the exit_msg is displayed

    elif selection == "r": #THis code will only read a specific json data, data with id given by user
        id = input("Enter desired id: ")
        Continue = read(id)

        inquiry() if Continue else exit_msg()


    elif selection == "u":
        # Ask for the id and attribute to change

        id = input("Enter id that should be updated: ")
        to_change= input("Enter the key whose value you want to change: ")

            # Check if the to_change attribute is valid

        if to_change in ["name", "age"]:
         #This is the same as if to_change == "name" or to_change == "age":
            
            changed = input(f"What should the new {to_change} be? ")
            Continue = update(id, to_change, changed)

            # Call the update function with the provided values
        else:
            print("Invalid key")

        inquiry() if Continue else exit_msg()

        
    elif selection == "d":
        id = input("Enter the id that you wish to delete: ")
        Continue = delete(id)

        inquiry() if Continue else exit_msg()
    else:
        print("Invalid request")


if __name__ == "__main__":
    inquiry()

