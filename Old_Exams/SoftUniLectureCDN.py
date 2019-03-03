class ContentDeliveryNetwork:
    def __init__(self, number_of_server, course_net, lecture_net, trainer_net):
        self.number_of_server = int(number_of_server)
        self.course_net = course_net
        self.trainer_net = trainer_net
        self.lecture_net = lecture_net

    @property
    def course_net(self):
        return self.__course_net

    @course_net.setter
    def course_net(self, course_net):
        self.__course_net = course_net

    @property
    def lecture_net(self):
        return self.__lecture_net

    @lecture_net.setter
    def lecture_net(self, lecture_net):
        self.__lecture_net = lecture_net

    @property
    def trainer_net(self):
        return self.__trainer_net

    @trainer_net.setter
    def trainer_net(self, trainer_net):
        self.__trainer_net = trainer_net

    def __str__(self):
        return f'https://streamcdn{self.number_of_server}.softuni.bg/course={self.course_net.course_name}&lecture={self.lecture_net.name}&' + f'trainer={self.trainer_net.name}'


class CourseDuration:
    def __init__(self, hh, min, ss='00'):
        self.hh = hh
        self.min = min

    @property
    def hh(self):
        return self.__hh

    @hh.setter
    def hh(self, hh):
        self.__hh = hh

    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, min):
        self.__min = min


class Course:
    def __init__(self, course_name, trainer_cour, course_duration):
        self.course_duration = course_duration
        self.trainer_cour = trainer_cour
        self.course_name = course_name

    def __str__(self):
        return self.course_name + " " + self.trainer.name + " " + self.courseDuration.hh


class Trainer:
    def __init__(self, name):
        self.name = name


class Lecture:
    def __init__(self, name):
        self.name = name


trainer = Trainer("Gosho")
durationcourse = CourseDuration('01', '12', '33')
lec = Lecture("polymorphism")
course = Course("cshap", trainer, durationcourse)

cdnt = ContentDeliveryNetwork(1, course, lec, trainer)
print(cdnt)
