from PIL import Image,ImageTk
import random
from 背景音乐 import*
import tkinter as tk

class Animal:
    def __init__(self , name , fight , fight_add , protect , \
        protect_add , speed , Hp , attact1 , attact2 , attact3 , attact4\
        ,att1_name , att2_name , att3_name , att4_name,\
        att1_eff , att2_eff , att3_eff , att4_eff,\
        one , two , three , four):
        (self.name , self.fight , self.fight_add , self.protect , self.protect_add , self.speed, self.Hp)\
           = (name , fight , fight_add , protect , protect_add , speed , Hp) 
        (self.attact1 , self.attact2 , self.attact3 , self.attact4) = (attact1,attact2,attact3,attact4)
        (self.att1_name , self.att2_name , self.att3_name , self.att4_name) = (att1_name,att2_name , att3_name , att4_name)
        (self.att1_eff,self.att2_eff,self.att3_eff,self.att4_eff) = (att1_eff,att2_eff,att3_eff,att4_eff)
        (self.one , self.two , self.three , self.four) = (one , two , three , four)

Num = -1
List = []
Matrix=[]
fr = open(r'E:\学习\程序设计\项目集合\Python\赛尔号\content.txt')
for line in fr.readlines():
    lineArr = line.strip().split()
    Num += 1
    for i in range(19):
        List.append(lineArr[i])
    Matrix.append(List)
    List = []
while(1):
    (first,second) = (random.randint(0,Num) , random.randint(0,Num))    #随机选取精灵
    if first != second:
        break
#(first , second) = (7,3)
#************************************************8************
Qun = 0     #群影乱舞
Fire_Mo = 0    #烧伤
Jue_Mo = 0     #觉醒
Hui_Ha = 0      #回避
Qian_Ka = 0     #乾坤反转
Hai_Yu = 0     #海之祝愿
Rui_Yu = -1      #瑞流龙击打
You_Bu = 0      #幽幻之盾
#***************************                        通用函数
def Wait_time():            #中场等待时间
    root.after(1000,)
def Prob(num):
    N = random.randint(0,99)
    if 10<= N <= num+9:
        return 1
    else:
        return 0

def Fire_changed1(Hp):      #烧伤函数对左边精灵
    global hp1,Fire_Mo
    if(Fire_Mo > 0):
            N = random.randint(1,5)
            temp = float(N/100) * Hp
            temp = int(temp)
            hp1 = hp1 - temp
            Hp1_changed()
            string = '烧伤'+'扣'+'{}'.format(temp)+'\n'
            txt0.insert(tk.END,string)
            Fire_Mo -= 1

def Fire_changed2(Hp):      #烧伤函数对右边精灵
    global hp2,Fire_Mo
    if(Fire_Mo > 0):
            N = random.randint(1,5)
            temp = float(N/100) * Hp
            temp = int(temp)
            hp2 = hp2 - temp
            Hp2_changed()
            string = '烧伤'+'扣'+'{}'.format(temp)+'\n'
            txt0.insert(tk.END,string)
            Fire_Mo -= 1   
def Qun_get1(att_name , Shanghai):      #群影乱舞影响左边精灵扣右边精灵的血
    global Qun , hp2 , txt0
    if(Qun == 0):
            hp2= hp2 - Shanghai
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
    elif Qun>0:
            Shanghai = Shanghai*0.7
            hp2 = hp2 - int(Shanghai)
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'+'群影乱舞减少了'+'{}伤害'.format(int(Shanghai*0.3))+'\n'
            #Qun -= 1
    txt0.insert(tk.END,string)
    Hp2_changed()

def Qun_get2(att_name , Shanghai):          #群影乱舞影响右边精灵扣左边精灵的血
    global Qun , hp1 , txt0
    if(Qun == 0):
            hp1 = hp1 - Shanghai
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
    elif Qun>0:
            Shanghai = Shanghai*0.7
            hp1 = hp1 - int(Shanghai)
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'+'群影乱舞减少了'+'{}伤害'.format(int(Shanghai*0.3))+'\n'
           # Qun -= 1
    txt0.insert(tk.END,string)
    Hp1_changed()

def Hui_Haget1(att_name , Shanghai):       #回避影响左边精灵扣右边精灵的血
    global Hui_Ha , hp2 , txt0
    if(Hui_Ha > 0  and Prob(50)):
            Shanghai = Shanghai*0.4
            hp2 = hp2 - int(Shanghai)
            string = '回避命中\n'+att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
            #Hui_Ha -= 1
    else:
            hp2= hp2 - Shanghai
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
    txt0.insert(tk.END,string)
    Hp2_changed()
def Hui_Haget2(att_name , Shanghai):        #回避影响右边精灵打左边精灵打右边精灵
    global Hui_Ha , hp1 , txt0
    if(Hui_Ha > 0  and Prob(50)):
            Shanghai = Shanghai*0.4
            hp1 = hp1 - int(Shanghai)
            string = '回避命中\n'+att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
            #Hui_Ha -= 1
    else:
            hp1= hp1 - Shanghai
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
    txt0.insert(tk.END,string)
    Hp1_changed()
def Qian_Kaget1(att_name , Shanghai):       #乾坤反转影像左边精灵扣血
    global Qian_Ka, hp1,hp2,txt0
    hp2 = hp2 -Shanghai
    if(Qian_Ka > 0 and Prob(50)):
        N = random.randint(50,75)
        temp = int( float(N/100) * Shanghai)
        hp1 = hp1 - temp
        string = '乾坤反转命中扣'+'{}'.format(temp)+'\n'
        txt0.insert(tk.END,string)
        Hp1_changed()
    string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
    txt0.insert(tk.END,string)
    Hp2_changed()

def Qian_Kaget2(att_name , Shanghai):       #乾坤反转影像右边精灵扣血
    global Qian_Ka, hp1,hp2,txt0
    hp1 = hp1 -Shanghai
    if(Qian_Ka > 0 and Prob(50)):
        N = random.randint(50,75)
        temp = int( float(N/100) * Shanghai)
        hp2 = hp2 - temp
        string = '乾坤反转命中扣'+'{}'.format(temp)+'\n'
        txt0.insert(tk.END,string)
        Hp2_changed()
    string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
    txt0.insert(tk.END,string)
    Hp1_changed()
def You_Buget1(att_name , Shanghai):           #幽幻之盾影响左边精灵打右边
    global You_Bu , hp2 , txt0
    if(You_Bu > 0):
            Shanghai = Shanghai*0.4
            hp2 = hp2 - int(Shanghai)
            string = '幽幻之盾命中\n'+att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END,string)
    else:
            hp2= hp2 - Shanghai
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END,string)
            #Hp2_changed()
    Hp2_changed()

def You_Buget2(att_name  ,Shanghai):             #幽幻之盾影响右边精灵打左边
    global You_Bu , hp1 , txt0
    if(You_Bu > 0):
          Shanghai = Shanghai*0.4
          hp1 = hp1- int(Shanghai)
          string = '幽幻之盾命中\n'+att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
          txt0.insert(tk.END,string)
    else:
            hp1= hp1 - Shanghai
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END,string)
            #Hp2_changed()
    Hp1_changed()
def Jing_shang1(att_name , Shanghai):       #封装后总技能对左边精灵影响
    global Jing2,hp2
    if Jing2.name == '盖亚':
            Qun_get1(att_name,Shanghai)
    elif Jing2.name == '哈莫雷特':
            Hui_Haget1(att_name,Shanghai)
    elif Jing2.name == '卡修斯':
            Qian_Kaget1(att_name,Shanghai)
    elif Jing2.name == '布莱克':
            You_Buget1(att_name , Shanghai)
    else:
            hp2= hp2 - Shanghai
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END,string)
            Hp2_changed()
def Jing_shang2(att_name , Shanghai):       #封装后总技能对右边精灵的影响
    global Jing1,hp1
    if Jing1.name == '盖亚':
            Qun_get2(att_name,Shanghai)
    elif Jing1.name == '哈莫雷特':
            Hui_Haget2(att_name,Shanghai)
    elif Jing1.name == '卡修斯':
            Qian_Kaget2(att_name,Shanghai)
    elif Jing1.name == '布莱克':
            You_Buget2(att_name , Shanghai)
    else:
            hp1= hp1 - Shanghai
            string = att_name+'打出'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END,string)
            Hp1_changed()
def First():
    global attacka_1
    global attacka_2
    global attacka_3
    global attacka_4
    global mp2
    Wait_time()
    attacka_1.place_forget()
    attacka_2.place_forget()
    attacka_3.place_forget()
    attacka_4.place_forget()
    mp2 += 3
    Mp2_changed()
    Attackb()           #展示B精灵可用的招数
    #print('First-Gai')

def Attackb():              #B精灵的技能显示
    global attackb_1
    global attackb_2
    global attackb_3
    global attackb_4
    global mp2
    global txt1
    global txt2
    global txt3
    global txt4
    txt1.configure(text = Jing2.att1_eff)
    txt2.configure(text=Jing2.att2_eff)
    txt3.configure(text = Jing2.att3_eff)
    txt4.configure(text = Jing2.att4_eff)
    if mp2 >= Jing2.one:
        attackb_1 = tk.Button(root , text=Jing2.att1_name , command=Jing2.attact1 ,relief='groove',bg='gray',fg='blue')
        attackb_1.place(relx=0.3 , rely=0.8 , width=100,height=50)

        attackb_2 = tk.Button(root , text=Jing2.att2_name , command=Jing2.attact2 , relief='groove',bg='gray',fg='blue')
        attackb_2.place(relx=0.4 , rely=0.8 , width=100,height=50)

        attackb_3 = tk.Button(root , text=Jing2.att3_name , command=Jing2.attact3 , relief='groove',bg='gray',fg='blue')
        attackb_3.place(relx=0.5 , rely=0.8 , width=100,height=50)

        attackb_4 = tk.Button(root , text=Jing2.att4_name , command=Jing2.attact4 , relief='groove',bg='gray',fg='blue')
        attackb_4.place(relx=0.6 , rely=0.8 , width=100,height=50)
    elif  Jing2.two<= mp2 < Jing2.one:
        attackb_1 = tk.Label(root , text=Jing2.att1_name , relief='groove',bg='black',fg='blue')
        attackb_1.place(relx=0.3 , rely=0.8 , width=100,height=50)

        attackb_2 = tk.Button(root , text=Jing2.att2_name , command=Jing2.attact2 , relief='groove',bg='gray',fg='blue')
        attackb_2.place(relx=0.4 , rely=0.8 , width=100,height=50)

        attackb_3 = tk.Button(root , text=Jing2.att3_name , command=Jing2.attact3 , relief='groove',bg='gray',fg='blue')
        attackb_3.place(relx=0.5 , rely=0.8 , width=100,height=50)

        attackb_4 = tk.Button(root , text=Jing2.att4_name , command=Jing2.attact4 , relief='groove',bg='gray',fg='blue')
        attackb_4.place(relx=0.6 , rely=0.8 , width=100,height=50)
    elif  Jing2.three<= mp2 < Jing2.two:
        attackb_1 = tk.Label(root , text=Jing2.att1_name , relief='groove',bg='black',fg='blue')
        attackb_1.place(relx=0.3 , rely=0.8 , width=100,height=50)

        attackb_2 = tk.Label(root , text=Jing2.att2_name , relief='groove',bg='black',fg='blue')
        attackb_2.place(relx=0.4 , rely=0.8 , width=100,height=50)

        attackb_3 = tk.Button(root , text=Jing2.att3_name , command=Jing2.attact3 , relief='groove',bg='gray',fg='blue')
        attackb_3.place(relx=0.5 , rely=0.8 , width=100,height=50)

        attackb_4 = tk.Button(root , text=Jing2.att4_name , command=Jing2.attact4 , relief='groove',bg='gray',fg='blue')
        attackb_4.place(relx=0.6 , rely=0.8 , width=100,height=50)
    elif Jing2.four<= mp2 < Jing2.three:
        attackb_1 = tk.Label(root , text=Jing2.att1_name , relief='groove',bg='black',fg='blue')
        attackb_1.place(relx=0.3 , rely=0.8 , width=100,height=50)

        attackb_2 = tk.Label(root , text=Jing2.att2_name , relief='groove',bg='black',fg='blue')
        attackb_2.place(relx=0.4 , rely=0.8 , width=100,height=50)

        attackb_3 = tk.Label(root , text=Jing2.att3_name , relief='groove',bg='black',fg='blue')
        attackb_3.place(relx=0.5 , rely=0.8 , width=100,height=50)

        attackb_4 = tk.Button(root , text=Jing2.att4_name , command=Jing2.attact4 , relief='groove',bg='gray',fg='blue')
        attackb_4.place(relx=0.6 , rely=0.8 , width=100,height=50)


def Mp1_changed():
    global Mp1
    Mp1.place_forget()
    Mp1 = tk.Label(root ,text='MP:{}'.format(mp1) ,fg='blue',font=('Arial',16))
    Mp1.place(relx=0.2,rely=0.1,width=80,relheight=0.1)

def Hp1_changed():
    global Hp1
    global Hp_show1
    Hp1.configure(text='Hp:{}'.format(int(hp1)))
    Hp_show1.place_forget()
    Hp_show1 = tk.Label(root ,bg='red',font=('Arial',1))#左边精灵的血条
    Hp_show1.place(relx=0.1 , rely=0.2 , width=hp1 , relheight=0.03)

def Hp2_changed():
    global Hp2
    global Hp_show2
    Hp2.configure(text='Hp:{}'.format(int(hp2)))
    Hp_show2.place_forget()
    Hp_show2 = tk.Label(root ,bg='red',font=('Arial',1))#左边精灵的血条
    Hp_show2.place(relx=0.7 , rely=0.2 , width=hp2 , relheight=0.03)

def Change_HP(fight1 , protect2 , power):
    temp =int( fight1 - float(protect2/2) )
    jishu = random.randint(5,temp)
    rate = 1 + float(power/100)
    hp_temp = int(jishu * rate)
    return hp_temp

def Second():
    global attacka_1
    global attacka_2
    global attacka_3
    global attacka_4
    global attackb_1
    global attackb_2
    global attackb_3
    global attackb_4
    global mp1
    Wait_time()
    attackb_1.place_forget()
    attackb_2.place_forget()
    attackb_3.place_forget()
    attackb_4.place_forget()
    mp1 += 3
    Mp1_changed()
    Attacka()

def Attacka():              #展示A精灵可用的招数
    global mp1
    global attacka_1
    global attacka_2
    global attacka_3
    global attacka_4
    global txt1
    global txt2
    global txt3
    global txt4
    txt1.configure(text = Jing1.att1_eff)
    txt2.configure(text=Jing1.att2_eff)
    txt3.configure(text = Jing1.att3_eff)
    txt4.configure(text = Jing1.att4_eff)
    
    if mp1 >= Jing1.one:
        attacka_1 = tk.Button(root , text=Jing1.att1_name , command=Jing1.attact1 ,relief='groove',bg='gray',fg='red')
        attacka_1.place(relx=0.3 , rely=0.8 , width=100,height=50)

        attacka_2 = tk.Button(root , text=Jing1.att2_name , command=Jing1.attact2 , relief='groove',bg='gray',fg='red')
        attacka_2.place(relx=0.4 , rely=0.8 , width=100,height=50)

        attacka_3 = tk.Button(root , text=Jing1.att3_name , command=Jing1.attact3 , relief='groove',bg='gray',fg='red')
        attacka_3.place(relx=0.5 , rely=0.8 , width=100,height=50)

        attacka_4 = tk.Button(root , text=Jing1.att4_name , command=Jing1.attact4 , relief='groove',bg='gray',fg='red')
        attacka_4.place(relx=0.6 , rely=0.8 , width=100,height=50)
    elif  Jing1.two<= mp1 < Jing1.one:
        attacka_1 = tk.Label(root , text=Jing1.att1_name , relief='groove',bg='black',fg='red')
        attacka_1.place(relx=0.3 , rely=0.8 , width=100,height=50)

        attacka_2 = tk.Button(root , text=Jing1.att2_name , command=Jing1.attact2 , relief='groove',bg='gray',fg='red')
        attacka_2.place(relx=0.4 , rely=0.8 , width=100,height=50)

        attacka_3 = tk.Button(root , text=Jing1.att3_name , command=Jing1.attact3 , relief='groove',bg='gray',fg='red')
        attacka_3.place(relx=0.5 , rely=0.8 , width=100,height=50)

        attacka_4 = tk.Button(root , text=Jing1.att4_name , command=Jing1.attact4 , relief='groove',bg='gray',fg='red')
        attacka_4.place(relx=0.6 , rely=0.8 , width=100,height=50)
    elif  Jing1.three<= mp1 < Jing1.two:
        attacka_1 = tk.Label(root , text=Jing1.att1_name , relief='groove',bg='black',fg='red')
        attacka_1.place(relx=0.3 , rely=0.8 , width=100,height=50)

        attacka_2 = tk.Label(root , text=Jing1.att2_name , relief='groove',bg='black',fg='red')
        attacka_2.place(relx=0.4 , rely=0.8 , width=100,height=50)

        attacka_3 = tk.Button(root , text=Jing1.att3_name , command=Jing1.attact3 , relief='groove',bg='gray',fg='red')
        attacka_3.place(relx=0.5 , rely=0.8 , width=100,height=50)

        attacka_4 = tk.Button(root , text=Jing1.att4_name , command=Jing1.attact4 , relief='groove',bg='gray',fg='red')
        attacka_4.place(relx=0.6 , rely=0.8 , width=100,height=50)
    elif Jing1.four<= mp2 < Jing1.three:
        attacka_1 = tk.Label(root , text=Jing1.att1_name , relief='groove',bg='black',fg='red')
        attacka_1.place(relx=0.3 , rely=0.8 , width=100,height=50)

        attacka_2 = tk.Label(root , text=Jing1.att2_name , relief='groove',bg='black',fg='red')
        attacka_2.place(relx=0.4 , rely=0.8 , width=100,height=50)

        attacka_3 = tk.Label(root , text=Jing1.att3_name , relief='groove',bg='black',fg='red')
        attacka_3.place(relx=0.5 , rely=0.8 , width=100,height=50)

        attacka_4 = tk.Button(root , text=Jing1.att4_name , command=Jing1.attact4 , relief='groove',bg='gray',fg='red')
        attacka_4.place(relx=0.6 , rely=0.8 , width=100,height=50)


def Mp2_changed():
    global Mp2  
    Mp2.place_forget()
    Mp2 = tk.Label(root ,text='MP:{}'.format(mp2) ,fg='blue',font=('Arial',16))
    Mp2.place(relx=0.8,rely=0.1,width=80,relheight=0.1)
#*********************************************************************#精灵技能
def Gaiya_1():        #盖亚-石破天惊
    #print('***')
    #playMusic(filename)
    global txt0,Jing2,mp2,show_protect1,show_protect2
    global mp1,Jing1,hp1,hp2,Fire_Mo,Qun,show_fight1,show_fight2
    #********************************
    if Jing1.name == '盖亚':
        mp1 -= 5
        Mp1_changed()
        shanghai = Change_HP(Jing1.fight+Jing1.fight_add , Jing2.protect+Jing2.protect_add, 180)

        Jing_shang1('石破天惊',shanghai)
        Jing2.protect_add = 0#技能效果
        Jing2.fight_add = 0
        show_fight2.configure(text='攻:{}'.format(Jing2.fight +Jing2.fight_add))
        show_protect2.configure(text='防:{}'.format(Jing2.protect+Jing2.protect_add))
        Fire_changed1(Jing1.Hp)             #烧伤判断
        if Qun>0:
            Qun -= 1
        First()
    else:
        mp2 -= 5
        Mp2_changed()
        shanghai = Change_HP(Jing2.fight+Jing2.fight_add , Jing1.protect+Jing1.protect_add, 180)

        Jing_shang2('石破天惊',shanghai)
        Jing1.protect_add = 0#技能效果
        Jing1.fight_add = 0
        show_fight1.configure(text='攻:{}'.format(Jing1.fight +Jing1.fight_add))
        show_protect1.configure(text='防:{}'.format(Jing1.protect+Jing1.protect_add))
        Fire_changed2(Jing2.Hp)
        if Qun > 0:
            Qun -= 1
        Second()
    #********************************
    #********************************       

def Gaiya_2():            #盖亚-破釜沉舟
    global mp1,txt0,hp1,mp2,Qun
    global hp2,Jing1,Jing2,Fire_Mo
    #*********************************************
    if Jing1.name == '盖亚':
        mp1 -= 3
        Mp1_changed()
        shanghai = Change_HP(Jing1.fight+Jing1.fight_add , Jing2.protect+Jing2.protect_add , 120)

        Jing_shang1('破釜沉舟',shanghai)

        Fire_changed1(Jing1.Hp)
        if Qun > 0:
            Qun -= 1
        if(Prob(15)):
            Wait_time()
            mp1 += 3
            Mp1_changed()
            string='恐惧效果命中'+'\n'
            txt0.insert(tk.END,string)
        else:
            string='恐惧效果未命中'+'\n'
            txt0.insert(tk.END,string)
            First()
    else:
        mp2 -= 3
        Mp2_changed()
        shanghai = Change_HP(Jing2.fight+Jing2.fight_add , Jing1.protect+Jing1.protect_add , 120)
        
        Jing_shang2('破釜沉舟',shanghai)

        if Qun > 0:
            Qun -= 1
        Fire_changed2(Jing2.Hp)
        if(Prob(15)):
            Wait_time()
            mp2 += 3
            Mp1_changed()
            string='恐惧效果命中'+'\n'
            txt0.insert(tk.END,string)
        else:
            string='恐惧效果未命中'+'\n'
            txt0.insert(tk.END,string)
            Second()
    #**************************************
    
    #**********************************************

def Gaiya_4():             #盖亚-元气觉醒
    global mp1,mp2,Qun
    global Jing1,Jing2,Fire_Mo
    global show_fight1,show_fight2
    #******************************
    if Jing1.name == '盖亚':
        mp1 -= 1
        Mp1_changed()
        Jing1.fight_add += 5
        show_fight1.configure(text ='攻:{}'.format(Jing1.fight+Jing1.fight_add) )
        Fire_changed1(Jing1.Hp)
        if Qun > 0:
            Qun -= 1
        First()
    else:
        mp2 -= 1
        Mp2_changed()
        Jing2.fight_add += 5
        show_fight2.configure(text ='攻:{}'.format(Jing2.fight+Jing2.fight_add) )
        Fire_changed2(Jing2.Hp)
        if Qun > 0:
            Qun -= 1
        Second()
    #*****************************

def Gaiya_3():              #盖亚-群影乱舞
    global mp1,Qun,mp2,Fire_Mo
    if Jing1.name == '盖亚':
        mp1 -= 2
        Mp1_changed()
        Qun += 3
        Fire_changed1(Jing1.Hp)
        if Qun > 0:
            Qun -= 1
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        Qun += 3
        if Qun > 0:
            Qun -= 1
        Fire_changed2(Jing2.Hp)
        Second()

def Li_2():                 #丽莎布布-光合作用
    global mp2,txt0
    global mp1,hp1,hp2,Jing1,Jing2
    if Jing2.name == '丽莎布布':
        mp2 -= 4
        Mp2_changed()
        temp = 23*random.randint(1,5)
        hp2 += temp
        if hp2  >= 400:
            hp2 = 400
        string = '光合作用'+'血恢复'+'{}'.format(temp)+'\n'
        txt0.insert(tk.END,string)
        Hp2_changed()
        Fire_changed2(Jing2.Hp)
        Second()
    #***************************
    else:
        mp1 -= 4
        Mp1_changed()
        temp = 25*random.randint(1,5)
        hp1 += temp
        if hp1  >= 400:
            hp1 = 400
        string = '光合作用'+'血恢复'+'{}'.format(temp)+'\n'
        txt0.insert(tk.END,string)
        Hp1_changed()
        Fire_changed1(Jing1.Hp)
        First()
    #****************************
def Li_3():                    #丽莎布布-叶绿光速
    global mp2,txt0,mp1,hp2
    global hp1,show_fight1,Jing1,Jing2,show_fight2
    if Jing2.name == '丽莎布布':
        mp2 -= 2
        Mp2_changed()
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect+Jing1.protect_add , 90)

        Jing_shang2('叶绿光速',Shanghai)

        Fire_changed2(Jing2.Hp)
        #****************************************
        Jing1.fight_add = 0
        show_fight1.configure(text='攻:{}'.format(Jing1.fight))
        #*************************
        Second()
    else:
        mp1 -= 2
        Mp1_changed()
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect+Jing2.protect_add , 90)

        Jing_shang1('叶绿光速',Shanghai)

        Fire_changed1(Jing1.Hp)
        #****************************************
        Jing2.fight_add = 0
        show_fight2.configure(text='攻:{}'.format(Jing2.fight))
        #*************************
        First()
def Li_1():                 #丽莎布布-金光绿叶
    global mp2,Qun,txt0
    global hp1,hp2,mp1,Jing1,Jing2
    if Jing2.name == '丽莎布布':
        mp2 -= 5
        Mp2_changed()
        #********************************
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect + Jing1.protect_add , 150)

        Jing_shang2('金光绿叶',Shanghai)

        Fire_changed2(Jing2.Hp)
        #**********************************
        if Prob(40):
            hp2 = hp2+Shanghai
            if hp2 >= 400:
                hp2 = 400
            string = '金光绿叶'+'恢复了'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END , string)
        Hp2_changed()
        #**********************************
        Second()
    else:
        mp1 -= 5
        Mp1_changed()
        #********************************
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect + Jing2.protect_add , 150)
        
        Jing_shang1('金光绿叶',Shanghai)

        Fire_changed1(Jing1.Hp)
        #**********************************
        if Prob(40):
            hp1 += Shanghai
            if hp1 >= 400:
                hp1 = 400
            string = '金光绿叶'+'恢复了'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END , string)
        Hp1_changed()
        #**********************************
        First()

def Li_4():                 #丽莎布布-叶绿护甲
    global mp2,mp1,Jing1,Jing2
    global show_protect1,show_protect2
    if Jing2.name == '丽莎布布':
        mp2 -= 1
        Mp2_changed()
        #**************************8
        Jing2.protect_add += 5
        show_protect2.configure(text='防:{}'.format(Jing2.protect + Jing2.protect_add))
        Fire_changed2(Jing2.Hp)
        #***************************
        Second()
    else:
        mp1 -= 1
        Mp1_changed()
        #**************************8
        Jing1.protect_add += 5
        show_protect1.configure(text='防:{}'.format(Jing1.protect + Jing1.protect_add))
        #***************************
        Fire_changed1(Jing1.Hp)
        First()

def Mo_1():                     #魔焰烈空击
    global mp1,mp2,hp1,hp2,Jing1,Jing2,txt0,Qun,Fire_Mo,Jue_Mo
    if Jing1.name == '魔焰猩猩':
        mp1 -= 5
        Mp1_changed()
        #********************************
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect + Jing2.protect_add , 150)
        if (Jue_Mo>0 and Prob(60)):
            Shanghai = Shanghai * 2
            Jue_Mo -= 1
            string = '觉醒命中'+'\n'
            txt0.insert(tk.END,string)
        #**********************************************
        Jing_shang1('魔焰烈空击',Shanghai)
        #***********************************************************
        if (Prob(30)):
            Fire_Mo += 3
            string = '对手处于烧伤状态'+'\n'
            txt0.insert(tk.END,string)
        First()
    else:
        mp2 -= 5
        Mp2_changed()
        #********************************
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect + Jing1.protect_add , 150)
        if (Jue_Mo>0 and Prob(60)):
            Shanghai = Shanghai * 2
            Jue_Mo -= 1
            string = '觉醒命中'+'\n'
            txt0.insert(tk.END,string)
        #****************************************
        Jing_shang2('魔焰烈空击',Shanghai)
        #*****************************************************
        if(Prob(30)):
            Fire_Mo += 3
            string = '对手处于烧伤状态'+'\n'
            txt0.insert(tk.END,string)
        Second()
def Mo_2():             #绝命火焰
    global hp1,hp2,mp1,mp2,Jing1,Jing2,txt0,Qun,Jue_Mo
    if Jing1.name == '魔焰猩猩':
        mp1 -= 3
        Mp1_changed()
        #********************************
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect + Jing2.protect_add , 100)
        if (Jue_Mo>0 and Prob(60)):
            Shanghai = Shanghai * 2
            Jue_Mo -= 1
            string = '觉醒命中'+'\n'
            txt0.insert(tk.END,string)
        if(Prob(8)):
            hp2 = 0
            string = '绝命火焰秒杀对方'+'\n'
            txt0.insert(tk.END,string)
            Hp2_changed()
        else:
            Jing_shang1('绝命火焰',Shanghai)
        First()
    else:
        mp2 -= 3
        Mp2_changed()
        #********************************
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect + Jing1.protect_add , 100)
        if (Jue_Mo>0 and Prob(60)):
            Shanghai = Shanghai * 2
            Jue_Mo -= 1
            string = '觉醒命中'+'\n'
            txt0.insert(tk.END,string)
        if(Prob(8)):
            hp1 = 0
            string = '绝命火焰秒杀对方'+'\n'
            txt0.insert(tk.END,string)
            Hp1_changed()
        else:
           Jing_shang2('绝命火焰',Shanghai)
        Second()
def Mo_3():         #觉醒
    global mp1,mp2,Jing1,Jing2,Jue_Mo
    if Jing1.name == '魔焰猩猩':
        mp1 -= 2
        Mp1_changed()
        Jue_Mo += 2
        if Jue_Mo > 0:
            Jue_Mo -= 1
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        Jue_Mo += 2
        if Jue_Mo > 0:
            Jue_Mo -= 1
        Second()

def Mo_4():         #火焰漩涡
    global mp1,mp2,Fire_Mo,Jing1,Jing2,Jue_Mo
    if Jing1.name == '魔焰猩猩':
        mp1 -= 2
        Mp1_changed()
        Fire_Mo += 3
        if Jue_Mo > 0:
            Jue_Mo -= 1
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        Fire_Mo += 3
        if Jue_Mo > 0:
            Jue_Mo -= 1
        Second()

def Ha_1():         #龙王灭碎阵
    global mp1,mp2,Jing1,Jing2,txt0,Hui_Ha,hp2,hp1
    if Jing1.name == '哈莫雷特':
        mp1 -= 5
        Mp1_changed()
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect + Jing2.protect_add , 160)

        Jing_shang1('龙王灭碎阵',Shanghai)

        Fire_changed1(Jing1.Hp)
        if Hui_Ha > 0:
            Hui_Ha -= 1
        if(Prob(30)):
            Wait_time()
            mp1 += 3
            Mp1_changed()
            Attacka()
            string='恐惧效果命中'+'\n'
            txt0.insert(tk.END,string)
        else:
            string='恐惧效果未命中'+'\n'
            txt0.insert(tk.END,string)
            First()
    else:
        mp2 -= 5
        Mp2_changed()
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect + Jing1.protect_add , 160)
        
        Jing_shang2('龙王灭碎阵',Shanghai)

        Fire_changed2(Jing2.Hp)
        if Hui_Ha > 0:
            Hui_Ha -= 1
        if(Prob(30)):
            Wait_time()
            mp2 += 3
            Mp2_changed()
            Attackb()
            string='恐惧效果命中'+'\n'
            txt0.insert(tk.END,string)
        else:
            string='恐惧效果未命中'+'\n'
            txt0.insert(tk.END,string)
            Second()

def Ha_2():             #龙爪闪空破
    global mp1,mp2,Jing1,Jing2,txt0,hp1,hp2,Hui_Ha
    if Jing1.name == '哈莫雷特':
        mp1 -= 3
        Mp1_changed()
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect + Jing2.protect_add , 120)
        
        Jing_shang1('龙爪闪空破',Shanghai)

        Fire_changed1(Jing1.Hp)
        if Hui_Ha > 0:
            Hui_Ha -= 1
        if(Prob(30)):
            string = '额外附加25点伤害'+'\n'
            hp2 -= 25
            txt0.insert(tk.END,string)
            Hp2_changed()
        First()
    else:
        mp2 -= 3
        Mp2_changed()
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect + Jing1.protect_add , 120)
        
        Jing_shang2('龙爪闪空破',Shanghai)

        Fire_changed2(Jing2.Hp)
        if Hui_Ha > 0:
            Hui_Ha -= 1
        if(Prob(30)):
            string = '额外附加25点伤害'+'\n'
            hp1 -= 25
            txt0.insert(tk.END,string)
            Hp1_changed()
        Second()

def Ha_3():         #回避
    global mp1,mp2,Hui_Ha
    if Jing1.name == '哈莫雷特':
        mp1 -= 2
        Mp1_changed()
        Hui_Ha += 3
        Fire_changed1(Jing1.Hp)
        if Hui_Ha > 0:
            Hui_Ha -= 1
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        Hui_Ha += 3
        Fire_changed2(Jing2.Hp)
        if Hui_Ha > 0:
            Hui_Ha -= 1
        Second()
def Ha_4():             #龙之意志
    global mp2,mp1,Jing1,Jing2,show_fight1,show_fight2
    global show_protect1,show_protect2,Hui_Ha
    if Jing1.name == '哈莫雷特':
        mp1 -= 2
        Mp1_changed()
        #**************************8
        Jing1.protect_add += 5
        Jing1.fight_add   += 5
        show_protect1.configure(text='防:{}'.format(Jing1.protect + Jing1.protect_add))
        show_fight1.configure(text='攻:{}'.format(Jing1.fight+Jing1.fight_add) )
        if Hui_Ha > 0:
            Hui_Ha -= 1
        Fire_changed1(Jing1.Hp)
        #***************************
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        #**************************8
        Jing2.protect_add += 5
        Jing2.fight_add   += 5
        show_protect2.configure(text='防:{}'.format(Jing2.protect + Jing2.protect_add))
        show_fight2.configure(text='攻:{}'.format(Jing2.fight+Jing2.fight_add) )
        if Hui_Ha > 0:
            Hui_Ha -= 1
        Fire_changed2(Jing2.Hp)
        Second()
def Lei_1():         #雷神天明闪
    global mp1,mp2,hp1,hp2,Jing1,Jing2,txt0
    if Jing1.name == '雷伊':
        mp1 -= 6
        Mp1_changed()
        #********************************
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect + Jing2.protect_add , 160)
        if ( Prob(30)):
            Shanghai = Shanghai * 3.5
            string = '雷神天明闪伤害*3.5'+'打出'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END,string)
        #**********************************************
        Jing_shang1('雷神天明闪',Shanghai)

        Fire_changed1(Jing1.Hp)
        First()
    else:
        mp2 -= 6
        Mp2_changed()
        #********************************
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect + Jing1.protect_add , 160)
        if ( Prob(30)):
            Shanghai = Shanghai * 3.5
            string = '雷神天明闪伤害*3.5'+'打出'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END,string)
        #**********************************************
        Jing_shang2('雷神天明闪',Shanghai)

        Fire_changed2(Jing2.Hp)
        Second()
def Lei_2():        #瞬雷天闪
    global mp1,mp2,hp1,hp2,Jing1,Jing2,txt0
    if Jing1.name == '雷伊':
        mp1 -= 3
        Mp1_changed()
        #********************************
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect ,120)
        if Jing2.name == '卡修斯':
            Qian_Kaget1('瞬雷天闪',Shanghai)
        else:
            hp2= hp2 - Shanghai
            string = '瞬雷天闪'+'打出'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END,string)
            Hp2_changed()
        Fire_changed1(Jing1.Hp)
        First()
    else:
        mp2 -= 3
        Mp2_changed()
        #********************************
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect ,120)
        if Jing1.name == '卡修斯':
            Qian_Kaget2('瞬雷天闪',Shanghai)
        else:
            hp1= hp1 - Shanghai
            string = '瞬雷天闪'+'打出'+'{}'.format(int(Shanghai))+'\n'
            txt0.insert(tk.END,string)
            Hp1_changed()
        Fire_changed2(Jing2.Hp)
        Second()

def Lei_3():        #电闪雷鸣
    global hp2,Jing1,Jing2,hp1,mp1,mp2,txt0
    #*********************************************
    if Jing1.name == '雷伊':
        mp1 -= 2
        Mp1_changed()
     #   First()
     #   Second()
     #   mp1 -=3
     #   Mp1_changed()
        Fire_changed1(Jing1.Hp)
        if(Prob(50)):
            Wait_time()
            mp1 += 3
            Mp1_changed()
            Attacka()
            string='麻痹效果命中'+'\n'
            txt0.insert(tk.END,string)
        else:
            string='麻痹效果未命中'+'\n'
            txt0.insert(tk.END,string)
            N = random.randint(10,25)
            hp2 = hp2 -N
            Hp2_changed()
            string = '电闪雷鸣扣除'+'{}血'.format(N)+'\n'
            txt0.insert(tk.END,string)
            First()
    else:
        mp2 -= 2
        Mp2_changed()
    #    Second()
    #    First()
    #    mp2 -=3
    #    Mp2_changed()
        Fire_changed2(Jing2.Hp)
        if(Prob(50)):
            Wait_time()
            mp2 += 3
            Mp2_changed()
            Attackb()
            string='麻痹效果命中'+'\n'
            txt0.insert(tk.END,string)
        else:
            string='麻痹效果未命中'+'\n'
            txt0.insert(tk.END,string)
            N = random.randint(10,25)
            hp1 = hp1 -N
            Hp1_changed()
            string = '电闪雷鸣扣除'+'{}血'.format(N)+'\n'
            txt0.insert(tk.END,string)
            Second()

def Lei_4():        #雷神觉醒
    global mp1,mp2
    global Jing1,Jing2
    global show_fight1,show_fight2
    #******************************
    if Jing1.name == '雷伊':
        mp1 -= 2
        Mp1_changed()
        Jing1.fight_add += 10
        show_fight1.configure(text ='攻:{}'.format(Jing1.fight+Jing1.fight_add) )
        Fire_changed1(Jing1.Hp)
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        Jing2.fight_add += 10
        show_fight2.configure(text ='攻:{}'.format(Jing2.fight+Jing2.fight_add) )
        Fire_changed2(Jing2.Hp)
        Second()

def Ka_1():         #量子绝灭波
    global mp1,mp2,hp1,hp2,Jing1,Jing2,txt0,Qian_Ka
    if Jing1.name == '卡修斯':
        mp1 -= 5
        Mp1_changed()
        #********************************
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect_add+Jing2.protect ,150)
        if(Shanghai < 40):
            Shanghai = 40
        Jing_shang1('量子绝灭波',Shanghai)
        Fire_changed1(Jing1.Hp)
        if Qian_Ka > 0:
            Qian_Ka -= 1
        First()
    else:
        mp2 -= 5
        Mp2_changed()
        #********************************
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect+Jing1.protect_add ,150)
        if(Shanghai < 40):
            Shanghai = 40

        Jing_shang2('量子绝灭波',Shanghai)

        Fire_changed2(Jing2.Hp)
        if Qian_Ka > 0:
            Qian_Ka -= 1
        Second()

def Ka_2():             #幻化灭影
    global mp1,mp2,hp1,hp2,Jing1,Jing2,txt0,show_protect2,show_protect1,Qian_Ka
    if Jing1.name == '卡修斯':
        mp1 -= 3
        Mp1_changed()
        #********************************
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect+Jing2.protect_add ,110)
        if(Shanghai < 50 and Prob(50)):
            Jing2.protect_add -= 5
            show_protect2.configure(text ='防:{}'.format(Jing2.protect+Jing2.protect_add) )
            string = '对手的防御力-5'+'\n'
            txt0.insert(tk.END,string)

        Jing_shang1('幻化灭影',Shanghai)

        Fire_changed1(Jing1.Hp)
        if Qian_Ka > 0:
            Qian_Ka -= 1
        First()
    else:
        mp2 -= 3
        Mp2_changed()
        #********************************
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect+Jing1.protect_add ,110)
        if(Shanghai < 50 and Prob(50)):
            Jing1.protect_add -= 5
            show_protect1.configure(text ='防:{}'.format(Jing1.protect+Jing1.protect_add) )
            string = '对手的防御力-5'+'\n'
            txt0.insert(tk.END,string)

        Jing_shang2('幻化灭影',Shanghai)

        Fire_changed2(Jing2.Hp)
        if Qian_Ka > 0:
            Qian_Ka -= 1
        Second()

def Ka_3():         #乾坤反转
    global mp1,mp2,Qian_Ka
    if Jing1.name == '卡修斯':
        mp1 -= 2
        Mp1_changed()
        Qian_Ka += 3
        Fire_changed1(Jing1.Hp)
        if Qian_Ka > 0:
            Qian_Ka -= 1
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        Qian_Ka += 3
        Fire_changed2(Jing2.Hp)
        if Qian_Ka > 0:
            Qian_Ka -= 1
        Second()
def Ka_4():         #山神之力
    global mp1,mp2,Qian_Ka
    global Jing1,Jing2,show_protect1,show_protect2
    global show_fight1,show_fight2
    #******************************
    if Jing1.name == '卡修斯':
        mp1 -= 1
        Mp1_changed()
        if (Prob(50)):
            Jing2.fight_add -= 5
            show_fight2.configure(text ='攻:{}'.format(Jing2.fight+Jing2.fight_add) )
        else:
            Jing2.protect_add -= 5
            show_protect2.configure(text ='防:{}'.format(Jing2.protect+Jing2.protect_add) )
        Fire_changed1(Jing1.Hp)
        if Qian_Ka > 0:
            Qian_Ka -= 1
        First()
    else:
        mp2 -= 1
        Mp2_changed()
        if (Prob(50)):
            Jing1.fight_add -= 5
            show_fight1.configure(text ='攻:{}'.format(Jing1.fight+Jing1.fight_add) )
        else:
            Jing1.protect_add -= 5
            show_protect1.configure(text ='防:{}'.format(Jing1.protect+Jing1.protect_add) )
        Fire_changed2(Jing2.Hp)
        if Qian_Ka > 0:
            Qian_Ka -= 1
        Second()
def Yu_1():         #瑞流龙击打
    global mp1,mp2,hp1,hp2,Jing1,Jing2,txt0,Hai_Yu,Rui_Yu
    if Jing1.name == '鱼龙王':
        mp1 -= 5
        Mp1_changed()
        #********************************
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect_add+Jing2.protect ,150)
        Rui_Yu += 1

        Jing_shang1('瑞流龙击打',Shanghai)

        if(15 * Rui_Yu > 30):
            temp = 30
        else:
            temp = 15 * Rui_Yu
        hp2 = hp2 -  temp
        string = '瑞流龙击打的额外伤害'+'{}'.format(temp)+'\n'
        txt0.insert(tk.END,string)
        Hp2_changed()
        if (not Hai_Yu):
            Fire_changed1(Jing1.Hp)
        First()
    else:
        mp2 -= 5
        Mp2_changed()
        #********************************
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect_add+Jing1.protect ,150)
        Rui_Yu += 1

        Jing_shang2('瑞流龙击打',Shanghai)

        if(15 * Rui_Yu > 30):
            temp = 30
        else:
            temp = 15 * Rui_Yu
        hp1 = hp1 - temp
        string = '瑞流龙击打的额外伤害'+'{}'.format(temp)+'\n'
        txt0.insert(tk.END,string)
        Hp1_changed()
        if (not Hai_Yu):
            Fire_changed2(Jing2.Hp)
        Second()

def Yu_2():             #排山倒海
    global mp1,mp2,hp1,hp2,Jing1,Jing2,txt0,Hai_Yu
    if Jing1.name == '鱼龙王':
        mp1 -= 3
        Mp1_changed()
        #********************************
        if hp1 <= 150:
            temp = 2
            string = '排山倒海伤害翻倍'+'\n'
            txt0.insert(tk.END,string)
        else:
            temp = 1
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect_add+Jing2.protect ,100*temp)

        Jing_shang1('排山倒海',Shanghai)

        if (not Hai_Yu):
            Fire_changed1(Jing1.Hp)
        First()
    else:
        mp2 -= 3
        Mp2_changed()
        #********************************
        if hp2 <= 150:
            temp = 2
            string = '排山倒海伤害翻倍'+'\n'
            txt0.insert(tk.END,string)
        else:
            temp = 1
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect_add+Jing1.protect ,100*temp)

        Jing_shang2('排山倒海',Shanghai)

        if (not Hai_Yu):
            Fire_changed2(Jing2.Hp)
        Second()

def Yu_3():         #海之祝愿
    global mp1,mp2,hp1,hp2,Jing1,Jing2,txt0,Hai_Yu,show_fight1,show_fight2,show_protect1,show_protect2
    if Jing1.name == '鱼龙王':
        mp1 -= 2
        Mp1_changed()
        if hp1 > 0:
            Hai_Yu = 1
            string = '海之祝愿消除了负面效果'+'\n'
            txt0.insert(tk.END,string)
            if(Jing1.fight_add < 0):
                Jing1.fight_add = 0
                show_fight1.configure(text ='攻:{}'.format(Jing1.fight+Jing1.fight_add) )
            if Jing1.protect_add < 0:
                Jing1.protect_add = 0
                show_protect1.configure(text ='防:{}'.format(Jing1.protect+Jing1.protect_add) )
        else:
            if(Prob(50)):
                hp1 =  random.randint(25,75)
                Hp1_changed()
                string = '海之祝愿恢复了'+'{}'.format(hp1)+'\n'
                txt0.insert(tk.END,string)
            else:
                string = '海之祝愿失效,死亡'+'\n'
                txt0.insert(tk.END,string)
        if(not Hai_Yu):
            Fire_changed1(Jing1.Hp)
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        if hp2 > 0:
            Hai_Yu = 1
            string = '海之祝愿消除了负面效果'+'\n'
            txt0.insert(tk.END,string)
            if(Jing2.fight_add < 0):
                Jing2.fight_add = 0
                show_fight2.configure(text ='攻:{}'.format(Jing2.fight+Jing2.fight_add) )
            if Jing2.protect_add < 0:
                Jing2.protect_add = 0
                show_protect2.configure(text ='防:{}'.format(Jing2.protect+Jing2.protect_add) )
        else:
            if(Prob(50)):
                hp2 =  random.randint(25,75)
                Hp2_changed()
                string = '海之祝愿恢复了'+'{}'.format(hp2)+'\n'
                txt0.insert(tk.END,string)
            else:
                string = '海之祝愿失效,死亡'+'\n'
                txt0.insert(tk.END,string)
        if (not Hai_Yu):
            Fire_changed2(Jing2.Hp)
        Second()
def Yu_4():         #祈雨
    global mp1,mp2
    global Jing1,Jing2
    global show_protect1,show_protect2
    #******************************
    if Jing1.name == '鱼龙王':
        mp1 -= 2
        Mp1_changed()
        Jing1.protect_add += 10
        show_protect1.configure(text ='防:{}'.format(Jing1.protect+Jing1.protect_add) )
        if (not Hai_Yu):
            Fire_changed1(Jing1.Hp)
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        Jing2.protect_add += 10
        show_protect2.configure(text ='防:{}'.format(Jing2.protect+Jing2.protect_add) )
        if (not Hai_Yu):
            Fire_changed2(Jing2.Hp)
        Second()
def Bu_1():         #双重暗影
    global mp1,mp2,hp1,hp2,Jing1,Jing2,txt0,show_protect2,show_protect1,show_fight1,show_fight2,You_Bu
    if Jing1.name == '布莱克':
        mp1 -= 5
        Mp1_changed()
        #********************************
        Shanghai = Change_HP(Jing1.fight+Jing1.fight_add, Jing2.protect+Jing2.protect_add ,160)
        if(Prob(50)):
                Jing2.protect_add -= 10
                show_protect2.configure(text ='防:{}'.format(Jing2.protect+Jing2.protect_add) )
                string = '对手的防御力-10'+'\n'
                txt0.insert(tk.END,string)
        else:
                Jing1.fight_add += 10
                show_fight1.configure(text ='攻:{}'.format(Jing1.fight+Jing1.fight_add) )
                string = '自己的攻击力+10'+'\n'
                txt0.insert(tk.END,string)

        Jing_shang1('双重暗影',Shanghai)
        if You_Bu > 0:
            You_Bu -= 1
        Fire_changed1(Jing1.Hp)
        First()
    else:
        mp2 -= 5
        Mp2_changed()
        #********************************
        Shanghai = Change_HP(Jing2.fight+Jing2.fight_add, Jing1.protect+Jing1.protect_add ,160)
        if(Prob(50)):
                Jing1.protect_add -= 5
                show_protect1.configure(text ='防:{}'.format(Jing1.protect+Jing1.protect_add) )
                string = '对手的防御力-10'+'\n'
                txt0.insert(tk.END,string)
        else:
                Jing2.fight_add += 5
                show_fight2.configure(text ='攻:{}'.format(Jing2.fight+Jing2.fight_add) )
                string = '自己的攻击力+10'+'\n'
                txt0.insert(tk.END,string)

        Jing_shang2('双重暗影',Shanghai)
        if You_Bu > 0:
            You_Bu -= 1
        Fire_changed2(Jing2.Hp)
        Second()

def Bu_2():         #夜魔之球
    global txt0,Jing2,mp2,show_protect1,show_protect2
    global mp1,Jing1,hp1,hp2,show_fight1,show_fight2,You_Bu
    #********************************
    if Jing1.name == '布莱克':
        mp1 -= 3
        Mp1_changed()
        shanghai = Change_HP(Jing1.fight+Jing1.fight_add , Jing2.protect+Jing2.protect_add, 120)

        Jing_shang1('夜魔之球',shanghai)
        if(Jing2.protect_add > 0):
            Jing2.protect_add = 0#技能效果
        if(Jing2.fight_add>0):
            Jing2.fight_add = 0
        show_fight2.configure(text='攻:{}'.format(Jing2.fight +Jing2.fight_add))
        show_protect2.configure(text='防:{}'.format(Jing2.protect+Jing2.protect_add))
        Fire_changed1(Jing1.Hp)             #烧伤判断
        if You_Bu > 0:
            You_Bu -= 1
        First()
    else:
        mp2 -= 3
        Mp2_changed()
        shanghai = Change_HP(Jing2.fight+Jing2.fight_add , Jing1.protect+Jing1.protect_add, 120)

        Jing_shang2('夜魔之球',shanghai)
        if Jing1.protect_add > 0:
            Jing1.protect_add = 0#技能效果
        if Jing2.fight_add > 0:
            Jing1.fight_add = 0
        show_fight1.configure(text='攻:{}'.format(Jing1.fight +Jing1.fight_add))
        show_protect1.configure(text='防:{}'.format(Jing1.protect+Jing1.protect_add))
        Fire_changed2(Jing2.Hp)
        if You_Bu > 0:
            You_Bu -= 1
        Second()
def Bu_3():             #幽幻之盾
    global mp1,mp2,You_Bu
    if Jing1.name == '布莱克':
        mp1 -= 2
        Mp1_changed()
        You_Bu += 2
        Fire_changed1(Jing1.Hp)
        if You_Bu > 0:
            You_Bu -= 1
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        You_Bu += 2
        if You_Bu > 0:
            You_Bu -= 1
        Fire_changed2(Jing2.Hp)
        Second()
def Bu_4():             #深黑恐惧
    global mp1,mp2,You_Bu
    global Jing1,Jing2
    global show_protect1,show_protect2
    #******************************
    if Jing1.name == '布莱克':
        mp1 -= 2
        Mp1_changed()
        Jing2.protect_add -= 10
        show_protect2.configure(text ='防:{}'.format(Jing2.protect+Jing2.protect_add) )
        Fire_changed1(Jing1.Hp)
        if You_Bu > 0:
            You_Bu -= 1
        First()
    else:
        mp2 -= 2
        Mp2_changed()
        Jing1.protect_add -= 10
        show_protect1.configure(text ='防:{}'.format(Jing1.protect+Jing1.protect_add) )
        Fire_changed2(Jing2.Hp)
        if You_Bu > 0:
            You_Bu -= 1
        Second()
#***************************************************************
root = tk.Tk()
root.geometry('2500x1500')
root.title('赛尔号')

lb1 = tk.Label(root, text='***VS***',fg='red',font=('仿宋',32))
lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)

string0 = Matrix[first][6]

(string1,string2,string3,string4)=(string0+'_1', string0+'_2' , string0+'_3' , string0+'_4')

Jing1 = Animal(Matrix[first][1] , eval(Matrix[first][2]) , 0 , eval(Matrix[first][3]) , 0 ,\
    eval(Matrix[first][4]) , eval(Matrix[first][5]) ,\
    eval(string1),eval(string2),eval(string3),eval(string4),\
    Matrix[first][7],Matrix[first][8],Matrix[first][9],Matrix[first][10],\
    Matrix[first][11],Matrix[first][12],Matrix[first][13],Matrix[first][14],\
    eval(Matrix[first][15]) , eval(Matrix[first][16]) , eval(Matrix[first][17]) , eval(Matrix[first][18]) )


string0 = Matrix[second][6]

(string1,string2,string3,string4)=(string0+'_1', string0+'_2' , string0+'_3' , string0+'_4')

Jing2 = Animal(Matrix[second][1] , eval(Matrix[second][2]) , 0 , eval(Matrix[second][3]) , 0 ,\
    eval(Matrix[second][4]) , eval(Matrix[second][5]) ,\
    eval(string1),eval(string2),eval(string3),eval(string4),\
    Matrix[second][7],Matrix[second][8],Matrix[second][9],Matrix[second][10],\
    Matrix[second][11],Matrix[second][12],Matrix[second][13],Matrix[second][14],\
    eval(Matrix[second][15]) , eval(Matrix[second][16]) , eval(Matrix[second][17]) , eval(Matrix[second][18]) )

if Jing1.speed < Jing2.speed:
    (Jing1,Jing2) = (Jing2,Jing1)

hp1 = Jing1.Hp
hp2 = Jing2.Hp
mp1 = 8
mp2 = 5
#*******************************************************************
Hp_show1 = tk.Label(root ,bg='red',font=('Arial',1))#左边精灵的血条
Hp_show1.place(relx=0.1 , rely=0.2 , width=Jing1.Hp , relheight=0.03)

Hp1 = tk.Label( root ,text='HP:{}'.format(Jing1.Hp) ,fg='red',font=('Arial',16) )#左边精灵的血值
Hp1.place(relx=0.1,rely=0.1,width=80,relheight=0.1)

Mp1 = tk.Label(root ,text='MP:{}'.format(mp1) ,fg='blue',font=('Arial',16))
Mp1.place(relx=0.2,rely=0.1,width=80,relheight=0.1)

Hp_show2 = tk.Label(root , bg = 'red' , font = ('Arial',1))#右边精灵的血条
Hp_show2.place(relx=0.7,rely=0.2 , width=Jing2.Hp,relheight=0.03)

Hp2 = tk.Label(root , text='Hp:{}'.format(Jing2.Hp) , fg='red' , font=('Arial',16) )#右边精灵的血值
Hp2.place(relx=0.9,rely=0.1,width=80,relheight=0.1)

Mp2 = tk.Label(root ,text='MP:{}'.format(mp2) ,fg='blue',font=('Arial',16))
Mp2.place(relx=0.8,rely=0.1,width=80,relheight=0.1)
#******************************************************************
string = 'E:\\学习\\程序设计\\项目集合\\Python\\赛尔号\\Photo\\'     #显示照片
photo1 = Jing1.name +'1.jpg'
photo1 = string + photo1
photo2 = Jing2.name + '2.jpg'
photo2 = string + photo2

animal_1 =Image.open(photo1)
animal_1 = animal_1.resize( (320,350) )
img_png1 = ImageTk.PhotoImage(animal_1)
show_a1 = tk.Label(root , image = img_png1)
show_a1.place(relx=0.1,rely=0.35,width=320,height=350)


animal_2 =Image.open(photo2)
animal_2 = animal_2.resize( (320,350) )
img_png2 = ImageTk.PhotoImage(animal_2)
show_a2 = tk.Label(root , image = img_png2)
show_a2.place(relx=0.7,rely=0.35,width=320,height=350)
#********************************************************************
txt = tk.Message(root,bg='green',text='用完技能后等待一秒')
txt.place(relx = 0.45 , rely =0.3,width=100,height=50 )
#txt.insert(tk.END,'等待2秒\n')

txt1 = tk.Message(root , bg='green',text=Jing1.att1_eff)
txt1.place(relx=0.3 ,rely = 0.9 , width=100 , height=70)

txt2 = tk.Message(root , bg='green',text=Jing1.att2_eff)
txt2.place(relx=0.4 ,rely = 0.9 , width=100 , height=70)

txt3 = tk.Message(root , bg='green',text=Jing1.att3_eff)
txt3.place(relx=0.5 ,rely = 0.9 , width=100 , height=70)

txt4 = tk.Message(root , bg='green',text=Jing1.att4_eff)
txt4.place(relx=0.6 ,rely = 0.9 , width=100 , height=70)

txt0 = tk.Text(root,bg='light blue')
txt0.place(relx=0.40 , rely = 0.4 , width=300 , height=200)
#******************************************************************
filename = 'E:\\学习\\程序设计\\项目集合\\Python\\赛尔号\\测试1\\背景音乐\\Music\\Sai'
I = random.randint(1,6)
filename = filename + '_{}.mp3'.format(I)
playMusic(filename)
#************************************************************************

show_fight1 = tk.Label(root , text='攻:{}'.format(Jing1.fight) , fg='red' , font=('Arial',16) )#左边精灵的攻击力
show_fight1.place(relx=0.1,rely=0.25,width=80,relheight=0.1)
show_protect1 = tk.Label(root , text='防:{}'.format(Jing1.protect) , fg='blue' , font=('Arial',16) )#左边精灵的防御力
show_protect1.place(relx=0.2,rely=0.25,width=80,relheight=0.1)

show_fight2 = tk.Label(root , text='攻:{}'.format(Jing2.fight) , fg='red' , font=('Arial',16) )#右边精灵的攻击力
show_fight2.place(relx=0.8,rely=0.25,width=80,relheight=0.1)
show_protect2 = tk.Label(root , text='防:{}'.format(Jing2.protect) , fg='blue' , font=('Arial',16) )#右边精灵的防御力
show_protect2.place(relx=0.9,rely=0.25,width=80,relheight=0.1)

#***********************************************************************
attacka_1 = tk.Button(root , text=Jing1.att1_name , command=Jing1.attact1 ,relief='groove',bg='gray',fg='red')
attacka_1.place(relx=0.3 , rely=0.8 , width=100,height=50)

attacka_2 = tk.Button(root , text=Jing1.att2_name , command=Jing1.attact2 , relief='groove',bg='gray',fg='red')
attacka_2.place(relx=0.4 , rely=0.8 , width=100,height=50)

attacka_3 = tk.Button(root , text=Jing1.att3_name , command=Jing1.attact3 , relief='groove',bg='gray',fg='red')
attacka_3.place(relx=0.5 , rely=0.8 , width=100,height=50)

attacka_4 = tk.Button(root , text=Jing1.att4_name , command=Jing1.attact4 , relief='groove',bg='gray',fg='red')
attacka_4.place(relx=0.6 , rely=0.8 , width=100,height=50)

root.mainloop()










