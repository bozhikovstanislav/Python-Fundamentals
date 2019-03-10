from abc import ABC, abstractmethod


class BaseMonster(ABC):
    @abstractmethod
    def __init__(self, name, mon_id, strength, ugliness):
        self.name = name
        self.mon_id = int(mon_id)
        self.strength = int(strength)
        self.ugliness = int(ugliness)


class Hydralisk(BaseMonster):
    def __init__(self, name, mon_id, strength, ugliness, range):
        BaseMonster.__init__(self, name, mon_id, strength, ugliness)
        self.range = range

    @property
    def range(self):
        return self.__range

    @range.setter
    def range(self, range):
        if isinstance(range, str):
            self.__range = range
        else:
            raise Exception('Range must be string')


class Zergling(BaseMonster):
    def __init__(self, name, mon_id, strength, ugliness, speed):
        BaseMonster.__init__(self, name, mon_id, strength, ugliness)
        self.speed = speed

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        try:
            self.__speed = int(speed)
        except:
            raise Exception('Speed must be integer')


data = input()
warriors_list = []

while not data == 'stopAddingArmy':
    try:
        warrior = eval(data)
        warriors_list.append(warrior)

    except Exception as ex:
        print(ex)

    data = input()

overall_speed = 0
overall_strength = 0
hyd_count = 0
zer_count = 0

for inst in warriors_list:
    if isinstance(inst, Zergling):
        overall_speed += inst.speed
        zer_count += 1

    if isinstance(inst, Hydralisk):
        hyd_count += 1

    overall_strength += inst.strength

print(f'Overall speed of army: {overall_speed}')
print(f'Overall stength: {overall_strength}')
print(f'Hydralisk: {hyd_count}; Zergling: {zer_count}')