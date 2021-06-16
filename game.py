import team as t


class Game:
    def __init__(self, teamA, teamB, knockoutRound=False):
        assert type(teamA) is t.Team
        assert type(teamB) is t.Team
        assert type(knockoutRound) is bool

        self.teamA = teamA
        self.teamB = teamB

        self.teams = [teamA.name, teamB.name]

        self.knockoutRound = knockoutRound

        self.played = False
        self.winner = None
        self.loser = None

        self.goalsA = None
        self.goalsB = None

    def playGame(self, goalsA, goalsB,
                 penaltiesA=None, penaltiesB=None,
                 yellowCardsA=0, redCardsA=0, yellowRedCardsA=0,
                 yellowCardsB=0, redCardsB=0, yellowRedCardsB=0):

        assert type(goalsA) is int
        assert type(goalsB) is int
        assert type(yellowCardsA) is int
        assert type(redCardsA) is int
        assert type(yellowRedCardsA) is int
        assert type(yellowCardsB) is int
        assert type(redCardsB) is int
        assert type(yellowRedCardsB) is int

        assert goalsA >= 0
        assert goalsB >= 0
        assert yellowCardsA >= 0
        assert redCardsA >= 0
        assert yellowRedCardsA >= 0
        assert yellowCardsB >= 0
        assert redCardsB >= 0
        assert yellowRedCardsB >= 0

        self.goalsA = goalsA
        self.goalsB = goalsB

        self.teamA.yellowCards += yellowCardsA
        self.teamA.redCards += redCardsA
        self.teamA.yellowRedCards += yellowRedCardsA
        self.teamB.yellowCards += yellowCardsB
        self.teamB.redCards += redCardsB
        self.teamB.yellowRedCards += yellowRedCardsB

        if not self.knockoutRound:
            self.teamA.played += 1
            self.teamB.played += 1

            self.teamA.goalsFor += goalsA
            self.teamB.goalsFor += goalsB
            self.teamA.goalsAway += goalsB
            self.teamB.goalsAway += goalsA

            self.teamA.goalDiff += goalsA - goalsB
            self.teamB.goalDiff += goalsB - goalsA

            if goalsA == goalsB:
                self.winner = None

                self.teamA.drawn += 1
                self.teamB.drawn += 1

                self.teamA.points += 1
                self.teamB.points += 1

                self.teamA.form.append('D')
                self.teamB.form.append('D')

            elif goalsA > goalsB:
                self.winner = self.teamA.name
                self.loser = self.teamB.name

                self.teamA.won += 1
                self.teamB.lost += 1

                self.teamA.points += 3

                self.teamA.form.append('W')
                self.teamB.form.append('L')

            else:
                self.winner = self.teamB.name
                self.loser = self.teamA.name

                self.teamA.lost += 1
                self.teamB.won += 1

                self.teamB.points += 3

                self.teamA.form.append('L')
                self.teamB.form.append('W')

        if self.knockoutRound:
            assert type(penaltiesA) is int
            assert type(penaltiesB) is int

            assert penaltiesA >= 0
            assert penaltiesB >= 0

            if goalsA == goalsB:
                if penaltiesA > penaltiesB:
                    self.winner = self.teamA.name
                else:
                    self.winner = self.teamB.name

            elif goalsA > goalsB:
                self.winner = self.teamA.name

            else:
                self.winner = self.teamB.name

        self.teamA.calcDisciplinaryPoints()
        self.teamB.calcDisciplinaryPoints()

        self.played = True

    def participated(self, team):
        assert type(team) in [t.Team, list]

        return True if team.name in self.teams else False

    def anyParticipated(self, teams):
        assert type(teams) is list
        assert all(type(team) == t.Team for team in teams)

        return any(True if team.name in self.teams else False
                   for team in teams)

    def getTeamGoalDiff(self, team):
        assert self.participated(team)
        assert self.played

        if team.name == self.teamA.name:
            return self.goalsA - self.goalsB
        else:
            return self.goalsB - self.goalsA

    def getTeamScored(self, team):
        assert self.participated(team)
        assert self.played

        if team.name == self.teamA.name:
            return self.goalsA
        else:
            return self.goalsB
