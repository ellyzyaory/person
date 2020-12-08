import csv

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def __repr__(self):
        return "% s ,% s" % (self.name,self.address)

courses = {}
grades = {}
average = {}
class Student(Person):
    def __init__(self, name, address, numCourses = 0):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades
        self.average = average

    def addCourseGrade(self, name, course, grade):
        if course not in self.grades and course not in self.courses:
            self.courses.update({name: []})
            self.grades.update({course:[]})
            self.courses[name].append(course)
            self.grades[course].append(grade)
            self.numCourses += 1
        else:
            self.grades[course].append(grade)
        return self.courses, self.grades


    def getAverageGrade(self, name, course):
        total = 0
        for grades in self.grades[course]:
            total += grades
        average = total/len(self.grades[course])
        self.average.update({name:average})
        return self.average

    def printGrades(self):
        return self.courses, self.grades, self.average

    def __repr__(self):
        return "% s ,% s" % (self.name,self.address)

class Teacher(Person):
    def __init__(self, courses, name, address, numCourses = 0):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses

    def addCourse(self, course):
        for i in courses:
            if course not in self.courses[i]:
                self.courses[i].append(course)
                self.numCourses += 1
            else:
                return False
            return self.courses

    def removeCourse(self, course):
        for i in courses:
            if course in self.courses[i] and course > 1:
                self.courses[i].pop(course)
                self.numCourses -= 1
            else:
                return False

    def __repr__(self):
        return "% s ,% s, %s" % (self.name, self.courses, self.numCourses)

def main():
    def main_s():
        while True:
            name_input = input("Full name: ").strip()
            address_input = input("Address: ").strip()
            person = Person(name_input, address_input)
            course_input = input("Enter the name of the course: ").strip()
            grade_input = int(input("Enter your grade for the chosen course: ").strip())
            s = Student(name_input, address_input)
            student = Student.addCourseGrade(s, name_input, course_input, grade_input)
            with open("scores.csv", 'a') as file:
                myfile = csv.writer(file)
                myfile.writerow([course_input, name_input, grade_input])
            print(person, student)
            ask = input("Do you want to see your average score: ")
            if ask == 'y' or ask =="yes" or ask == "Yes" or ask == 'Y':
                avg = Student.getAverageGrade(s, name_input, course_input)
                print(avg)
            elif ask == 'n'or ask =="no" or ask == "No" or ask == 'N':
                pass
            else:
                return False

    def main_t():
        name_input = input("Full name: ").strip()
        address_input = input("Address: ").strip()
        course_input = input("Enter the name of the course: ").strip()
        t = Teacher(course_input, name_input, address_input)
        Teacher.addCourse(t, course_input)
        Teacher.removeCourse(t, course_input)

    student_or_teacher = input("Are you a student or a teacher: ").capitalize().strip()
    if student_or_teacher == "student" or student_or_teacher == "Student":
        main_s()
    elif student_or_teacher == "teacher" or student_or_teacher == "Teacher":
        main_t()
    else:
        return False

if __name__=="__main__":
    main()

