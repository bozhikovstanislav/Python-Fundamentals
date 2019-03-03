list_of_lectures = []


def calc_duration_in_minutes(lecture):
    lecture["dur_hours"] = int(lecture["duration"].split("h")[0])
    lecture["dur_mins"] = int(lecture["duration"].split("h")[1][:-1])
    return lecture["dur_hours"] * 60 + lecture["dur_mins"]


while True:
    str_line = input()
    if str_line.split()[0] == "scrape":
        if str_line.split()[1] == "course":
            course_name = str_line.split()[2]
            total_duration_in_minutes = 0
            total_duration_of_all_lectures_in_minutes = 0
            for lecture in list_of_lectures:
                total_duration_of_all_lectures_in_minutes += lecture["duration_in_minutes"]
                if lecture["course"] == course_name:
                    total_duration_in_minutes += lecture["duration_in_minutes"]
                    # "ceil"-s the result for k for both floats and int-s
                    k = int(total_duration_of_all_lectures_in_minutes / (10 * 60)) + (
                                total_duration_of_all_lectures_in_minutes % (10 * 60) > 0)
                    print(f"https://streamcdn{k}.softuni.bg/course={lecture['course']}&lecture={lecture[
                        'lecture']}&trainer={lecture['trainer']}")
            print(f"total duration: {(total_duration_in_minutes // 60):02d}:{(total_duration_in_minutes % 60):02d}:00")
            break
        elif str_line.split()[1] == "trainer":
            trainer_name = str_line.split()[2]
            total_duration_in_minutes = 0
            total_duration_of_all_lectures_in_minutes = 0
            for lecture in list_of_lectures:
                total_duration_of_all_lectures_in_minutes += lecture["duration_in_minutes"]
                if lecture["trainer"] == trainer_name:
                    total_duration_in_minutes += lecture["duration_in_minutes"]
                    # "ceil"-s the result for k for both floats and int-s
                    k = int(total_duration_of_all_lectures_in_minutes / (10 * 60)) + (
                                total_duration_of_all_lectures_in_minutes % (10 * 60) > 0)
                    print(f"https://streamcdn{k}.softuni.bg/course={lecture['course']}&lecture={lecture[
                        'lecture']}&trainer={lecture['trainer']}")
            print(f"total duration: {(total_duration_in_minutes // 60):02d}:{(total_duration_in_minutes % 60):02d}:00")
            break
    str_line_list = str_line.split(";")
    lecture = {}
    for i in range(len(str_line_list)):
        key, value = str_line_list[i].split(":")
        lecture[key] = value
    duration_in_minutes = calc_duration_in_minutes(lecture)
    lecture["duration_in_minutes"] = duration_in_minutes
    list_of_lectures.append(lecture)