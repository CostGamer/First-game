import pygame


class Bot(pygame.sprite.Sprite):
    """Класс одного пришельца"""

    def __init__(self, screen):
        """Инициализируем и задаем начальную позиуию"""
        super(Bot, self).__init__()
        self.screen = screen
        self.image = pygame.image.load(
            r'D:\coding\MyFirstGame\images\123.png')      # загрузка изображения
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_bot(self):
        """рисует бота"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Перемещает прищельцев"""
        self.y += 0.05
        self.rect.y = self.y
