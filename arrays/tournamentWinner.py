'''
Given an array of pairs representing the team that cave competed agains
each other and the array of the results of each competition, write the
function that returns the winner of the turnament
0 - away team won, 1 home team won.
win means +3 points

Tournament Winner
There's an algorithms tournament taking place in which teams of programmers compete against each
other to solve algorithmic problems as fast as possible. Teams compete in a round robin, where each team
faces off against all other teams. Only two teams compete against each other at a time, and for each
competition, one team is designated the home team, while the other team is the away team. In each
competition there's always one winner and one loser; there are no ties. A team receives 3 points if it wins
and 0 points if it loses. The winner of the tournament is the team that receives the most amount of points.
Given an array of pairs representing the teams that have competed against each other and an array
containing the results of each competition, write a function that returns the winner of the tournament. The
input arrays are named competitions and results , respectively. The competitions array has
elements in the form of [homeTeam, awayTeam] , where each team is a string of at most 30 characters
representing the name of the team. The results array contains information about the winner of each
corresponding competition in the competitions array. Specifically, results[i] denotes the winner
of competitions[i] , where a 1 in the results array means that the home team in the
corresponding competition won and a 0 means that the away team won.
It's guaranteed that exactly one team will win the tournament and that each team will compete against all
other teams exactly once. It's also guaranteed that the tournament will always have at least two teams.
Sample Input
competitions = [
 ["HTML", "C#"],
 ["C#", "Python"],
 ["Python", "HTML"],
]
results = [0, 0, 1]
Sample Output
"Python"
// C# beats HTML, Python Beats C#, and Python Beats HTML.
// HTML - 0 points
// C# - 3 points
// Python - 6 points
'''


# def tournamentWinner(competitions, results):
#     dict ={}
#     for i, cmp in enumerate(competitions):
#         if results[i]:
#             dict[cmp[0]] = dict.get(cmp[0],0) + 1
#         else:
#             dict[cmp[1]] = dict.get(cmp[1],0) + 1
#     return max(dict,key=dict.get)


# teams below: at index 0 of each array we have home team and guest team in intes 2
teams = [
  ["HTML", "C#"], 
  ["C#", "Python"],
  ["Python", "HTML"]
]
results =  [0,0,1] #(home, home, wisiting)

HomeTeamWon = 1

def tournamentWinner(competitions, results):
    currentBestTeam = 0
    scores = {currentBestTeam:0}

    for indx, competition in enumerate(competitions):
        result = results[indx]
        homeTeam, awayTeam = competition

        winningTeam = homeTeam if result == HomeTeamWon else awayTeam
        updatescores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    return winningTeam


def updatescores(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points

import unittest
class TestCase(unittest.TestCase):
    def test1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        actual = tournamentWinner(competitions, results)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
