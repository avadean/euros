import game as g
import team as t


def getGroups(groups):
    assert type(groups) is dict

    localGroups = []

    for name, group in groups.items():
        assert type(name) is str
        assert type(group) is list
        assert all(type(team) is str for team in group)

        teams = t.getTeams(group)

        localGroups.append(Group(name, teams))

    return localGroups


class Group:
    def __init__(self, name, teams):
        assert type(name) is str

        assert type(teams) is list
        assert len(teams) == 4
        assert all(type(team) is t.Team for team in teams)

        self.name = name
        self.teams = teams
        self.games = [g.Game(teamA, teamB)
                      for numA, teamA in enumerate(teams)
                      for numB, teamB in enumerate(teams) if numA > numB]
        self.complete = False

    def playGame(self, teamA, teamB, teamAgoals, teamBgoals,
                 teamApenalties=None, teamBpenalties=None,
                 yellowCardsA=0, redCardsA=0, yellowRedCardsA=0,
                 yellowCardsB=0, redCardsB=0, yellowRedCardsB=0):

        for game in self.games:
            if teamA == game.teamA.name and teamB == game.teamB.name:
                game.playGame(teamAgoals, teamBgoals,
                              teamApenalties, teamBpenalties,
                              yellowCardsA, redCardsA, yellowRedCardsA,
                              yellowCardsB, redCardsB, yellowRedCardsB)
            elif teamA == game.teamB.name and teamB == game.teamA.name:
                game.playGame(teamBgoals, teamAgoals,
                              teamBpenalties, teamApenalties,
                              yellowCardsB, redCardsB, yellowRedCardsB,
                              yellowCardsA, redCardsA, yellowRedCardsA)

        #if knockout: self.rankTeams()
        self.rankTeams()
        self.checkComplete()

    def checkComplete(self):
        self.complete = True if all(game.played for game in self.games) else False

    def rankTeams(self):
        self.teams = sorted(self.teams, key=lambda x: x.points, reverse=True)

        team0, team1, team2, team3 = self.teams

        potA = [team0]
        potB = []
        potC = []
        potD = []

        # This bit of code creates four pots out of the teams in the group
        # based on the points. E.g.
        # TeamA points = 3
        # TeamB points = 1
        # TeamC points = 1
        # TeamD points = 0
        # This will create:
        # potA = [teamA]
        # potB = [teamB, teamC]
        # potC = [teamD]
        # potD = []
        if team1.points == team0.points:
            potA.append(team1)
            if team2.points == team1.points:
                potA.append(team2)
                if team3.points == team2.points:
                    potA.append(team3)
                else:
                    potB.append(team3)
            else:
                potB.append(team2)
                if team3.points == team2.points:
                    potB.append(team3)
                else:
                    potC.append(team3)
        else:
            potB.append(team1)
            if team2.points == team1.points:
                potB.append(team2)
                if team3.points == team2.points:
                    potB.append(team3)
                else:
                    potC.append(team3)
            else:
                potC.append(team2)
                if team3.points == team2.points:
                    potC.append(team3)
                else:
                    potD.append(team3)

        if all([True if len(pot) == 1 else False
                for pot in [potA, potB, potC, potD]]):
            # All sorted and each have different points so quick return.
            return

        # This list comprehension gives the numbers of wins for each team in
        # the pot but where the win total is based on only teams in that pot.
        # E.g.
        # TeamA points = 3 (win against teamB)
        # TeamB points = 3 (win against teamC)
        # TeamC points = 0
        # TeamD points = 0 (yet to play)
        # Then potA = [TeamA, TeamB] and potB = [TeamC, TeamD]
        # therefore winsA = [1, 0] where the 1 corresponds to TeamA's win over
        # teamB the 0 corresponds to the fact that teamB's win came from
        # against a team not in their pot. winsB = [0, 0] of course.

        pots = [potA, potB, potC, potD]

        for num, pot in enumerate(pots):
            restOfGroup = []
            for i in range(4):
                if i != num:
                    restOfGroup += pots[i]

            for team in pot:
                restOfPot = [team2 for team2 in pot if team2.name != team.name]

                for game in self.games:
                    if game.played and game.participated(team):
                        if game.anyParticipated(restOfPot):

                            if game.winner == team.name:
                                team.potPoints += 3

                            elif game.winner is None:
                                team.potPoints += 1

                            team.potGoalDiff += game.getTeamGoalDiff(team)
                            team.potGoalsFor += game.getTeamScored(team)

                        elif game.anyParticipated(restOfGroup):

                            if game.winner == team.name:
                                team.potPoints2 += 3

                            elif game.winner is None:
                                team.potPoints2 += 1

                            team.potGoalDiff2 += game.getTeamGoalDiff(team)
                            team.potGoalsFor2 += game.getTeamScored(team)

        # Now that we've got the extra information based on the pots,
        # recombine them to form the teams again.
        self.teams = potA + potB + potC + potD

        # Now sort them!
        self.teams = sorted(self.teams, key=lambda x: (-x.points,
                                                       -x.potPoints,
                                                       -x.potGoalDiff,
                                                       -x.potGoalsFor,
                                                       -x.potPoints2,
                                                       -x.potGoalDiff2,
                                                       -x.potGoalsFor2,
                                                       -x.goalDiff,
                                                       -x.goalsFor,
                                                       -x.won,
                                                       x.disciplinaryPoints,
                                                       x.rankingPosition))

        # Need to reset pot numbers for next time.
        for team in self.teams:
            team.resetPotNumbers()

    def __str__(self):
        table = ' ----------------------- Group {} -----------------------\n'.format(self.name)

        table += '          Club        '
        table += 'MP  MW  MD  ML   GF   GA   GD  PTS\n'

        for position, team in enumerate(self.teams, 1):
            table += '{:>2d}  {:<16s}  {:>2d} '.format(position,
                                                       team.name,
                                                       team.played)

            table += ' {:>2d}  {:>2d}  {:>2d} '.format(team.won,
                                                       team.drawn,
                                                       team.lost)

            table += ' {:>3d}  {:>3d}  {:>3d}  {:>3d}\n'.format(team.goalsFor,
                                                                team.goalsAway,
                                                                team.goalDiff,
                                                                team.points)
        # table = table[:-1]

        return table
