from data import rankings


def getTeams(teamNames):
    assert type(teamNames) is list
    assert all(type(team) is str for team in teamNames)

    return [Team(name) for name in teamNames]


class Team:
    def __init__(self, name):
        assert type(name) is str

        self.name = name
        self.abbr = name[:3].upper()

        self.played = 0
        self.won = 0
        self.drawn = 0
        self.lost = 0
        self.goalsFor = 0
        self.goalsAway = 0
        self.goalDiff = 0
        self.points = 0

        self.form = []

        # Pot points are between teams on same points.
        self.potPoints = 0
        self.potGoalDiff = 0
        self.potGoalsFor = 0

        # Pot points 2 are to compare a team in a pot against
        # the rest of the group.
        self.potPoints2 = 0
        self.potGoalDiff2 = 0
        self.potGoalsFor2 = 0

        self.yellowCards = 0
        self.redCards = 0
        self.yellowRedCards = 0
        self.disciplinaryPoints = 0

        self.rankingPosition = rankings.get(self.name, 999)

    def calcDisciplinaryPoints(self):
        self.disciplinaryPoints = 3 * (self.redCards + self.yellowRedCards) +\
            self.yellowCards

    def resetPotNumbers(self):
        self.potPoints = 0
        self.potGoalDiff = 0
        self.potGoalsFor = 0
        self.potPoints2 = 0
        self.potGoalDiff2 = 0
        self.potGoalsFor2 = 0
