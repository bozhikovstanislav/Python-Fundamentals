class Player:
    def __init__(self, player_name):
        self.name = player_name
        self.numbers_of_game = []

    @property
    def numbers_of_game(self):
        return self.__numbers_of_game

    @numbers_of_game.setter
    def numbers_of_game(self, numbers_of_game):
        self.__numbers_of_game = numbers_of_game

    def print_second(self):
        return f'{self.name}: {self.num_of_skore()}'

    def __str__(self):
        return f'{self.name}: {self.sum_of_skore()}'

    def sum_of_skore(self):
        my_sum = sum(list(map(lambda gl1: gl1.score_value, self.numbers_of_game)))
        return my_sum

    def num_of_skore(self):
        my_sum = len(self.numbers_of_game)
        return my_sum


class Score:
    def __init__(self, scor_value):
        self.score_value = int(scor_value)


class GamePool:
    def __init__(self):
        self.game_pool = []

    @property
    def game_pool(self):
        return self.__game_pool

    def add_game_pool(self, game_pool):
        self.game_pool.append(game_pool)

    @game_pool.setter
    def game_pool(self, value):
        self.__game_pool = value


data = input()
game_pool = GamePool()
while data != "report":
    data_lst = data.split(' -> ')
    name_player = data_lst[0].split(' ')
    player = Player(name_player[0])
    if ' -> ' in data:
        if name_player[0] != 'score' and name_player[0] != 'report':
            if len(data_lst) >= 2 and name_player[0]:
                games_player = data_lst[1:][0].split(', ')
                for x in range(0, len(games_player)):
                    score_pl = Score(games_player[x])
                    player.numbers_of_game.append(score_pl)
                game_pool.add_game_pool(player)
    data = input()
data = input()
while data != 'end':
    if data == 'score descending':
        ordered_players = sorted(game_pool.game_pool, key=lambda gle: (-gle.sum_of_skore(), gle.name))
        for x in ordered_players:
            print(x)
    elif data == 'score ascending':
        ordered_players = sorted(game_pool.game_pool, key=lambda gle: (gle.sum_of_skore(), gle.name))
        for x in ordered_players:
            print(x)
    elif data == 'numberOfGames descending':
        ordered_players = sorted(game_pool.game_pool, key=lambda gle: (-gle.num_of_skore(), gle.name))
        for x in ordered_players:
            print(x.print_second())
    elif data == 'numberOfGames ascending':
        ordered_players = sorted(game_pool.game_pool, key=lambda gle: (gle.num_of_skore(), gle.name))
        for x in ordered_players:
            print(x.print_second())
    data = input()
