from abc import ABC, abstractmethod
import re


class Human(ABC):
    @abstractmethod
    def __init__(self, first_name, last_name):
        self.fisrt_name = first_name
        self.last_name = last_name

    @property
    def fisrt_name(self):
        return self.__fisrt_name

    @fisrt_name.setter
    def fisrt_name(self, fisrt_name):
        length = len(fisrt_name)

        if not fisrt_name[0].isupper():
            raise Exception('Expected upper case letter! Argument: firstName')

        if length < 4:
            raise Exception('Expected length at least 4 symbols! Argument: firstName')

        self.__fisrt_name = fisrt_name

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        length = len(last_name)

        if not last_name[0].isupper():
            raise Exception('Expected upper case letter! Argument: lastName')

        if length < 3:
            raise Exception('Expected length at least 3 symbols! Argument: lastName ')

        self.__last_name = last_name


class Student(Human):
    def __init__(self, name, last_name, faculty_number):
        Human.__init__(self, name, last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self.__faculty_number

    @faculty_number.setter
    def faculty_number(self, faculty_number):
        length = len(faculty_number)

        is_allowed = bool(re.match("^[A-Za-z0-9]*$", faculty_number))

        if not (5 <= length <= 10) or not is_allowed:
            raise Exception('Invalid faculty number!')

        self.__faculty_number = faculty_number

    def __str__(self):
        return f'First Name: {self.fisrt_name}\nLast Name: {self.last_name}\nFaculty number: {self.faculty_number}'


class Worker(Human):
    def __init__(self, name, ln, week_salary, w_h):
        Human.__init__(self, name, ln)
        self.week_salary = float(week_salary)
        self.work_hours_per_day = float(w_h)

    def get_money_per_hour(self):
        return self.week_salary / 5 / self.work_hours_per_day

    @property
    def week_salary(self):
        return self.__week_salary

    @week_salary.setter
    def week_salary(self, week_salary):

        if not (week_salary > 10):
            raise Exception('Expected value mismatch! Argument: weekSalary')

        self.__week_salary = week_salary

    @property
    def work_hours_per_day(self):
        return self.__work_hours_per_day

    @work_hours_per_day.setter
    def work_hours_per_day(self, work_hours_per_day):

        if not (work_hours_per_day >= 1 and work_hours_per_day <= 12):
            raise Exception('Expected value mismatch! Argument: workHoursPerDay')

        self.__work_hours_per_day = work_hours_per_day

    def __str__(self):
        return f'First Name: {self.fisrt_name}\nLast Name: {self.last_name}\nWeek Salary: {self.week_salary:.2f}\nHours per day: {self.work_hours_per_day:.2f}\nSalary per hour: {self.get_money_per_hour():.2f}'


student_list = input().split()
worker_list = input().split()

try:
    student = Student(student_list[0], student_list[1], student_list[2])
    worker = Worker(worker_list[0], worker_list[1], worker_list[2], worker_list[3])
    print(student)
    print()
    print(worker)
except Exception as ex:
    print(ex)
