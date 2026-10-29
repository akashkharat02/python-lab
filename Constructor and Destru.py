class Student:
    def __init__(self):
        print("Constructor is called")
        print("Object is created")

    def __del__(self):
        print("Destructor is called")
        print("Object is destroyed")


s = Student()

print("Program is running")