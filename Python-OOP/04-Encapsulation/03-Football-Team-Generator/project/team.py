class Team:
    def __init__(self, name, rating):
        self.__name = name
        self.__rating = rating
        self.__players=[]

    def get_name(self):
        return self.__name

    @property
    def name(self):
        return self.__name

    def set_name(self, name):
        self.__name=name

    def get_rating(self):
        return self.__rating

    @property
    def rating(self):
        return self.__rating

    def set_rating(self, rating):
        self.__rating=rating

    def get_players(self):
        return self.__players

    @property
    def players(self):
        return self.__players

    def set_players(self, players):
        self.__players=players

    def add_player(self, player):
        if player in self.__players:
            return f"Player {player.get_name()} has already joined"
        self.__players.append(player)
        return f"Player {player.get_name()} joined team {self.get_name()}"

    def remove_player(self, player_name):
        for player in self.__players:
            if player.get_name() == player_name:
                current_player = player
                self.__players.remove(player)
                return current_player
        return f"Player {player_name} not found"


