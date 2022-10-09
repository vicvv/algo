'''This file contains a hint to help you work on your project.

Hint #1: 
When validating user input you will need to use a while loop and keep asking the user to enter another value
until their input satisfies the constraints outlined in the prompt. When getting the team names and scores you will 
need to place a while loop inside of a for loop, as you need to check validity for every team. You can loop through
the number of teams in the for loop and for each team ask for either a valid name of number of wins in the while loop.



Hint #2:
When gathering the wins for each team it may be helpful to create a list containing tuples of (team_name, wins).
This way you can easily sort the teams by their wins using the .sort() method or sorted() function. Since you'll want to
sort by the second element in each pairing you'll need to use the key keyword argument like this: .sort(list_to_sort, key=function) 
or sorted(list_to_sort, key=function). Refer to the "Sorting" lesson in Programming Fundamental for more information on using key=.

Hint #3: 
Once you've sorted the teams by their number of wins you can start creating games.
Doing this is as simple as matching the team with the most wins with the team with
the least wins and then repeating for all remaining teams. Take an example where we 
have 4 teams, sorted in ascending order by their wins: 

sorted_teams = ["Tigers", "Bears", "Dolphins", "Sheep"] 
game1 = (sorted_teams[-1], sorted_teams[0])  # sorted_teams[-1] is the home team
game2 = (sorted_teams[-2], sorted_teams[1])

In this example the team at index 0 and the team at index 3 need to play a game and the teams at
index 1 and index 2 need to play a game. Can you figure out how to emulate this using a 
single for loop?'''


# Write your code here.

def get_number_of_teams():
    while True:
        try:
            num_teams = int(input('Enter the number of teams in the tournament: ')) 
            if num_teams > 1 and num_teams%2 == 0:
                break
            else:
                print("Number of teams should be more than 1 and even")
                num_teams=''
                continue
        except:
            print('Input is invalid, need a NUMBER')
    return num_teams
        
    


def get_team_names(num_teams):
    print('num_teams', num_teams)
    names =[]
    i=1
    while i < num_teams+1:
        name = input(f'Enter the name for team #{i}: ')
        if len(name) <2:
            print('Team names must have at least 2 characters, try again.')
            continue
        elif len(name.split(' ')) >2:
            print('Team names may have at most 2 words, try again.')
            continue
        else:
            i +=1
            names.append(name)
    return names

    

def get_number_of_games_played(num_teams):
    min_games = num_teams-1
    while True:
        gplayed = int(input("Enter the number of games played by each team: "))
        if gplayed < min_games:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
            continue
        else:
            break
    return gplayed


def get_team_wins(team_names, games_played):
    stats={}; sm=0
    for team in team_names:
        while True:
            wins = int(input(f"Enter the number of wins Team {team} had: "))
            if sm > games_played or wins > games_played:
                print(f"The maximum number of wins is {games_played}, try again.")
            elif wins < 0:
                print("The minimum number of wins is 0, try again.")
            else:
                sm += wins               
                break
        stats[team] = stats.get(team,0) + wins
    return stats
    
        
        
        


# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
games_played = get_number_of_games_played(num_teams)
team_wins = get_team_wins(team_names, games_played)
tw = sorted([(k,v) for k,v in team_wins.items()], key=lambda item:item[1])
print(tw)

print("Generating the games to be played in the first round of the tournament...")
homet = tw[:len(tw)//2]
awayt = tw[len(tw)//2:][::-1]

for t in range(len(homet)):
    print(f'Home: {homet[t][0] }VS Away: {awayt[t][0]}')
