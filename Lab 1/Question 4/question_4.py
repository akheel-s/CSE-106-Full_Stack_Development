inputted_file = open("classesinput.txt", "r")
file_contents = inputted_file.readlines()
num_courses = int(file_contents[0])
print(num_courses)

class Courses():
    def __init__(self, i):
        a = 1
        b = 2
        c = 3
        d = 4
        e = 5
        f = 6
        g = 7
        h = 8
        
        a += 8*i
        self.course_department = file_contents[a]
        b += 8*i
        self.course_number = file_contents[b]
        c += 8*i
        self.course_name = file_contents[c]
        d += 8*i
        self.course_credits = file_contents[d]
        e += 8*i
        self.lecture_days = file_contents[e]
        f += 8*i
        self.start_time = file_contents[f]
        g += 8*i
        self.end_time = file_contents[g]
        h += 8*i
        self.average_grade = file_contents[h]
  
objects = []
for i in range(num_courses):
    objects.append(Courses(i))

print(type(objects[1].course_number))

def output():
    # output_file = open("test2.txt", "w")
    for i in range(len(objects)):
        output_file = open("test.txt", "a")

        str1 = ("Course %s: %s %s %s" %  (i+1, objects[i].course_department, objects[i].course_number, objects[i].course_name))
        str2 = ("Number of credits: " + objects[i].course_credits)
        str3 = ("Days of Lectures: " + objects[i].lecture_days)
        str4 = ("Stat: on average, students get %s in this course \n" % (objects[i].average_grade))
        output_file.write(str1)
        output_file.write(str2)
        output_file.write(str3)
        output_file.write(str4)

output()
print(objects[1].start_time)
