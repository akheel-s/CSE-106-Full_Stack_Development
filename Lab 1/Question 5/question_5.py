import json
def create(dict):
    student_name = input("Enter the student's name: ")
    if student_name in dict:
        print("Error: The name already exists")
    else:
        grade = int(input("Enter the grade: "))
        dict[student_name] = grade
        dump(dict)

def fetch_grade(dict):
    student_name = input("Enter the student's name: ")
    if student_name in dict:
        print("%s's grade is %d" %(student_name, dict[student_name]))
    else:
        print("Name does not exist in dictionary.")


def edit_grade(dict):
    student_name = input("Enter the student's name: ")
    if student_name in dict:
        grade = int(input("Enter the new grade: "))
        dict[student_name] = grade
        dump(dict)
    else:
        print("Name does not exist try creating the student first.")

def delete_grade(dict):
    student_name = input("Enter the student's name: ")
    if student_name in dict:
        dict[student_name] = None
        dump(dict)
    else:
        print("Name not in dictionary, nothing to delete.")


def dump(dict):
    with open("grades.txt", "w") as outfile:
        json.dump(dict, outfile)

dict = {}
with open('grades.txt', 'r') as file:
    dict = json.load(file)

x = 0

while x == 0:
    print("a. Create a student and grade")
    print("b. Find student's grade from name")
    print("c. Edit Grade")    
    print("d. Delete Grade")
    print("e. Quit")
    option = input("Enter your choice:")
    
    if option == "a":
        create(dict)
    elif option == "b":
        fetch_grade(dict) 
    elif option == "c":
        edit_grade(dict)
    elif option == "d":
        delete_grade(dict)
    elif option == "e":
        break
    else:
        print("Choose between options a-e")