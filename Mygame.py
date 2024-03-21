import pygame
import random
import math
from pygame import mixer


#Intialize Pygame
pygame.init()

#Create the screen
screen=pygame.display.set_mode((1280,720))

#Title and Icon
pygame.display.set_caption("Galaxy Game")
icon =pygame.image.load("launch.png")
pygame.display.set_icon(icon)
background=pygame.image.load("pexels-frank-cone-3214110.jpg")

#add music
mixer.music.load('background.mp3')
mixer.music.play(-1)

#player
img_player=pygame.image.load("spaceship1.png")
player_x=640
player_y=650
player_x_change=0

#player function
def player(x,y):
    screen.blit(img_player,(player_x,player_y))

#enemy variables
img_enemy=[]
enemy_x=[]
enemy_y=[]
enemy_x_change=[]
enemy_y_change=[]
number_of_enemy=8

for e in range(number_of_enemy):
    img_enemy.append(pygame.image.load("ufo.png"))
    enemy_x.append(random.randint(6,1216))
    enemy_y.append(random.randint(6,250))
    enemy_x_change.append(0.5)
    enemy_y_change.append(60)


#enemy function
def enemy(x,y,en):
    screen.blit(img_enemy[en],(x,y))

#bullet variables
img_bullet=pygame.image.load("bullet.png")
bullet_x=0
bullet_y=650
bullet_x_change=0
bullet_y_change=5
visible_bullet= False

#score variable
score=0
my_font= pygame.font.Font('Dolce Vita Heavy Bold.ttf',32)
text_x=10
text_y=10

#end of game text
end_font= pygame.font.Font('Dolce Vita Heavy Bold.ttf',50)

def final_text():
    my_final_font= end_font.render("GAME OVER BUDDY",True,(255,255,255))
    screen.blit(my_final_font,(450,300))


#functions for displaying Score
def show_score(x,y):
    text = my_font.render(f'Score: {score}',True,(255,255,255))
    screen.blit(text,(x,y))


#bullet function
def shoot_bullet(x,y):
    global visible_bullet
    visible_bullet= True
    screen.blit(img_bullet,(x+16,y+15))

#collision detection
def collision(x1,x2,y1,y2):
    distance=math.sqrt(math.pow(x2-x1,2)+ math.pow(y2-y1,2))
    if distance<=27:
        return True
    else:
        return False



#Gameloop
is_running= True
while is_running:
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            is_running=False
        #KEY press detection
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change =-1.5
            if event.key == pygame.K_RIGHT:
                player_x_change =1.5
            if event.key ==pygame.K_SPACE:
                bullet_sound=mixer.Sound('bullet-[AudioTrimmer.com] (1)-[AudioTrimmer.com].mp3')
                bullet_sound.set_volume(0.4)
                bullet_sound.play()
                if visible_bullet ==False:
                    bullet_x=player_x
                    shoot_bullet(bullet_x,bullet_y)
        #key press release
        if event.type==pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key== pygame.K_RIGHT:
                player_x_change= 0

    #Modify player location
    player_x+= player_x_change

    #keep player inside screen
    if player_x <=6:
        player_x=6
    elif player_x>=1210:
        player_x=1210

    #Modify enemy location
    for enem in range(number_of_enemy):
        #end of game
        if enemy_y[enem]>600:
            for k in range(number_of_enemy):
                enemy_y[k]=1000
            final_text()
            break
        enemy_x[enem]+= enemy_x_change[enem]


    #keep enemy inside screen
        if enemy_x[enem] <=6:
            enemy_x_change[enem]=1.2
            enemy_y[enem]+=enemy_y_change[enem]
        elif enemy_x[enem]>=1210:
            enemy_x_change[enem]=-1.2
            enemy_y[enem] += enemy_y_change[enem]

        # collisions
        collision_stat = collision(enemy_x[enem], bullet_x, enemy_y[enem], bullet_y)

        if collision_stat:
            collision_sound=mixer.Sound('shot.mp3')
            collision_sound.play()
            bullet_y = 650
            visible_bullet = False
            score += 1
            enemy_x[enem] = random.randint(6, 1216)
            enemy_y[enem] = random.randint(6, 250)

        enemy(enemy_x[enem], enemy_y[enem],enem)

    #bullets movement
    if bullet_y<=-32:
        bullet_y=650
        visible_bullet =False
    if visible_bullet:
        shoot_bullet(bullet_x,bullet_y)
        bullet_y-=bullet_y_change


    player(player_x,player_y)
    show_score(text_x,text_y)


    #update
    pygame.display.update()