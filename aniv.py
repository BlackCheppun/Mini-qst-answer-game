import random
import sys

import easygui
import pygame
import pyperclip
from pygame import *
from pygame import locals
import time

pygame.init()
height = 600
width = 800
music = pygame.mixer.music.load("music.ogg")
def play_music():
    pygame.mixer.music.play(-1)
play_music()



screen = pygame.display.set_mode((width, height))
# import pics for background :
fb1 = pygame.image.load("1st.jpg")
fb2 = pygame.image.load("2nd.jpg")
fb3 = pygame.image.load("3rd.jpg")
fb4 = pygame.image.load("4th.jpg")
fb5 = pygame.image.load("5th.jpg")
fb6 = pygame.image.load("6th.jpg")
fb7 = pygame.image.load("7th.jpg")
fb8 = pygame.image.load("8th.jpg")
fb9 = pygame.image.load("9th.jpg")
fb10 = pygame.image.load("10th.jpg")
fb11 = pygame.image.load("11th.jpg")
fb12 = pygame.image.load("12th.png")
fb13 = pygame.image.load("13th.png")
list_of_bg = [fb1,fb2,fb3,fb4,fb5,fb6,fb6,fb7,fb8,fb9,fb10,fb11,fb12,fb13]
random.shuffle(list_of_bg)

for item in list_of_bg:
    item.convert(24)
    item.set_alpha(64)

bg_back = pygame.Surface((800, 600))
bg_back.fill((130, 130, 130))


font = pygame.font.SysFont('Helvetica', 22, bold=False, italic=False)


class text_lib:
    def __init__(self, text):
        self.text = text
        self.textshow = font.render(text, True, (0, 0, 0))
        self.rectangl = self.textshow.get_rect()


# list of questions that i was able to come up with.

list_of_qst = ['1- knowing that a plane goes at 40 foot per nanokilometer, is 1 = 0.999999...?',
               '2- knowing that the quantum computer is too fast for simple cals, is pi and pizza linked ?',
               "3- if a person's name is Hubert Blaine Wolfeschlegelsteinhausenbergerdorff Sr. what is his middle name ?",
               "4- if a couple had 69 children at their peak, how much free time did they have ? ",
               "5- knowing that 60 seconds in africa is equal to 1 minute, i contracted ligma ?",
               "6- knowing that googolplex is 10^(100 zeores), is googolplex bigger than infinity ?",
               "7- how likely is a supra mk4 twin turbo to gap a dacia logan 2010 ? :)",
               "8- what's x+x ? ",
               "9- 69",
               "is there a 10th question ??"]

list_of_answers = ["yes", "yes", "Wolfeschlegelsteinhausenbergerdo",
                   "enough", "balls", "nope", "very unlikely", "x", "69", "no"]

list_of_false = ["what", "what", "Blaine", "what",
                 "what's ligma", "yes", "very likely", "2x", "70", "yes"]
score = 0

###
# create 1st widow text objects
fr_text = text_lib("Welcome to this marvelous Game !")
fr_text1 = text_lib("This is a special game made for you, i wish u all the luck")
fr_text2 = text_lib("It's a question answer game, so only intelligence involved ;)")
fr_text3 = text_lib("The game ends when u get a score of 10 !")
birthday = text_lib("happy birthday !")
birthday3 = text_lib("hope u had fun !")

begin = font.render("B E G I N", True, (0, 0, 0))
begin_case = begin.get_rect()
begin_case.center = (400, 450)

next = font.render("N e x t", True, (0,0,0))
next_case = next.get_rect()
next_case.center = (400,450)

close = font.render("Close", True, (0,0,0))
close_case = close.get_rect()
close_case.center = (400,350)
x1 = 200
y1 = 500


def update_x1y1():
    global x1, y1
    x1 = random.randint(150, 500)
    y1 = random.randint(100, 400)

    while -30 < y1 - x1 < 30:
        x1 = random.randint(150, 500)
        y1 = random.randint(100, 400)


question_on = False
run = True
end  = False
while run:
    front_bg = list_of_bg[score]

    x, y = pygame.mouse.get_pos()
    pressed1 = pygame.mouse.get_pressed()[0]

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            run = False

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False

    screen.blit(bg_back, (0, 0))
    if question_on == False:
        screen.blit(fr_text.textshow, (10, 10))
        screen.blit(fr_text1.textshow, (10, 60))
        screen.blit(fr_text2.textshow, (10, 90))
        screen.blit(fr_text3.textshow, (10, 150))
        screen.blit(begin, begin_case)

    if pressed1 and begin_case.collidepoint(x, y):
        question_on = True

    if question_on == True:
        if 10 > score >= 0:
            screen.blit(bg_back, (0, 0))
            screen.blit(front_bg, (0, 0))
            score_text = font.render("score : " + str(score), True, (0, 0, 0))
            screen.blit(score_text, (10, 10))
            if score == 2:
                font = pygame.font.SysFont('Helvetica', 15, bold=False, italic=False)
            else:
                font = pygame.font.SysFont('Helvetica', 20, bold=False, italic=False)

            qst = font.render(list_of_qst[score], True, (0, 0, 0))
            screen.blit(qst, (10, 50))

            # first answer button

            answerb1 = font.render(list_of_answers[score], True, (0, 0, 0))
            answerb1_case = answerb1.get_rect()
            answerb1_case.center = (x1, y1)
            # second answer button
            answerb2 = font.render(list_of_false[score], True, (0, 0, 0))
            answerb2_case = answerb2.get_rect()
            answerb2_case.center = (y1, x1)

            screen.blit(answerb2, answerb2_case)
            screen.blit(answerb1, answerb1_case)

            if pressed1 and answerb1_case.collidepoint(x, y):
                for event in events:
                    if event.type == MOUSEBUTTONUP:
                        score += 1
                        easygui.msgbox(f"good job score is now equal to {score}", "NICE !")
                        update_x1y1()
            elif pressed1 and answerb2_case.collidepoint(x, y):
                for event in events:
                    if event.type == MOUSEBUTTONUP:
                        easygui.msgbox("Hah, meh, i expected better :(", "tch...")
        elif score == 10:
            screen.blit(next, next_case)
            screen.blit(front_bg, (0,0))
            if pressed1 and next_case.collidepoint(x, y):
                pygame.mixer.music.stop()
                score += 1
                text = "https://www.youtube.com/watch?v=9F8CHHQrryU"
                pyperclip.copy(text)
                easygui.msgbox("something has been pasted to your paperclip, check on ytb ;) ", " hmmmm ...")
                dia = easygui.ynbox("Have u checked yet ??", "question", ["yes ", "not yet"])
                if dia:
                    end = True
                while not dia:
                    dia = easygui.ynbox("Have u checked yet ??", "question", ["yes ", "not yet"])
        elif score ==11 and end == True:

            screen.blit(bg_back, (0,0))
            screen.blit(birthday.textshow, (30,30))
            screen.blit(birthday3.textshow, (30, 150))
            screen.blit(close, close_case)
            if pressed1 and close_case.collidepoint(x, y):
                run = False
    pygame.display.flip()