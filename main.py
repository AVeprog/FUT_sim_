from consequences import Consequences
from simulation import Simulation
from interview import Interview

# from media import Media
# from loyalty import Loyalty


if __name__ == '__main__':
    print('This is the start of your career. What is your name?')
    name = input('Enter your name: ')
    print('\n\nWelcome to Dream Team FC, ' + name + '!')
    print('\n\n📧 We also remind you that your loyalty to the club is at the level 0. The club believes in you and expects you to behave carefully and responsibly both on and off the field!')


    print('📧 Your media indicator is 0k subscribers')

    simulation_instance = Simulation()
    simulation_instance.add_player(name)  # Добавляем имя игрока в список игроков в классе Simulation

    consequences_instance = Consequences()
    interview = Interview()
    current_media = consequences_instance.get_media()
    current_loyalty = consequences_instance.get_loyalty()
    # interview_instance = Interview()
    # simulation_instance.display_players()

match_count = 0
game_count = match_count + 1


while match_count < 4:

    p_risk = current_loyalty
    # p_risk = loyalty_instance.value
    if p_risk != 2:
        # # p_media = media_instance.Media()
        # p_media = current_media

        while True:

            answer: str = input('\n\nReady to start the next match? (Yes/No): ')
            if answer.lower() == "yes":
                simulation_instance.match_simulation(name)
                interview.start_interview()
                # p_media = consequences_instance.get_media()
                break
            elif answer.lower() == "no":
                print('Okay, we''ll ask later.')
            else:
                print('Enter the correct answer (Yes/No).')
        if p_risk > 0:  # Проверяем, если p_risk > 0
            risk_flag = True  # Устанавливаем флаг в True
    else:
        print(
            '\n\n📧We inform you that your contract was terminated due to a bad influence on public opinion about the team. Your agent is already negotiating with other clubs. Stay in touch!')
        break
    match_count += 1
else:
    print(f'\n\n📧Congratulations, your first season is finished.')
    loyalty_score = interview.loyal_score

    if int(loyalty_score) >= 4:
        print('\n\n📧At the moment, the agent and the club management are discussing a contract extension. Stay in touch!')
        print('\n\n🏆 Congratulations on your behavior both on and off the field that is beyond praise. You receive a loyalty bonus equal to one month''s salary! At the moment, the agent and the club management are discussing a contract extension. Stay in touch!')


    # if risk_flag:  # Проверяем значение флага после завершения цикла
    #     print('At the moment, the agent and the club management are discussing a contract extension. Stay in touch!')
    # else:
    #     print(
    #         '📧Congratulations on your behavior both on and off the field that is beyond praise. You receive a loyalty bonus equal to one month''s salary! At the moment, the agent and the club management are discussing a contract extension. Stay in touch!')
