import pygame

def playMusic(filename):
    flag = 0
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(loops=3)
#filename = r'E:\程序设计\项目集合\Python\赛尔号\测试1\背景音乐\Music\Sai_1.mp3'
#playMusic(filename)