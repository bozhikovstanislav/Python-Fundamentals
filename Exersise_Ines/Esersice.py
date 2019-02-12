class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = problems


data = input()
exercises = []

while not data == 'go go go':
    splitted_data = data.split(" -> ")
    topic = splitted_data[0]
    course_name = splitted_data[1]
    judge_contest_link = splitted_data[2]
    problems = splitted_data[3].split(", ")

    exercise = Exercise(topic=topic, course_name=course_name, judge_contest_link=judge_contest_link, problems=problems)
    exercises.append(exercise)

    data = input()

for exercise in exercises:
    print(f'Exercises: {exercise.topic}')
    print(f'Problems for exercises and homework for the "{exercise.course_name}" course @ SoftUni.')
    print(f'Check your solutions here: {exercise.judge_contest_link}')
    counter = 1
    for problem in exercise.problems:
        print(f'{counter}. {problem}')
        counter += 1