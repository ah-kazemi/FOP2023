import re

class User:
    def __init__(self, id, name, password, type):
        self.id = id
        self.name = name
        self.password = password
        self.type = type
        self.courses = []

class Course:
    def __init__(self, course_id, name, capacity):
        self.course_id = course_id
        self.name = name
        self.capacity = capacity
        self.students = []

class UniversityManagementSystem:
    def __init__(self):
        self.users = []
        self.courses = []
        self.current_menu = 'log in/sign up menu'
        self.logged_in_user = None

    def run(self):
        while True:
            command = input().strip()
            if 'edu exit edu' in command:
                break
            elif command == 'edu current menu edu':
                print(self.current_menu)
            elif command.startswith('edu sign up'):
                self.sign_up(command)
            elif command.startswith('edu log in'):
                self.log_in(command)
            elif command == 'edu show course list edu':
                self.show_course_list()
            elif command == 'edu log out edu':
                self.log_out()
            elif command.startswith('edu add course'):
                self.add_course(command)
            elif command.startswith('edu get course'):
                self.get_course(command)
            else:
                print('invalid command')

    def sign_up(self, command):
        parts = command.split('-')
        if len(parts) != 5:
            print('invalid command')
            return
        type = parts[1].strip()
        if type not in ['S', 'P']:
            print('invalid type')
            return
        id_parts = parts[2].split()[1:]
        if len(id_parts) > 1 or not ''.join(id_parts).isdigit():
            print('invalid id')
            return
        id = ''.join(id_parts)
        name_parts = parts[3].split()[1:]
        if len(name_parts) > 1:
            print('invalid name')
            return
        name = ''.join(name_parts)
        password = parts[4].split()[1]
        if len(password) < 4 or ' ' in password or not re.search('[*.!@$%^&()]', password):
            print('invalid password')
            return
        if any(user.id == id for user in self.users):
            print('id already exists')
            return
        self.users.append(User(id, name, password, type))
        print('signed up successfully!')

    def log_in(self, command):
        parts = command.split('-')
        if len(parts) != 3 or '  ' in command.replace('edu', '').strip():
            print('invalid command')
            return
        id_parts = parts[1].split()
        if id_parts[0] != 'i':
            print('invalid command')
            return
        if len(id_parts) > 2:
            print('incorrect id')
            return
        id = id_parts[1]
        password = parts[2].split()[1]
        user = next((user for user in self.users if user.id == id), None)
        if user is None:
            print('incorrect id')
            return
        if user.password != password:
            print('incorrect password')
            return
        self.logged_in_user = user
        self.current_menu = 'student menu' if user.type == 'S' else 'professor menu'
        print('logged in successfully!')
        print('entered', self.current_menu)

    def show_course_list(self):
        if self.logged_in_user is None:
            print('invalid command')
            return
        print('course list:')
        for course in self.courses:
            print(f'{course.course_id} {course.name} {len(course.students)}/{course.capacity}')

    def log_out(self):
        if self.logged_in_user is None:
            print('invalid command')
            return
        self.logged_in_user = None
        self.current_menu = 'log in/sign up menu'
        print('logged out successfully!')
        print('entered', self.current_menu)

    def add_course(self, command):
        parts = command.split('-')
        if len(parts) != 4 or '  ' in command.replace('edu', '').strip() or parts[1].strip()[0] != 'c' or \
                parts[2].strip()[0] != 'i':
            print('invalid command')
            return
        if self.logged_in_user is None or self.logged_in_user.type != 'P':
            print('invalid command')
            return
        course_name_parts = parts[1].split()[1:]
        if len(course_name_parts) > 1:
            print('invalid course name')
            return
        course_name = ''.join(course_name_parts)
        id_parts = parts[2].split()[1:]
        if len(id_parts) > 1 or not ''.join(id_parts).isdigit():
            print('invalid course id')
            return
        id = ''.join(id_parts)
        capacity_parts = parts[3].split()[1]
        if not capacity_parts.isdigit():
            print('invalid course capacity')
            return
        capacity = int(capacity_parts)
        if any(course.course_id == id for course in self.courses):
            print('course id already exists')
            return
        self.courses.append(Course(id, course_name, capacity))
        print('course added successfully!')

    def get_course(self, command):
        if self.logged_in_user is None or self.logged_in_user.type != 'S':
            print('invalid command')
            return
        parts = command.split('-')
        if len(parts) != 2:
            print('invalid command')
            return
        course_id = parts[1].split()[1]
        course = next((course for course in self.courses if course.course_id == course_id), None)
        if course is None:
            print('incorrect course id')
            return
        if course in self.logged_in_user.courses:
            print('you already have this course')
            return
        if len(course.students) >= course.capacity:
            print('course is full')
            return
        self.logged_in_user.courses.append(course)
        course.students.append(self.logged_in_user)
        print('course added successfully!')


system = UniversityManagementSystem()
system.run()
