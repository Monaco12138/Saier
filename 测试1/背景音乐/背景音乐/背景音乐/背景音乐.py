import pygame

def playMusic(filename , loops=0 , start =0.0 , value=0.5):
    flag = 0
    pygame.mixer.init()
    while 1:
        if flag == 0:
             pygame.mixer.music.load(filename)
             pygame.mixer.music.play(loops=loops , start=start)
             pygame.mixer.music.set_volume(value)
        if pygame.mixer.music.get_busy() == 1:
             flag = 1
        else:
             if flag:
                pygame.mixer.music.stop()
                break

filename = r'E:\程序设计\项目集合\Python\赛尔号\测试1\背景音乐\Music\Sai_1.mp3'
#playMusic(filename)