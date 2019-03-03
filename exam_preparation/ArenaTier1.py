class Gladiotor:
    def __init__(self, name, skill_dict):
        self.name = name
        self.skill_dict = skill_dict
        self.total_skill = 0

    def set_total_skill(self):
        self.total_skill = sum(list(self.skill_dict.values()))


data = input()
gladiators_list = []

while not data == 'Ave Cesar':
    splitted_data = data.split(' -> ')

    if len(splitted_data) == 3:
        dict_obj = {splitted_data[1]: int(splitted_data[2])}
        gladiator = None
        if splitted_data[0] in list(map(lambda g: g.name, gladiators_list)):
            gladiator = list(filter(lambda g: g.name == splitted_data[0], gladiators_list))[0]
            techniques = []

            for gla in gladiators_list:
                try:
                    techniques.extend(list(gla.skill_dict.keys()))
                except KeyError:
                    techniques.append(list(gla.skill_dict.keys()))

            if splitted_data[1] in techniques:
                skill = int(splitted_data[2])
                key = gladiator.skill_dict.get(splitted_data[1], None)
                if key:
                    current_skill = gladiator.skill_dict[splitted_data[1]]
                    if skill > current_skill:
                        gladiator.skill_dict[splitted_data[1]] = int(splitted_data[2])
            else:
                gladiator.skill_dict.update(dict_obj)
        else:
            gladiator = Gladiotor(splitted_data[0], dict_obj)
            gladiators_list.append(gladiator)


    else:
        first_g_name, second_g_name = data.split(' vs ')
        list_g_names = list(map(lambda g: g.name, gladiators_list))

        if first_g_name in list_g_names and second_g_name in list_g_names:
            first_g_obj = list(filter(lambda g: g.name == first_g_name, gladiators_list))[0]
            second_g_obj = list(filter(lambda g: g.name == second_g_name, gladiators_list))[0]

            skills_first = first_g_obj.skill_dict.keys()
            skills_second = second_g_obj.skill_dict.keys()

            common_skils_list = list(set(skills_first).intersection(set(skills_second)))

            if common_skils_list:
                total_first_point = sum(list(first_g_obj.skill_dict.values()))
                total_second_point = sum(list(second_g_obj.skill_dict.values()))

                if total_first_point > total_second_point:
                    gladiators_list.remove(second_g_obj)
                else:
                    gladiators_list.remove(first_g_obj)

    data = input()

for g in gladiators_list:
    g.set_total_skill()

ordered_gladiators_list = sorted(gladiators_list, key=lambda g: (-g.total_skill, g.name))

for gladiator in ordered_gladiators_list:
    print(f'{gladiator.name}: {gladiator.total_skill} skill')
    ordered_techniques = sorted(gladiator.skill_dict.items(), key=lambda kvp: (-kvp[1], kvp[0]))
    for key in ordered_techniques:
        print(f'- {key[0]} <!> {key[1]}')