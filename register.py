def process_namelist():
    f = open("namelist.txt")        # Open file to get the content as string
    content = f.read()
    f.close()
    #print(content)
    teamlist = content.split(sep="\n\n")        # Split the content into a list of strings
    ##print(teamlist)
    for i in range(len(teamlist)):      # Loop through the list of teams
        teamlist[i] = teamlist[i].split(sep="\n")       # Split each team into a list of strings
    return(display_teamlist(teamlist))

def display_teamlist(teamlist):
    layout = "{0:<20} {1:<20}"
    #layout = "{0:<20} {1:<20} {2:<20} {3:<20}"
    for i in range(len(teamlist[0])):
        print(layout.format(teamlist[0][i],teamlist[1][i]), end="\n\n")    # Print the list of teams in a table
       # print(layout.format(teamlist[0][i],teamlist[1][i],teamlist[2][i],teamlist[3][i]), end="\n\n")    # Print the list of teams in a table
    input("Press Enter to continue...")
    return(create_team_obj(teamlist))
    print("There are {0} teams in the file.".format(len(teamlist)))

def create_team_obj(teamlist):
    f_team = list()
    for i in range(len(teamlist)):
        team_name = teamlist[i][0]
        players = teamlist[i][1:5]
        #print("TYPE",team_name,names)

        teams = team(team_name, players, 0)
        f_team.append(teams)
        print(f_team[i])
    print("Team object list f_team created successfully")
    return (f_team)
        

class team():       # Create a class for teams
    def __init__(self, team_name, names, score = 0):
        self.team_name = team_name
        self.players = list(names)
        self.score = score

    def __str__(self):
        return ("{0} {1} \nScore: {2}\n".format(self.team_name, self.players, self.score))

class player(team):     # Create a class for players
    def __init__(self, name, team_name):
        self.name = name
        self.team_name = team_name


#process_namelist()
