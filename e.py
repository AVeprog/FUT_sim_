# chosen_list = self.choose_players()  # Получаем список игроков для текущей игры
# team_label = self.choose_teams(chosen_list, opponent)
# for minute in range(0, 90, 10):  # Проходим по каждой минуте в диапазоне от 0 до 75
#     if minute != 0:
#         if minute == 70:
#             if substitution_needed == 0:
#                 if add_player in sorted_list:
#                     sorted_list.remove(add_player)
#                     print(f'{minute} minute - substitution: {add_player}, Dream Team FC')
#             else:
#                 break
#         else:
#             if random.randint(0, 100) < 60:  # Примерно 10% шанс на гол в каждую минуту
#                 player_scored = random.choice(sorted_list)
#                 if player_scored == add_player:
#                     substitution_needed = 1
#                 if player_scored in sorted_list[16:]:
#                     # print(sorted_list[16:])
#                     scoring_team = opponent if player_scored in self.oplayers else 'Dream Team FC'
#                     print(f'{minute} minute - goal scored by {player_scored}, {scoring_team}')
#                 else:
#                     if random.randint(0, 100) < 10:
#                         scoring_team = opponent if player_scored in self.oplayers else 'Dream Team FC'
#                         print(f'{minute} minute - goal scored by {player_scored}, {scoring_team}')
