from moviepy.editor import *
import pygame
pygame.init()



pygame.display.set_caption('Hello World!')
pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
running = True
clock = pygame.time.Clock()

while running:
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False
            #pygame.quit()
            
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): #or pygame.K_p:
            running = False
            pygame.quit()
            
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_UP):
            #clock.tick(50)#25 FPS
            clip = (VideoFileClip('NeverGonnaGiveYouUp_720p.mp4')
                    .fx( vfx.resize, width=1920))
            clip.preview(fps=25, fullscreen=True)
        elif (event.type == pygame.KEYDOWN) and (event.key == pygame.K_DOWN): #30 FPS
            clip = (VideoFileClip('ststic-mute1.mp4')
                    .fx( vfx.resize, width=1920)
                    .fx( vfx.loop, n=None, duration=200))
            clip.preview(fps=30, fullscreen=True)


#clip.preview()

pygame.quit()
