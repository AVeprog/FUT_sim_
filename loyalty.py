class Loyalty:
    def __init__(self):
        self.value = 0  # Начальное значение лояльности

    def balancing_loyalty(self):
        if self.value != 0:  # Если значение не равно 0
            if self.value > 0:  # Если значение положительное
                self.value = max(self.value - 1, 0)  # Уменьшаем значение на 1, ограничивая минимальное значение 0
            else:  # Если значение отрицательное
                self.value = min(self.value + 1, 0)  # Увеличиваем значение на 1, ограничивая максимальное значение 0
        return self.value

    def increase_loyalty(self):
        if self.value < 0:  # Если значение отрицательное
            self.value = min(self.value + 1, 0)  # Увеличиваем значение на 1, ограничивая максимальное значение 0
        elif self.value > 0:  # Если значение положительное
            value = max(self.value - 1, 0)  # Уменьшаем значение на 1, ограничивая минимальное значение 0
        return self.value

    def decrease_loyalty(self):
        if self.value > 0:  # Если значение положительное
            self.value = max(self.value - 1, 0)  # Уменьшаем значение на 1, ограничивая минимальное значение 0
        elif self.value < 0:  # Если значение отрицательное
            value = min(self.value + 1, 0)  # Увеличиваем значение на 1, ограничивая максимальное значение 0
        return self.value

    def get_loyalty(self):
        return self.value


loyalty_instance = Loyalty()

# print('Your loyalty level: Comfortable\nYou are in the starting lineup for the next match')
# print('Your loyalty level: Passive\nYou are in the starting lineup for the next match')
# print('Your loyalty level: Active\nYou are in the starting lineup for the next match')
# print('Your loyalty level: Calm\nYou are in the starting lineup for the next match')
# print('Your loyalty level: Aggressive\nYou are in the starting lineup for the next match')
# print('Your loyalty level: Aggressive\nYou will start the next match from the bench')
