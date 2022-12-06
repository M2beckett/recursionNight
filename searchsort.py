
class student:
    def __init__(self, name, studentId, gpa, credits):
        self.name = name
        self.bannerId = studentId
        self.gpa = gpa
        self.credits = credits

    def __str__(self):
        return f"Student with name: {self.name} and bannerId: {self.bannerId} \n gpa: {self.gpa}, credits: {self.credits}"
#end student class

def binary_search(list_of_students, student_to_find):
    if list_of_students ==[]:
        return None
    middle = len(list_of_students)//2
    middle_student = list_of_students[middle]
    if middle_student.name == student_to_find:
        return middle_student
    if middle_student.name < student_to_find:
        return binary_search(list_of_students[middle+1:],student_to_find)
    else:
        return binary_search(list_of_students[:middle-1], student_to_find)


def get_data(filename):
    student_file = open(filename)
    lines = student_file.readlines()
    list_of_students = []
    for student_line in lines:
        data = student_line.split('|')
        current_student = student(data[0], int(data[1]), gpa=float(data[3]), credits=int(data[2]))
        list_of_students.append(current_student)
    return list_of_students

def get_key(student_to_sort):
    return  student_to_sort.name

def main():
    student_data = get_data("students.txt")
    student_data.sort(key=get_key)
    stu_to_find = input("what student should we find")
    result = binary_search(student_data, stu_to_find)
    print(result)
#    for stu in student_data:
#        print(stu)

def find_sum_of_credits():
    student_data = get_data("students.txt")
    sum = 0
    for someone in student_data:
        sum = sum + someone.credits
    return sum

def recursive_sum_of_credits(student_list):
    if not student_list:
        return 0
    first_student = student_list[0]
    return first_student.credits + recursive_sum_of_credits(student_list[1:])


recursive_sum = recursive_sum_of_credits(get_data("students.txt"))
sum = find_sum_of_credits()
print(f"those students too {sum} credits all together")
print(f"the recursive calculated sum is {recursive_sum}")
#main()


