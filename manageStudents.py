from student import Student

student_log = []

def create_student(name, marks):
    return Student(name, marks)

def add_new_student():
    name = input('Enter student name: ')
    marks = []
    while True:
        mark = input('Enter mark (or write stop to stop): ')
        if mark == 'stop':
            break
        marks.append(int(mark))
    student = create_student(name, marks)
    student_log.append(student)
    print('Student %s added' % name)

def print_students():
    for student in student_log:
        student.print_info()

def print_average_marks():
    for student in student_log:
        print('%s: %s' % (student.name, student.average_marks()))

def remove_student():
    name = input('Enter student name: ')
    for student in student_log:
        if student.name == name:
            student_log.remove(student)
            del student
            break

def menu():
    while True:
        print('1. Add new student')
        print('2. Print students')
        print('3. Print average marks')
        print('4. Remove student')
        print('5. Exit')
        choice = input('Enter your choice: ')
        if choice == 1:
            add_new_student()
        elif choice == 2:
            print_students()
        elif choice == 3:
            print_average_marks()
        elif choice == 4:
            remove_student()
        elif choice == 5:
            break
        else:
            print('Invalid choice')
            continue

    print('Bye!')
    print()
    print('Student log:')
    print_students()
    print()
    print('Average marks:')
    print_average_marks()

if __name__ == '__main__':
    
   menu()