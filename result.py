# class team():       # Create a class for teams
#     def __init__(self, team_name, names, score = 0):
#         self.team_name = team_name
#         self.players = list(names)
#         self.score = score

# f_team = list()
# f_team.append(team("Team A", ["Player A", "Player B", "Player C", "Player D"],3))
# f_team.append(team("Team B", ["Player E", "Player F", "Player G", "Player H"],4))
# f_team.append(team("Team C", ["Player I", "Player J", "Player K", "Player L"],10))
# f_team.append(team("Team D", ["Player M", "Player N", "Player O", "Player P"],6))
# f_team.append(team("Team E", ["Player Q", "Player R", "Player S", "Player T"],12))

def sorting_result(f_team):
    f_team.sort(key=lambda x: x.score, reverse=True)
    ranking = []
    for team in f_team:
        ranking.append(team.team_name)
    #print(ranking)
    showing_result(ranking)

def showing_result(ranking):
    print("The ranking is:")
    for i in range(len(ranking)):
        print("{0} {1}".format(i+1, ranking[i]))