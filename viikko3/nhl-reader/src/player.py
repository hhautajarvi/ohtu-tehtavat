class Player:
    def __init__(self, name,  team, goals, assists, nationality):
        self.name = name
        self.team = team    
        self.goals = goals
        self.assists = assists
        self.points = goals + assists
        self.nationality = nationality

    def __str__(self):
        return f"{self.name:20}{self.team:5}{str(self.goals):2} + {str(self.assists):2} = {str(self.points)}"
