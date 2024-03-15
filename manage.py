import pygame
import sys
from bullet import Bullet
from bot import Bot
import time


def events(gun, screen, bullets):
    """Обрабтка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # закрывает окно

        elif event.type == pygame.KEYDOWN:  # Если тип события - нажатая клавиша
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # вправо
                gun.move_right = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  # влево
                gun.move_left = True
            elif event.key == pygame.K_SPACE:  # пробел
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:  # Если клавиша отжата
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # вправо
                gun.move_right = False
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  # влево
                gun.move_left = False


def screen_update(background_color, screen, stats, sc, gun, bots, bullets):
    """Обовление экрана"""
    screen.fill(background_color)  # передача фонового цвета
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output_gun()
    bots.draw(screen)
    pygame.display.flip()  # проресовка последнего экрана


def update_bullets(screen, bots, stats, sc, bullets):
    """Обновлять позиции пуль, удаляет пулю, когда она уходит за экран"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, bots, True, True)
    if collisions:
        for bots in collisions.values():
            stats.score += 10 * len(bots)
        sc.image_score()
        sc.image_lifes()
        check_record(stats, sc)
    if len(bots) == 0:
        bullets.empty()
        compose_army(screen, bots)


def update_bot(stats, screen, gun, bots, bullets):
    """Обновление позиции ботов"""
    bots.update()
    if pygame.sprite.spritecollideany(gun, bots):
        gun_kill(stats, screen, gun, bots, bullets)
    check_bottom_bots(stats, screen, gun, bots, bullets)


def check_bottom_bots(stats, screen, gun, bots, bullets):
    """Дошли ли боты до низа экрана?"""
    screen_rect = screen.get_rect()
    for bot in bots.sprites():
        if bot.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, bots, bullets)
            break


def compose_army(screen, bots):
    """Создание Армии ботов"""
    bot = Bot(screen)
    bot_width = bot.rect.width
    bot_height = bot.rect.height
    n_botsx = int((700 - 2 * bot_width) / bot_width)
    n_botsy = int((700 - 100 - 3 * bot_height) / bot_height)

    for bot_rows in range(n_botsy - 6):
        for bot_n in range(n_botsx):
            bot = Bot(screen)
            bot.x = bot_width + bot_width * bot_n
            bot.y = bot_height + bot_height * bot_rows
            bot.rect.y = bot.rect.height + bot.rect.height * bot_rows
            bot.rect.x = bot.x
            bots.add(bot)


def gun_kill(stats, screen, gun, bots, bullets):
    """Столкновении пушки и армии"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        bots.empty()
        bullets.empty()
        compose_army(screen, bots)
        gun.reset_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()


def check_record(stats, sc):
    """Проверка новых рекордов"""
    if stats.score > stats.record:
        stats.record = stats.score
        sc.record_score()
        with open(r'D:\coding\MyFirstGame\record.txt', 'w', encoding='utf-8') as file:
            file.write(str(stats.record))
