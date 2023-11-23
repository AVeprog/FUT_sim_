class Media:
    def __init__(self):
        self.value = 0  # Начальное значение лояльности

    def p_increase_media(self):
        self.value += 10

    def n_increase_media(self):
        self.value += 20

    def decrease_media(self):
        self.value = max(self.value - 10, 0)

    def get_media(self):
        return self.value


media_instance = Media()
