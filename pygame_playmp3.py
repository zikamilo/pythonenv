import pygame

pygame.mixer.init()
pygame.mixer.music.load("test.mp3")
pygame.mixer.music.play()
pygame.time.wait(3000)
pygame.mixer.music.stop()
pygame.mixer.music.load("test1.mp3")
pygame.mixer.music.play()
pygame.time.wait(3000)
pygame.mixer.music.stop()
pygame.mixer.music.load("test2.mp3")
pygame.mixer.music.play()
pygame.time.wait(3000)
pygame.mixer.music.stop()
pygame.mixer.music.load("test3.mp3")
pygame.mixer.music.play()
pygame.time.wait(3000)
pygame.mixer.music.stop()

