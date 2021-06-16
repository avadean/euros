import data as d
import tournament as t

groups = {'A': d.groupA,
          'B': d.groupB,
          'C': d.groupC,
          'D': d.groupD,
          'E': d.groupE,
          'F': d.groupF
          }


tournament = t.getTournament(groups)

tournament.playGame('Turkey', 'Italy', 0, 3, yellowCardsA=2)
tournament.playGame('Wales', 'Switzerland', 1, 1, yellowCardsA=1, yellowCardsB=2)
tournament.playGame('Denmark', 'Finland', 0, 1, yellowCardsB=2)
tournament.playGame('Belgium', 'Russia', 3, 0, )
tournament.playGame('England', 'Croatia', 1, 0, yellowCardsA=1, yellowCardsB=3)
tournament.playGame('Austria', 'North Macedonia', 3, 1, yellowCardsA=1, yellowCardsB=2)
tournament.playGame('Netherlands', 'Ukraine', 3, 2, yellowCardsB=1)
tournament.playGame('Scotland', 'Czech Republic', 0, 2)
tournament.playGame('Poland', 'Slovakia', 1, 2, redCardsA=1, yellowCardsB=1)
tournament.playGame('Spain', 'Sweden', 0, 0, yellowCardsB=1)
tournament.playGame('Hungary', 'Portugal', 0, 3, yellowCardsA=2, yellowCardsB=1)
tournament.playGame('France', 'Germany', 1, 0, yellowCardsB=1)
tournament.playGame('Finland', 'Russia', 0, 1, yellowCardsA=2, yellowCardsB=3)
tournament.playGame('Turkey', 'Wales', 0, 2, yellowCardsA=2, yellowCardsB=2)
tournament.playGame('Italy', 'Switzerland', 3, 0, yellowCardsB=2)

print(tournament)
