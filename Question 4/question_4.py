inputted_file = open("classesinput.txt", "r")
file_contents = inputted_file.readlines()
num_courses = int(file_contents[0])
print(num_courses)
x = 1

class Courses:
    def __init__(self, x):
        self.course_department = file_contents[1 * x]
        self.course_number = file_contents[2 * x]
        self.course_name = file_contents[3 * x]
        self.course_credits = file_contents[4 * x]
        self.lecture_days = file_contents[5 * x]
        self.start_time = file_contents[6 * x]
        self.end_time = file_contents[7 * x]
        self.average_grade = file_contents[8 * x]
    
    def output(self):
        print("Course %d: %s: %s" %  (x, self.course_number, self.course_name))
        print("Number of credits: " + self.course_credits)
        print("Days of Lectures: " + self.lecture_days)
        print("Stat: on average, students get %d% in this course" % (self.average_grade))

all_courses = [Courses(x) for x in range(num_courses)]

print(all_courses)

