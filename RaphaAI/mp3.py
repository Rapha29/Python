import pygame
pygame.init()  #Para iniciar o pygame
pygame.mixer.music.load('ex021.mp3')    # Para carregar o arquivo
pygame.mixer.music.play()   # Para iniciar o evento

pygame.event.wait()