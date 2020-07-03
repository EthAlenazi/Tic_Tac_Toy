
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
# فخto play with computer

root =Tk()
style=ttk.Style(root)
style.configure('classic')






root.title ('  مبادرة مليون مبرمج عربي : اللاعب الاول ')
ActivPlayer =1
P1 =[]
P2 =[]

bu1 =ttk.Button (root,text='  ')
bu1.grid (row=0 ,column=0 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu1.config (command=lambda :BuClick ( 1 ))
"""
-
"""
bu2 =ttk.Button (root ,text=' ')
bu2.grid (row=0 ,column=1 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu2.config (command=lambda :BuClick ( 2 ))

bu3 =ttk.Button (root ,text=' ')
bu3.grid (row=0 ,column=2 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu3.config (command=lambda :BuClick ( 3 ))

bu4 =ttk.Button (root ,text=' ')
bu4.grid (row=1 ,column=0 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu4.config (command=lambda :BuClick ( 4 ))

bu5 =ttk.Button (root ,text=' ')
bu5.grid (row=1 ,column=1 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu5.config (command=lambda :BuClick ( 5 ))

bu6 =ttk.Button (root ,text=' ')
bu6.grid (row=1 ,column=2 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu6.config (command=lambda :BuClick ( 6 ))

bu7 =ttk.Button (root ,text=' ')
bu7.grid (row=2 ,column=0 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu7.config (command=lambda :BuClick ( 7 ))

bu8 =ttk.Button (root ,text=' ')
bu8.grid (row=2 ,column=1 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu8.config (command=lambda :BuClick ( 8 ))

bu9 =ttk.Button (root ,text=' ')
bu9.grid (row=2 ,column=2 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu9.config (command=lambda :BuClick ( 9 ))
style.configure ('TButton', background='black ')



def BuClick(id)  :  # id is the number of button
    global ActivPlayer
    global P1
    global P2
    if (ActivPlayer==1)  :  # if Active ==1 ,the plaer 1 is can play
        SetLayout (id ,'X '  )  # but X for Player 1
        P1.append (id)
        root.title ('  مبادرة مليون مبرمج عربي : اللاعب الاول '  )  # change titel of wendow if player on is active
        ActivPlayer =2
        print ('P1:{}'.format (P1 )  )  # stor the number of button in list to sure the button was clicked or not

        # AutoPlay()
        # if i used the other  chose,   the play with computer must  call this function

    elif (ActivPlayer==2)  :  # if Active ==2  ,the plaer 2 is can play
        SetLayout (id ,'O '  )  # but O for Player 1
        P2.append (id)
        root.title ('  مبادرة مليون مبرمج عربي : اللاعب الثاني ')
        ActivPlayer =1
        print ('P2:{}'.format (P2 ))
    checkWinner(  )  # check if any one is Winner


# To do what is required on the second path (social intelligence)
"""
def BuClick2(id):
    global ActivPlayer
    global P1
    global P2
    if (ActivPlayer==1):
        SetLayout(id,'X')
        P1.append(id)
        root.title('  مبادرة مليون مبرمج عربي : اللاعب الاول')
        ActivPlayer=2
        print('P1:{}'.format(P1))
        AutoPlay()
"""
def SetLayout(id ,text):  # to disabled'input Xor O into button
    if (id==1):
        bu1.config (text=text)
        bu1.state (['disabled' ])
    elif (id==2):
        bu2.config (text=text)
        bu2.state (['disabled' ])
    elif (id==3):
        bu3.config (text=text)
        bu3.state (['disabled' ])
    elif (id==4):
        bu4.config (text=text)
        bu4.state (['disabled' ])
    elif (id==5):
        bu5.config (text=text)
        bu5.state (['disabled' ])
    elif (id==6):
        bu6.config (text=text)
        bu6.state (['disabled' ])
    elif (id==7):
        bu7.config (text=text)
        bu7.state (['disabled' ])
    elif (id==8):
        bu8.config (text=text)
        bu8.state (['disabled' ])
    elif (id==9):
        bu9.config (text=text)
        bu9.state (['disabled' ])


def checkWinner()  :  # The probability of winning is achieved when.
    Winer =-1
    if((1 in P1 )and (2 in P1 )and(3 in P1)):
        Winer =1
    if((1 in P2 )and (2 in P2 )and(3 in P2)):
        Winer =2
    if((4 in P1 )and (5 in P1 )and(6 in P1)):
        Winer =1
    if((4 in P2 )and (5 in P2 )and(6 in P2)):
        Winer =2
    if((7 in P1 )and (8 in P1 )and(9 in P1)):
        Winer =1
    if((7 in P2 )and (8 in P2 )and(9 in P2)):
        Winer =2
    if((1 in P1 )and (4 in P1 )and(7 in P1)):
        Winer =1
    if((1 in P2 )and (4 in P2 )and(7 in P2)):
        Winer =2
    if((2 in P1 )and (5 in P1 )and(8 in P1)):
        Winer =1
    if((2 in P2 )and (5 in P2 )and(8 in P2)):
        Winer =2
    if((3 in P1 )and (6 in P1 )and(9 in P1)):
        Winer =1
    if((3 in P2 )and (6 in P2 )and(9 in P2)):
        Winer =2
    if((7 in P1 )and (8 in P1 )and(9 in P1)):
        Winer =1
    if((7 in P2 )and (8 in P2 )and(9 in P2)):
        Winer =2
    if((7 in P1 )and (5 in P1 )and(3 in P1)):
        Winer =1
    if((7 in P2 )and (5 in P2 )and(3 in P2)):
        Winer =2
    if((1 in P1 )and (5 in P1 )and(9 in P1)):
        Winer =1
    if((1 in P2 )and (5 in P2 )and(9 in P2)):
        Winer =2
    if(Winer==1):
        messagebox.showinfo (title='Cong',message='player one is winner  '  )  # if Game is over show message ,Who is winner
        messagebox.askretrycancel ("Title","Game is over, restart the program to play again! "  )  # show message how restart the program
    elif(Winer==2):
        messagebox.showinfo (title='Cong' ,message='player two is winner  ')
        messagebox.askretrycancel ("Title" ,"Game is over, restart the program to play again! ")


# to play with computer
def AutoPlay():
    global P1
    global P2
    Emptycell =[]
    for cell in range ( 9):
        if (not (cell +1 in P1) or (cell +1 in P2) ):
            Emptycell.append (cell + 1)
    Randomindex =randint (0 ,len (Emptycell ) - 1)
    BuClick (Emptycell[Randomindex ])


root.mainloop()