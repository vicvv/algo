'''
Given an array of pairs representing the team that cave competed agains
each other and the array of the results of each competition, write the
function that returns the winner of the turnament
0 - away team won, 1 home team won.
win means +3 points
'''

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
