class Player:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def __str__(self):
        return f"{self.name} ({self.role})"

class Fielder(Player):
    def __init__(self, name, role="Fielder"):
        super().__init__(name, role)
    
class Batter(Fielder):
    def __init__(self, name):
        super().__init__(name, "Batter")

class Bowler(Fielder):
    def __init__(self, name):
        super().__init__(name, "Bowler")
    
class AllRounder(Fielder):
    def __init__(self, name):
        super().__init__(name, "All-Rounder")

class Captain(Fielder):
    def __init__(self, name):
        super().__init__(name, "Captain (Batter/Bowler)")
    
    def lead_team(self):
        return f"{self.name} is leading the team."

class WicketKeeper(Batter):
    def __init__(self, name):
        super().__init__(name)
        self.role = "Wicketkeeper/Batter"
    
    def keep_wickets(self):
        return f"{self.name} is keeping wickets."

class Team:
    def __init__(self, name):
        self.name = name
        self.players = []
        self.captain = None
        self.wicketkeeper = None
    
    def add_player(self, player):
        if len(self.players) < 11:
            self.players.append(player)
        else:
            print("Cannot add more than 11 players.")
    
    def assign_captain(self, captain):
        if captain in self.players:
            self.captain = captain
        else:
            print("Captain must be a part of the team.")
    
    def assign_wicketkeeper(self, wicketkeeper):
        if wicketkeeper in self.players:
            self.wicketkeeper = wicketkeeper
        else:
            print("Wicketkeeper must be a part of the team.")
    
    def display_team(self):
        print(f"Team {self.name}:")
        for player in self.players:
            print(f" - {player}")
        print()

class Match:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
    
    def start_match(self):
        print(f"Match between {self.team1.name} and {self.team2.name} has started!\n")
        self.team1.display_team()
        self.team2.display_team()

# Creating teams
team_mi = Team("MI")
team_rcb = Team("RCB")

# Creating players for MI
players_mi = [
    Captain("Rohit Sharma"),
    WicketKeeper("Ishan Kishan"),
    Batter("Suryakumar Yadav"), Batter("Tilak Varma"), Batter("Dewald Brevis"), Batter("Tim David"), Batter("Nehal Wadhera"),
    AllRounder("Hardik Pandya"), AllRounder("Cameron Green"),
    Bowler("Jasprit Bumrah"), Bowler("Piyush Chawla")
]

# Creating players for RCB
players_rcb = [
    Captain("Faf du Plessis"),
    WicketKeeper("Dinesh Karthik"),
    Batter("Virat Kohli"), Batter("Rajat Patidar"), Batter("Anuj Rawat"), Batter("Mahipal Lomror"), Batter("Suyash Prabhudessai"),
    AllRounder("Glenn Maxwell"), AllRounder("Cameron Green"),  # Used Green in both, just for fun
    Bowler("Mohammed Siraj"), Bowler("Karn Sharma")
]

# Adding players to MI
for player in players_mi:
    team_mi.add_player(player)

team_mi.assign_captain(players_mi[0])
team_mi.assign_wicketkeeper(players_mi[1])

# Adding players to RCB
for player in players_rcb:
    team_rcb.add_player(player)

team_rcb.assign_captain(players_rcb[0])
team_rcb.assign_wicketkeeper(players_rcb[1])

# Starting a match
match = Match(team_mi, team_rcb)
match.start_match()
