#@Zero_Paradox

import pygame
import time
import random
import os


def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')


clear()
print("__Zero_Paradox__")
print("")
print("--> Run with Python3 <--")
print("")
pygame.init()
crash_sound = pygame.mixer.Sound("Lose.wav")
pygame.mixer.music.load("Trance.mp3")

# display_width and display_height for windows game ----------
display_width = 800
display_height = 600
white = (255, 255, 255)

# Game Color ----------
black = (0, 0, 0)
blue = (204, 255, 230)
red = (240, 0, 0)
bright_red = (255, 0, 20)
green = (0, 190, 0)
bright_green = (1, 234, 20)
gameDisplay = pygame.display.set_mode((display_width, display_height))

# Game Name & Propertise ----------
pygame.display.set_caption('Stop or Go')
clock = pygame.time.Clock()
CarImg = pygame.image.load('1.png')
car_width = 48


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "play":
                game_loop()
            elif action == "Exit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    TextSurf, TextRect = text_objects(msg, smallText)
    TextRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(TextSurf, TextRect)


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(blue)
        largeText = pygame.font.Font('freesansbold.ttf', 100)
        TextSurf, TextRect = text_objects("Let's Play", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)
        button("Play", 150, 450, 100, 50, green, bright_green, "play")
        button("Exit", 550, 450, 100, 50, red, bright_red, "Exit")
        pygame.display.update()


def stuff_dodged(count):
    #Score----------
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score : " + str(count), True, black)
    gameDisplay.blit(text, (1, 1))


def stuff(stuffx, stuffy, stuffw, stuffh, color):
    pygame.draw.rect(gameDisplay, color, [stuffx, stuffy, stuffw, stuffh])


def Car(x, y):
    gameDisplay.blit(CarImg, (x, y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()


def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    largeText = pygame.font.Font('freesansbold.ttf', 100)
    TextSurf, TextRect = text_objects("Game Over", largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Play more", 150, 450, 100, 50, green, bright_green, "play")
        button("Exit", 550, 450, 100, 50, red, bright_red, "Exit")
        pygame.display.update()


def game_loop():
    pygame.mixer.music.play(-1)
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    stuff_startx = random.randrange(0, display_width)
    stuff_starty = -700
    stuff_speed = 7
    stuff_width = 75
    stuff_height = 75
    dodged = 0
    GameExit = False
    while not GameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -6
                elif event.key == pygame.K_RIGHT:
                    x_change = 6
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gameDisplay.fill(blue)
        
        # Stuffx, Stuffy, Stuffw, Stuffh, Color ----------
        stuff(stuff_startx, stuff_starty, stuff_width, stuff_height, red)
        stuff_starty += stuff_speed
        stuff_dodged(dodged)
        Car(x, y)
        if x > display_width - car_width or x < 0:
            crash()
        if stuff_starty > display_height:
            stuff_startx = random.randrange(0, display_width)
            stuff_starty = 0 - stuff_height
            dodged += 1
            if dodged % 7 == 0:
                stuff_speed += 1
                stuff_width += 13
                stuff_height += 13
        if y < stuff_starty + stuff_height:
            if stuff_startx < x < stuff_startx + stuff_width or stuff_startx < x + car_width < stuff_startx + car_width:
                crash()
        pygame.display.update()
        clock.tick(110)


game_intro()
game_loop()
pygame.quit()
quit()
