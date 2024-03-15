import pygame
import manage
import sys
from gun import Gun
from pygame.sprite import Group
from game_stats import Stats
from scores import Scores


def run():
    pygame.init()  # инициализировали игру
    screen = pygame.display.set_mode(size=(00, 700))  # графическое окно
    pygame.display.set_caption("Space batle")           # надпись
    background_color = (0, 0, 0)  # цвет фона в формате RGB
    gun = Gun(screen)
    bullets = Group()
    bots = Group()
    manage.compose_army(screen, bots)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:  # цикл, в котором мы будем обрабатывать действия пользователя в игре
        manage.events(gun, screen, bullets)
        if stats.run_game:
            gun.update_gun()
            manage.screen_update(background_color, screen,
                                 stats, sc, gun, bots, bullets)
            manage.update_bullets(screen, bots, stats, sc, bullets)
            manage.update_bot(stats, screen, gun, bots, bullets)


run()
