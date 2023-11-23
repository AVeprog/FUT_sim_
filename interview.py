from consequences import Consequences


class Interview:
    def __init__(self):
        self.consequences = Consequences()
        self.loyalty = self.consequences.get_loyalty()
        self.media = self.consequences.get_media()
        self.prev_media = None
        self.loyal_score = 0

    def start_interview(self):
        while True:
            answer: str = input('\n\nReady to give a post-match interview? (Yes/No): ')
            if answer.lower() == "yes":
                self.interview()
                print(f'Current media: {self.consequences.get_media()}k')
                print(f'Current loyalty: {self.consequences.get_loyalty()}')
                loyalty_value = self.consequences.get_loyalty()
                # print(f'Current loyalty: {loyalty_value}')

                if int(loyalty_value) == 0:
                    self.loyal_score += 1
                    # print(f'Current loyalty score: {self.loyal_score}')
                    # print(self.loyal_score)
                    # Увеличиваем счётчик
                else:
                    break

                if self.prev_media is not None and self.consequences.get_media() >= 40 > self.prev_media:
                    print(
                        '🏆 Congratulations, your media exposure has reached 100k subscribers, from now on you have access to a new source of income through social networks')

                self.prev_media = self.consequences.get_media()
                break

            elif answer.lower() == "no":
                answer: str = input(
                    '\n\nAre you sure you don''t want to perform at the interview? The fans will be disappointed! (Yes/No): ')
                if answer.lower() == "no":
                    self.interview()
                    print(f'Current media: {self.consequences.get_media()}k')
                    print(f'Current loyalty: {self.consequences.get_loyalty()}')

                    loyalty_value = self.consequences.get_loyalty()
                    # print(f'Current loyalty: {loyalty_value}')

                    if int(loyalty_value) == 0:
                        self.loyal_score += 1
                        # print(f'Current loyalty score: {self.loyal_score}')
                        # print(self.loyal_score)
                        # Увеличиваем счётчик
                    else:
                        break

                    if self.prev_media is not None and self.consequences.get_media() >= 40 > self.prev_media:
                        print(
                            '🏆 Congratulations, your media exposure has reached 100k subscribers, from now on you have access to a new source of income through social networks')

                    self.prev_media = self.consequences.get_media()

                    break
                elif answer.lower() == "yes":
                    a=2
                    b=2
                    self.consequences.freezing()
                    print('\n\n📧 Your interview failed, but there were no problems.')
                    print(f'Current media: {self.consequences.get_media()}k')
                    print(f'Current loyalty: {self.consequences.get_loyalty()}')
                    loyalty_value = self.consequences.get_loyalty()
                    # print(f'Current loyalty: {loyalty_value}')

                    if int(loyalty_value) == 0:
                        self.loyal_score += 1
                        # print(f'Current loyalty score: {self.loyal_score}')
                        # print(self.loyal_score)
                        # Увеличиваем счётчик
                    else:
                        break

                    if self.prev_media is not None and self.consequences.get_media() >= 40 > self.prev_media:
                        print(
                            '🏆 Congratulations, your media exposure has reached 100k subscribers, from now on you have access to a new source of income through social networks')

                    self.prev_media = self.consequences.get_media()
                    break
                else:
                    print('\n\nEnter the correct answer (Yes/No).')
            else:
                print('\n\nEnter the correct answer (Yes/No).')

        # media_instance.interview_simulation()

    def interview(self):
        while True:
            print('Welcome to the post match interview! The question will be next, how do you evaluate teamwork?')
            print('1. We have already done excellent work with our teammates and coaches, but we do not stop working on ourselves! Together we will achieve our goals!')
            print('2. It’s difficult for me to evaluate this criterion. I think my teammates and coach will give a clearer answer.')
            print('3. I am progressing and working on myself. The coach should definitely give me more time, and my teammates should give me the ball! Only then will there be results!')

            choice = input('Enter the number of the selected answer: ')

            if choice == "1":
                self.consequences.balancing()
                print('\n\n📧 Your level of loyalty within the team and among fans has increased!')
                break
            elif choice == "2":
                self.consequences.freezing()
                print('\n\n📧 Your interview failed, but there were no problems.')
                break
            elif choice == "3":
                self.consequences.flaring()
                print('\n\n📧 You caused a stir in the media!')
                break
            else:
                print('Enter the correct answer(1/2/3).')

