'''
播放音乐
'''
import pygame
import time
path = r'C:\Users\Administrator\Desktop\aria2c下载工具\downloads\经典歌曲\01\012.BEYOND - 情人.mp3'
pygame.mixer.init()
track = pygame.mixer.music.load(path)
pygame.mixer.music.play()
time.sleep(10)
#pygame.mixer.music.pause()
pygame.mixer.music.stop()
