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
tournament.playGame('Ukraine', 'North Macedonia', 2, 1, yellowCardsA=1, yellowCardsB=2)
tournament.playGame('Denmark', 'Belgium', 1, 2, yellowCardsA=3, yellowCardsB=1)
tournament.playGame('Netherlands', 'Austria', 2, 0, yellowCardsA=1, yellowCardsB=2)
tournament.playGame('Sweden', 'Slovakia', 1, 0, yellowCardsA=1, yellowCardsB=3)
tournament.playGame('Croatia', 'Czech Republic', 1, 1, yellowCardsA=1, yellowCardsB=3)
tournament.playGame('England', 'Scotland', 0, 0, yellowCardsB=2)
tournament.playGame('Hungary', 'France', 1, 1, yellowCardsA=1, yellowCardsB=1)
tournament.playGame('Portugal', 'Germany', 2, 4, yellowCardsB=2)
tournament.playGame('Spain', 'Poland', 1, 1, yellowCardsA=2, yellowCardsB=4)
tournament.playGame('Italy', 'Wales', 1, 0, yellowCardsA=1, yellowCardsB=2, redCardsB=1)
tournament.playGame('Switzerland', 'Turkey', 3, 1, yellowCardsA=1, yellowCardsB=3)
tournament.playGame('Ukraine', 'Austria', 0, 1)
tournament.playGame('North Macedonia', 'Netherlands', 0, 3, yellowCardsA=4)
tournament.playGame('Russia', 'Denmark', 1, 4, yellowCardsA=2, yellowCardsB=1)
tournament.playGame('Finland', 'Belgium', 0, 2)
tournament.playGame('Croatia', 'Scotland', 3, 1, yellowCardsA=1, yellowCardsB=1)
tournament.playGame('Czech Republic', 'England', 0, 1, yellowCardsA=1)
tournament.playGame('Sweden', 'Poland', 3, 2, yellowCardsA=1, yellowCardsB=2)
tournament.playGame('Slovakia', 'Spain', 0, 5, yellowCardsA=2, yellowCardsB=2)
tournament.playGame('Portugal', 'France', 2, 2, yellowCardsB=3)
tournament.playGame('Germany', 'Hungary', 2, 2, yellowCardsA=1, yellowCardsB=1)

print(tournament)
