class Consequences:
    def __init__(self):
        self.media_value = 0  # Начальное значение медиа
        self.loyalty_value = 0  # Начальное значение лояльности
        self.last_media_change = 0  # Добавляем переменные для хранения последних изменений
        self.last_loyalty_change = 0

    def set_values(self, media, loyalty):
        self.media_value = media
        self.loyalty_value = loyalty

    def balancing(self):
        self.media_value += 10
        if self.loyalty_value != 0:  # Если значение не равно 0
            if self.loyalty_value > 0:  # Если значение положительное
                self.loyalty_value = max(self.loyalty_value - 1,
                                         0)  # Уменьшаем значение на 1, ограничивая минимальное значение 0
            else:  # Если значение отрицательное
                self.loyalty_value = min(self.loyalty_value + 1,
                                         0)  # Увеличиваем значение на 1, ограничивая максимальное значение 0
        self.last_media_change = self.media_value  # Сохраняем последнее изменение в переменных
        self.last_loyalty_change = self.loyalty_value
        return self.loyalty_value, self.media_value

    def freezing(self):
        print(self.media_value)
        self.media_value -= 25
        if -2 < self.loyalty_value <= 2:  # Если значение в интервале от -2 до 2
            self.loyalty_value -= 1
        else:
            self.loyalty_value = self.loyalty_value
        self.last_media_change = self.media_value  # Сохраняем последнее изменение в переменных
        self.last_loyalty_change = self.loyalty_value
        return self.loyalty_value, self.media_value

    def flaring(self):
        self.media_value += 120
        if -2 <= self.loyalty_value < 2:  # Если значение в интервале от -2 до 2
            self.loyalty_value += 1
        else:
            self.loyalty_value = self.loyalty_value
        self.last_media_change = self.media_value  # Сохраняем последнее изменение в переменных
        self.last_loyalty_change = self.loyalty_value
        return self.loyalty_value, self.media_value

    def get_loyalty(self):
        return self.last_loyalty_change

    def get_media(self):
        return self.last_media_change


# media_instance = Loyalty()
# loyalty_instance = Loyalty()
# с_instance = Consequences()
