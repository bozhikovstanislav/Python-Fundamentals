class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.__topic = self.set_topic(topic)
        self.__course_name = self.set_course_name(course_name)
        self.__judge_contest_link = self.set_judge_contest_link(judge_contest_link)
        self.__problems = problems

    def set_topic(self, topic):
        if topic.isalpha():
            return topic

    def get_topic(self):
        return self.__topic

    def set_course_name(self, course_name):
        if course_name.isalpha():
            return course_name

    def get_course_name(self):
        return self.__course_name

    def set_judge_contest_link(self, judge_contest_link):
            return judge_contest_link

    def get_judge_contest_link(self):
        return self.__judge_contest_link

    def set_problems(self, problems):
        if isinstance(problems, list):
            return problems

    def get_problems(self):
        return self.__problems

    def __str__(self):
        a = f'Exercises: {self.__topic}\n'
        b = f'Problems for exercises and homework for the "{self.get_course_name()}" course @ SoftUni.'
        c = f'\nCheck your solutions here: {self.__judge_contest_link}'
        return a + b + c


topic_i = ""
course_name_i = ""
judge_contest_link_i = ""
problems_i = []
listExer=[]
while True:
    data = input()
    if data == 'go go go':
        break
    else:
        list_str = data.split(' -> ')
        topic_i = list_str[0]
        course_name_i = list_str[1]
        judge_contest_link_i = list_str[2]
        problems_i = list(list_str[3:][0].split(', '))
        exter = Exercise(topic_i, course_name_i, judge_contest_link_i, problems_i)
        listExer.append(exter)

for i in listExer:
    print(i)
    count = 1
    for x in range(0, len(i.get_problems())):
        print(f'{count}. {i.get_problems()[x]}')
        count += 1
