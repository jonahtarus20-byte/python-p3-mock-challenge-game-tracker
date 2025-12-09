class Game:
    def __init__(self, title):
        self._title = str(title)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        # ignore any assignment, keep it immutable
        pass

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({result.player for result in self.results()})

    def average_score(self, player):
        results_for_player = [r.score for r in self.results() if r.player == player]
        if results_for_player:
            return sum(results_for_player) / len(results_for_player)
        return 0


class Player:
    def __init__(self, username):
        self._username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        # only accept strings of length 2-16
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._username = value
        # else ignore invalid assignments silently

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result for result in self.results() if result.game == game])


class Result:
    all = []
    def __init__(self, player, game, score):
        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game
    
    @score.setter
    def score(self, value):
        # ignore assignment, immutable
        pass
