import pygame, pygame.mixer
import sys, os, random
from pygame.locals import *

pygame.init()

character = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
key = (pygame.K_a,pygame.K_b,pygame.K_c,pygame.K_d,pygame.K_e,pygame.K_f,pygame.K_g,pygame.K_h,pygame.K_i,pygame.K_j,pygame.K_k,pygame.K_l,pygame.K_m,pygame.K_n,pygame.K_o,pygame.K_p,pygame.K_q,pygame.K_r,pygame.K_s,pygame.K_t,pygame.K_u,pygame.K_v,pygame.K_w,pygame.K_x,pygame.K_y,pygame.K_z)

#Screen
screen_width = 400
screen_height = 300
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Speedtest')
time = pygame.time.Clock()

#Value
i = random.randint(0,25)
i2 = random.randint(0,25)
score = 0
isCorrect = True
gameStart = False

#text
font = pygame.font.SysFont("Arial",64)
text = font.render("Score = "+str(score),1,(255,255,255))

#life
life = Rect(370,20,30,100)

#run
while True:
 tscore = font.render(str(score),1,(255,255,255))
 for event in pygame.event.get():
  if event.type == pygame.QUIT:
   pygame.quit()
   sys.exit()
  if pygame.key.get_pressed()[K_SPACE]:
   score = 0
   gameStart = True
   isCorrect = True
  elif pygame.key.get_pressed()[key[i]] or pygame.key.get_pressed()[key[i2]]:
   if pygame.key.get_pressed()[key[i]] and pygame.key.get_pressed()[key[i2]] and gameStart:
    if not isCorrect:
     score += 1
    isCorrect = True
  elif event.type == KEYDOWN:
   text = font.render("Score = "+str(score),1,(255,255,255))
   gameStart = False

 screen.fill((0,0,0))

 if gameStart:
  if isCorrect:
   i = random.randint(0,25)
   i2 = random.randint(0,25)
   while i == i2: i2 = random.randint(0,25)
   text1 = font.render(character[i],1,(random.randint(50,255),random.randint(50,255),random.randint(50,255)))
   text2 = font.render(character[i2],1,(random.randint(50,255),random.randint(50,255),random.randint(50,255)))
   isCorrect = False
   t = pygame.time.get_ticks()
  if pygame.time.get_ticks() - t + score*20 > 2000 :
   text = font.render("Score = "+str(score),1,(255,255,255))
   gameStart = False

 screen.blit(tscore, (10,10))
 if gameStart:
  screen.blit(text1, ((screen_width/4 - text1.get_width()/2), (screen_height/2- text1.get_height()/2)))
  screen.blit(text2, ((screen_width*3/4 - text1.get_width()/2), (screen_height/2- text1.get_height()/2)))
  pygame.draw.rect(screen,(255,255,255),Rect(370,20,30,(2000 - pygame.time.get_ticks() + t - score*20) * 100 / 2000))
 else :
  screen.blit(text, ((screen_width - text.get_width()) // 2, (screen_height- text.get_height()) // 2))
 pygame.display.flip()
 time.tick(60)
