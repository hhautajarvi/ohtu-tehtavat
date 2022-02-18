class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score = [0, 0]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score[0] += 1
        else:
            self.score[1] += 1

    def get_score(self):
        if self.score[0] == self.score[1]:
            return self.even_score()
        elif max(self.score) >= 4:
            return self.near_win()
        else:
            return f"{self.points_to_words(self.score[0])}-{self.points_to_words(self.score[1])}"

    def even_score(self):
        if self.score[0] > 3:
            return "Deuce"
        else:
            return f"{self.points_to_words(self.score[0])}-All"

    def near_win(self):
        leader = self.player1_name
        if self.score[1] > self.score[0]:
            leader = self.player2_name
        if abs(self.score[0] - self.score[1]) == 1:
            return f"Advantage {leader}"
        else:
            return f"Win for {leader}"

    def points_to_words(self, points):
        if points == 0:
            return "Love"
        elif points == 1:
            return "Fifteen"
        elif points == 2:
            return "Thirty"
        elif points == 3:
            return "Forty"
