def create() :
    id = input("Enter student id ")
    name = input("Enter student name
    age = input ("Enter
    student age")
    data = dict(id=id, name=name, age=age)
    if not os.path.exists (filemame):
        with open(filename, "W") as fp:
            json_obj = json. dumps ([data], indent=2)
            fp.write (json_obj)
    else:
        pass
