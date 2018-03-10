import pygame as Screen
import tkinter
import CrosswordGen


notdone = True
WordsInput = []
count = 0
while(notdone):
    word = input("input a word - ")
    WordsInput.append(word)
    count += 1
    if(count >= 3):
        another = input("do you want to input another word? Y/n - ")
        if(another == "Y"):
            notdone = True
        else:
            notdone = False

gridsize = input("Please input grid size in one number - ")

root = tkinter.Tk()
Screen.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)




count = 0
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
screen = Screen.display.set_mode((display_width, display_height), Screen.FULLSCREEN)

Screen.display.set_caption('Crossword Generator')

clock = Screen.time.Clock()

BlankImg = Screen.image.load('Blank.png')
WithCharImg = Screen.image.load('WithChar.png')

myfont = Screen.font.SysFont("monospace", 40)
mysecondfont = Screen.font.SysFont("monospace", 30)




Answers = CrosswordGen.CrosswordGen(WordsInput, int(gridsize))

n = 0

labels = [[myfont.render(x, 1, (0,0,0)) for x in Line] for Line in Answers[n]]
OutOfLbl = myfont.render(str(n+1) + "/" + str(len(Answers)), 1, (0,0,0))

def NextGrid(Place):
    global n, Answers, labels, OutOfLbl
    n += Place
    if n < 0:
        n = len(Answers) - 1
    if n > len(Answers) - 1:
        n = 0
    labels = [[myfont.render(x, 1, (0, 0, 0)) for x in Line] for Line in Answers[n]]
    OutOfLbl = myfont.render(str(n + 1) + "/" + str(len(Answers)), 1, (0, 0, 0))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,Input, action=None):
    global mysecondfont
    mouse = Screen.mouse.get_pos()
    click = Screen.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        Screen.draw.rect(screen, ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            action(Input)
    else:
        Screen.draw.rect(screen, ic,(x,y,w,h))

    smallText = Screen.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def CreateGrid(size):
    global Answers
    global n
    Grid = Answers[n]
    Gridx, Gridy = 0, 0
    x = 10
    y = 10
    count = 0
    for i in range(0, size*size):
        screen.blit(WithCharImg, (x, y))
        if Grid[Gridy][Gridx] == None:
            screen.blit(BlankImg, (x, y))
        else:
            screen.blit(labels[Gridy][Gridx], (x+7, y-5))
        x += 50
        Gridx += 1
        count += 1
        if(count == size):
            y += 50
            Gridy += 1
            x = 10
            Gridx = 0
            count = 0


done = False

def Done(Input = None):
    global done
    done = True
while not done:
    for event in Screen.event.get():
        if event.type == Screen.QUIT:
            done = True

    screen.fill(white)

    events = Screen.event.get()
    button("Previous Grid", display_width - 700, 10, 300, 100, red, bright_red, -1, NextGrid)
    button("Next Grid", display_width - 400, 10, 300, 100, green, bright_green, 1, NextGrid)
    button("X", display_width - 50, 10, 50, 50, white, bright_red, 1, Done)

    CreateGrid(10)
    screen.blit(OutOfLbl, (display_width - 440, 125))
    Screen.display.update()
    clock.tick(8)

Screen.quit()
quit()
