import pygame


class Gun():
    def __init__(self, screen):
        """Инициализация пушки"""
        self.screen = screen
        self.image = pygame.image.load(
            r'D:\coding\MyFirstGame\images\12.png')      # загрузка изображения
        # графический объект на котором находится изображение
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()  # объект экрана
        # выраниваем координаты изображения по центру нашего экрана
        self.rect.centerx = self.screen_rect.centerx
        # self.center = float(self.rectangle.centerx)               #делаем вещественным для плавности (не получилось))
        self.rect.bottom = self.screen_rect.bottom  # выравниваем по низу
        self.move_right = False
        self.move_left = False

    def output_gun(self):
        """рисует пушку"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """Обновление позиции пушки"""
        if self.move_right and self.rect.right <= self.screen_rect.right:
            self.rect.centerx += 1
        if self.move_left and self.rect.left >= self.screen_rect.left:
            self.rect.centerx -= 1

    def reset_gun(self):
        """размещает пушку по центру внизу"""
        self.center = self.rect.centerx
