students = {}
available_classes = [i for i in range(1, 12)]
completed_classes = []
current_classes = []


def add_student(name, class_number):
    students[name] = class_number
    available_classes.remove(class_number)
    current_classes.append(class_number)


def delete_student(name):
    current_classes.remove(students[name])
    available_classes.insert(students[name] - 1, students[name])
    completed_classes.append(students[name])
    students.pop(name)


def show_current_classes():
    return current_classes


def show_completed_classes():
    return completed_classes


while True:
    print('1) add a student, 2) delete a student, '
          '3) show current classes, 4) show completed classes')
    option = input('Enter your option: ')

    if option == '1':
        student_name = input('Enter student name: ')
        print(available_classes)
        class_number = int(input('Enter class number: '))

        if class_number in available_classes:
            add_student(student_name, class_number)
            print('Transmitted successfully')
            print(students)
        else:
            print('Wrong class')
    elif option == '2':
        student_name = input('Enter student name to delete: ')

        if student_name in students:
            delete_student(student_name)
            print('Deleted successfully')
            print(students)
        else:
            print('Student does not exist')
    elif option == '3':
        print(show_current_classes())
    elif option == '4':
        print(show_completed_classes())
    else:
        print('Invalid input')
