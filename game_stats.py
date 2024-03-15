class Stats:
    """Статистика текущей игры"""

    def __init__(self):
        """Инициализирует статистику"""
        self.reset_stats()
        self.run_game = True  # Если True продолжаем, если False выходим из игры

        with open(r'D:\coding\MyFirstGame\record.txt', 'r', encoding='utf-8') as file:
            self.record = int(file.readline())

    def reset_stats(self):
        """Статистика измен. во время игры"""
        self.guns_left = 2
        self.score = 0
