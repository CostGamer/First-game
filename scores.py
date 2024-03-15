import pygame.font
from gun import Gun


class Scores():
    """Вывод игровой инфы"""

    def __init__(self, screen, stats):
        """Инициализация подсчета очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.record_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 25)
        self.image_score()  # Отрисовывает шрифт на экране
        self.record_score()
        self.image_lifes()

    def image_score(self):
        """Преобразовывает текст счета в графическое изображение"""
        self.score_img = self.font.render(
            f'Очки = {str(self.stats.score)}', True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.left = 500  # Разм0ещение от правого края экрана
        self.score_rect.top = 0  # Размещение от верхнего края

    def image_lifes(self):
        """Показывает жизни"""
        self.lifes = self.font.render(
            f'Жизни = {str(self.stats.guns_left)}', True, self.text_color, (0, 0, 0))
        self.lifes_rect = self.lifes.get_rect()
        self.lifes_rect.left = 0  # Размещение от правого края экрана
        self.lifes_rect.top = 0  # Размещение от верхнего края

    def show_score(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.record_image, self.score_record)
        self.screen.blit(self.lifes, self.lifes_rect)

    def record_score(self):
        """Рекорд"""
        self.record_image = self.font.render(
            f'Рекорд = {str(self.stats.record)}', True, self.record_color, (0, 0, 0))
        self.score_record = self.record_image.get_rect()
        self.score_record.left = 250  # Размещение от правого края экрана
        self.score_record.top = 0  # Размещение от верхнего края
