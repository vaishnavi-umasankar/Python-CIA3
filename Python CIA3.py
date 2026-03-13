#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Team:
    def __init__(self, team_name, captain, batsmen, bowlers, all_rounders):
        self.team_name = team_name
        self.captain = captain
        self.batsmen = batsmen
        self.bowlers = bowlers
        self.all_rounders = all_rounders

    def display_team(self):
        print(f"Team: {self.team_name:15} | Capt: {self.captain:12} | Bat: {self.batsmen} | Bowl: {self.bowlers} | AR: {self.all_rounders}")

class Player:
    def __init__(self, player_id, player_name, team_name):
        self.player_id = player_id
        self.player_name = player_name
        self.team_name = team_name

class MatchRecord(Team):
    def __init__(self, team_obj, opponent, score, result, date):
        # Inheriting from the Team base class using an existing Team object
        super().__init__(team_obj.team_name, team_obj.captain, team_obj.batsmen, 
                         team_obj.bowlers, team_obj.all_rounders)
        self.opponent = opponent
        self.score = score
        self.result = result
        self.date = date

    def display_match(self):
        print(f"Date: {self.date:10} | {self.team_name:10} vs {self.opponent:10} | Score: {self.score:6} | Result: {self.result}")

class TournamentSystem:
    def __init__(self):
        # We store keys in lowercase to avoid "Team doesn't exist" errors
        self.teams = {} 
        self.players = []
        self.matches = []

    def add_team(self, *args):
        try:
            if len(args) == 0:
                name = input("Enter Team Name: ").strip()
                cap = input("Enter Captain Name: ").strip()
                bat = int(input("Number of Batsmen: "))
                bowl = int(input("Number of Bowlers: "))
                ar = int(input("Number of All Rounders: "))
                self.teams[name.lower()] = Team(name, cap, bat, bowl, ar)
                print(f"Success: Team '{name}' registered.")
            elif len(args) == 5:
                name, cap, bat, bowl, ar = args
                self.teams[name.lower()] = Team(name, cap, bat, bowl, ar)
        except ValueError:
            print("Input Error: Batsmen, Bowlers, and All-rounders must be integers.")

    def add_player(self, *args):
        try:
            if len(args) == 0:
                p_id = input("Enter Player ID: ").strip()
                p_name = input("Enter Player Name: ").strip()
                t_search = input("Enter Team Name to join: ").strip().lower()
                
                if t_search not in self.teams:
                    raise KeyError(f"Team '{t_search}' not found. Current teams: {list(self.teams.keys())}")
                
                self.players.append(Player(p_id, p_name, self.teams[t_search].team_name))
                print(f"Success: {p_name} added to {self.teams[t_search].team_name}.")
            elif len(args) == 3:
                p_id, p_name, t_name = args
                if t_name.lower() not in self.teams: raise KeyError("Team not found.")
                self.players.append(Player(p_id, p_name, self.teams[t_name.lower()].team_name))
        except KeyError as e:
            print(f"Key Error: {e}")

    def add_match_record(self, *args):
        try:
            if len(args) == 0:
                t_name = input("Your Team Name: ").strip().lower()
                if t_name not in self.teams: raise KeyError("Team not found.")
                opp = input("Opponent Team Name: ").strip()
                score = input("Score (e.g. 150/5): ").strip()
                res = input("Result (Win/Loss): ").strip()
                date = input("Date (YYYY-MM-DD): ").strip()
                self.matches.append(MatchRecord(self.teams[t_name], opp, score, res, date))
                print("Match recorded successfully.")
            elif len(args) == 5:
                t_name, opp, score, res, date = args
                if t_name.lower() not in self.teams: raise KeyError("Team not found.")
                self.matches.append(MatchRecord(self.teams[t_name.lower()], opp, score, res, date))
        except Exception as e:
            print(f"Error: {e}")

    def update_match_record(self):
        try:
            t_name = input("Enter Team Name to update score: ").strip().lower()
            found = False
            for m in self.matches:
                if m.team_name.lower() == t_name:
                    m.score = input("Enter updated score: ").strip()
                    m.result = input("Enter updated result: ").strip()
                    print("Update successful.")
                    found = True
                    break
            if not found: print("No match records found for that team.")
        except Exception as e:
            print(f"Runtime Error: {e}")

    def search_team(self):
        name = input("Enter Team Name to search: ").strip().lower()
        if name in self.teams:
            self.teams[name].display_team()
        else:
            print("Team not found in system.")

    def display_match_record(self):
        print("\n--- MATCH HISTORY ---")
        if not self.matches: print("No matches recorded yet.")
        for m in self.matches: m.display_match()

    def display_players(self):
        print("\n--- PLAYER ROSTER ---")
        if not self.players: print("No players registered yet.")
        for p in self.players:
            print(f"ID: {p.player_id:5} | Name: {p.player_name:15} | Team: {p.team_name}")

    def menu(self):
        while True:
            print("\n" + "="*30)
            print(" TOURNAMENT MANAGEMENT SYSTEM")
            print("="*30)
            print("1. Add Team\n2. Add Player\n3. Add Match Record\n4. Update Match\n5. Search Team\n6. View All Matches\n7. View All Players\n8. Exit")
            choice = input("\nSelect an option (1-8): ").strip()
            
            if choice == '1': self.add_team()
            elif choice == '2': self.add_player()
            elif choice == '3': self.add_match_record()
            elif choice == '4': self.update_match_record()
            elif choice == '5': self.search_team()
            elif choice == '6': self.display_match_record()
            elif choice == '7': self.display_players()
            elif choice == '8': 
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid selection. Please try again.")

# Main Execution
if __name__ == "__main__":
    tournament = TournamentSystem()
    tournament.menu()

    


# In[ ]:




