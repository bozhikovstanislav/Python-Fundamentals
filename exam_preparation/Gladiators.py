class Gladiator:
    def __init__(self, name):
        self.name = name
        self.technique_lst = []

    def __str__(self):
        return f'{self.name}: {self.sum_of_skill()} skill'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def add_tehn_to_gladiator(self, thehnique):
        self.technique_lst.append(thehnique)

    @property
    def technique_lst(self):
        return self.__technique_lst

    @technique_lst.setter
    def technique_lst(self, technique_lst):
        self.__technique_lst = technique_lst

    def sum_of_skill(self):
        my_sum = sum(list(map(lambda gl1: gl1.skill, self.technique_lst)))
        return my_sum

    def get_gladiator_th_name(self, gladiator_th):
        for x in range(0, len(self.technique_lst)):
            if gladiator_th == self.technique_lst[x].name:
                return self.technique_lst[x].name

    def get_gladiator_th_skill(self, gladiator_th):
        for x in range(0, len(self.technique_lst)):
            if gladiator_th == self.technique_lst[x].name:
                return self.technique_lst[x].skill

    def update_existing_value(self, new_value, old_value):
        map(lambda x: x if x != old_value else new_value, self.technique_lst)


class Technique:
    def __init__(self, name, skill):
        self.name = name
        self.skill = int(skill)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def skill(self):
        return self.__skill

    def sum_of_skill(self):
        return

    @skill.setter
    def skill(self, skill):
        self.__skill = skill

    def __str__(self):
        return f'- {self.name} <!> {self.skill}'


class GladiatorPool:
    def __init__(self):
        self.gladiator_pool = []

    @property
    def gladiator_pool(self):
        return self.__gladiator_pool

    @gladiator_pool.setter
    def gladiator_pool(self, gladiator_pool):
        self.__gladiator_pool = gladiator_pool

    def add_gladiator_to_pool(self, gladiator):
        self.gladiator_pool.append(gladiator)

    def update_existing_value(self, new_value, old_value):
        self.gladiator_pool[self.gladiator_pool.index(old_value)] = new_value

    def get_gladiator_from_pool(self, gladiator_name):
        for x in range(0, len(self.gladiator_pool)):
            if gladiator_name == self.gladiator_pool[x].name:
                return self.gladiator_pool[x]


glpool = GladiatorPool()
data = input()
while not data == 'Ave Cesar':
    splitted_data = data.split(' -> ')
    if len(splitted_data) == 3:
        name = splitted_data[0]
        technique = splitted_data[1]
        skill = int(splitted_data[2])
        if name in [x.name for x in glpool.gladiator_pool]:
            th = Technique(technique, skill)
            gl = glpool.get_gladiator_from_pool(name)
            if technique == gl.get_gladiator_th_name(technique):
                old_value = gl.get_gladiator_th_skill(technique)
                gl.update_existing_value(skill, old_value)
            else:
                gl.add_tehn_to_gladiator(th)
        else:
            gl = Gladiator(name)
            th = Technique(technique, skill)
            gl.add_tehn_to_gladiator(th)
            glpool.add_gladiator_to_pool(gl)
    else:
        fighter_1 = data.split(' vs ')[0]
        fighter_2 = data.split(' vs ')[1]
        is_f1_inpool = fighter_1 in [x.name for x in glpool.gladiator_pool]
        is_f2_inpool = fighter_2 in [x.name for x in glpool.gladiator_pool]
        if is_f1_inpool and is_f2_inpool:
            gl1 = glpool.get_gladiator_from_pool(fighter_1)
            gl2 = glpool.get_gladiator_from_pool(fighter_2)

            lst_ = [x.name for x in gl1.technique_lst]
            technique_lst_ = [x.name for x in gl2.technique_lst]

            common_skills = list(set(lst_).intersection(set(technique_lst_)))
            if common_skills:
                if gl1.sum_of_skill() < gl2.sum_of_skill():
                    glpool.gladiator_pool.remove(gl1)
                elif gl2.sum_of_skill() < gl1.sum_of_skill():
                    glpool.gladiator_pool.remove(gl2)

    data = input()
ordered_gladiators = sorted(glpool.gladiator_pool, key=lambda gle: (-gle.sum_of_skill(), gle.name))
for a in ordered_gladiators:
    print(a)
    ay = sorted(a.technique_lst, key=lambda kvp: kvp.skill, reverse=True)
    for x in ay:
        print(x)
