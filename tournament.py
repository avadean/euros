import group as g


def getTournament(groups):
    localGroups = g.getGroups(groups)

    return Tournament(localGroups)


class Tournament:
    def __init__(self, groups):
        assert type(groups) is list
        assert all(type(group) is g.Group for group in groups)

        self.groups = groups
        self.roundOf16 = []
        self.quarterFinal = []
        self.semiFinal = []
        self.final = None

    def playGame(self, teamA, teamB,
                 teamAgoals, teamBgoals,
                 teamApenalties=None, teamBpenalties=None,
                 yellowCardsA=0, redCardsA=0, yellowRedCardsA=0,
                 yellowCardsB=0, redCardsB=0, yellowRedCardsB=0):

        assert type(teamA) is str
        assert type(teamB) is str

        # Check group stages...
        for group in self.groups:
            groupTeams = [team.name for team in group.teams]
            if teamA in groupTeams and teamB in groupTeams:
                group.playGame(teamA, teamB,
                               teamAgoals, teamBgoals,
                               teamApenalties, teamBpenalties)

                if group.complete:
                    pass


        # ... and also knockout stages.

    def __str__(self):
        # Code in to print knockout if group stages are complete.
        status = ''

        for group in self.groups:
            status += str(group) + '\n'

        status = status[:-1]

        return status
