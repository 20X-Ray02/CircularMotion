#                                                    ╲╲╲╲┗━━┳┳━━┛╱╱╱╱
#                                                    ╲╲╭━━╮╭┻┻╮╭━━╮╱╱
#                                                    ╲╲┃┊┊┣┫╭╮┣┫┊┊┃╱╱
#                                                    ╲╲╰━╭┻╯┃┃╰┻╮━╯╱╱
#                                                    ╲╭━╮╭━╲╭╮╱━╮╭━╮╱
#                                                    ╲┃┊┣┻━━╰╯━━┻┫┊┃╱
#                                                    ╲╰━┗━━━━━━━━┛━╯╱


import pygame
from traffic import Traffic

# Параметры для создания дисплея
pygame.init()

display_width = 1300
display_height = 700

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Круговая развязка")

icon = pygame.image.load(r"img/icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
FPS = 60

# Параметры программы
bkr_music = pygame.mixer.music.load(r"music/background.mp3")
pygame.mixer.music.set_volume(0.2)


# Печать текста на дисплее
def print_text(message, x, y, font_color=(0, 0, 0), font_type="Neris-BlackItalic.otf",
               font_size=40):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


# Пауза
def pause():
    pygame.mixer.music.pause()
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text("Пауза. Нажмите Enter, чтобы продолжить", 250, 300)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            paused = False

        pygame.display.update()
        clock.tick(15)

    pygame.mixer.music.unpause()


# Основная программа
def run_program():
    program = True
    traffic = Traffic()

    road = pygame.image.load(r"img/road.png")
    pygame.mixer.music.play(-1)

    traffic.create_car_arr()

    while program:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pause()

        display.blit(road, (0, 0))

        traffic.draw_array()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    run_program()
