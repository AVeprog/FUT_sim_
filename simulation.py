import random
import re


class Simulation:
    def __init__(self):

        self.added_player_name = None
        self.players = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9', 'p10']
        self.oplayers = ['op1', 'op2', 'op3', 'op4', 'op5', 'op6', 'op7', 'op8', 'op9', 'op10', 'op11']
        self.opponents = ['Team A', 'Team B', 'Team C', 'Team D', 'Team E']
        self.game_count = 1

    def add_player(self, name):
        self.players.append(name)
        self.added_player_name = name

    def display_players(self):
        print('List of players:', self.players)

    def generate_unique_opponents(self, count):
        return random.sample(self.opponents, count) if count <= len(self.opponents) else self.opponents

    def choose_players(self):
        all_players = self.players + self.oplayers
        return random.sample(all_players, len(all_players))

    @staticmethod
    def sort_players(players):
        def extract_number(s):
            matches = re.findall(r'\d+', s)
            return int(matches[0]) if matches else float('inf')

        return sorted(players, key=extract_number)

    def match_simulation(self, add_player):
        unique_opponents = self.generate_unique_opponents(1)
        opponent = unique_opponents[0] if unique_opponents else "No opponents available"

        dream_team_score = 0
        opponent_team_score = 0

        sorted_list = self.sort_players(self.choose_players())
        substitution_needed = 0

        print('\n\nGAME ' + str(self.game_count + 1))
        self.game_count += 1
        print('Dream Team FC - ' + opponent + '   0 : 0')

        for minute in range(0, 90, 1):
            if minute != 0:
                if minute == 70:
                    if substitution_needed == 0:
                        if add_player in sorted_list:
                            sorted_list.remove(add_player)
                            print(f'{minute} minute - substitution: {add_player}, Dream Team FC')
                        else:
                            break
                    else:
                        break
                else:
                    if random.randint(0, 100) < 10:
                        player_scored = random.choice(sorted_list)
                        if player_scored == add_player:
                            substitution_needed = 1

                        if player_scored in sorted_list[16:]:
                            scoring_team = opponent if player_scored in self.oplayers else 'Dream Team FC'
                            print(f'{minute} minute - goal scored by {player_scored}, {scoring_team}')
                            if scoring_team == 'Dream Team FC':
                                dream_team_score += 1  # Увеличиваем счётчик
                            else:
                                opponent_team_score += 1

                        else:
                            if random.randint(0, 100) < 5:
                                scoring_team = opponent if player_scored in self.oplayers else 'Dream Team FC'
                                print(f'{minute} minute - goal scored by {player_scored}, {scoring_team}')
                                if scoring_team == 'Dream Team FC':
                                    dream_team_score += 1  # Увеличиваем счётчик
                                else:
                                    opponent_team_score += 1

        print(f'Final Score: Dream Team FC - {opponent} {dream_team_score} : {opponent_team_score}')
