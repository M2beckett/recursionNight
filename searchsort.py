
class student:
    def __init__(self, name, studentId, gpa, credits):
        self.name = name
        self.bannerId = studentId
        self.gpa = gpa
        self.credits = credits

    def __str__(self):
        return f"Student with name: {self.name} and bannerId: {self.bannerId} \n gpa: {self.gpa}, credits: {self.credits}"
#end student class

def get_data(filename):
    student_file = open(filename)
    lines = student_file.readlines()
    list_of_students = []
    for student_line in lines:
        data = student_line.split('|')
        current_student = student(data[0], int(data[1]), gpa=data[3], credits=data[2])
        list_of_students.append(current_student)
    return list_of_students

def get_key(student_to_sort:student):
    return  student_to_sort.name

def main():
    student_data = get_data("students.txt")
    student_data.sort(key=get_key)
    for stu in student_data:
        print(stu)

main()


