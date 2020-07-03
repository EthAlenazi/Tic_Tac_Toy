import tkinter.messagebox
from tkinter import *


root=Tk()
root.geometry("1350x750+0+0")
root.title("Tic Tac Toy")
root.configure (background="cadet Blue")

Tops = Frame(root, bg='cadet Blue', pady=2 ,width=1350 ,height=100, relief=RIDGE)
Tops.grid(row=0,column=0)

lblTitle =Label(Tops,font=('arial',50,'bold'), text=" Tic Tac Toe Game",bd=21,bg='cadet Blue',fg='cornsilk',justify=CENTER)
lblTitle.grid(row=0,column=0)

MainFrame = Frame(root,bg="powder Blue",pady=2 ,width=1350 ,height=600, relief=RIDGE)
MainFrame.grid(row=1,column=0)

LeftFrame =Frame(MainFrame , bd=10, width=750,height=500, padx=10, pady=2, bg="cadet Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame=Frame(MainFrame , bd=10, width=560,height=500, padx=10, pady=2, bg="cadet Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1=Frame(RightFrame , bd=10, width=560,height=200, padx=10, pady=2, bg="cadet Blue", relief=RIDGE)
RightFrame1.grid(row=0,column=0)

RightFrame2=Frame(RightFrame , bd=10, width=560,height=200, padx=10, pady=2, bg="cadet Blue", relief=RIDGE)
RightFrame2.grid(row=1,column=0)



playerX=IntVar()
playerO=IntVar()


playerX.set(0)
playerO.set(0)

buttons= StringVar()
click=True

def checker(buttons):
    global click
    if buttons["text"] ==" " and click == True:
        buttons["text"] = "X"
        click=False
        scorekeeper()
    elif buttons["text"] ==" " and click == False:
         buttons["text"] = "O"
         click= True
         scorekeeper()

def scorekeeper():
    if(bu1["text"] == "X" and bu2 ["text"] == "X" and bu3["text"] == "X"):
        bu1.configure( background="red")
        bu2.configure( background="red")
        bu3.configure( background="red")
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X","you have just won a game")

    if(bu4["text"] == "X" and bu5 ["text"] == "X" and bu6["text"] == "X"):
        bu4.configure( background="red")
        bu5.configure( background="red")
        bu6.configure( background="red")
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X","you have just won a game")

    if(bu7["text"] == "X" and bu8 ["text"] == "X" and bu9["text"] == "X"):
        bu7.configure( background="red")
        bu8.configure( background="red")
        bu9.configure( background="red")
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X","you have just won a game")

    if(bu7["text"] == "X" and bu5 ["text"] == "X" and bu3["text"] == "X"):
        bu7.configure( background="red")
        bu5.configure( background="red")
        bu3.configure( background="red")
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X","you have just won a game")

    if(bu1["text"] == "X" and bu5 ["text"] == "X" and bu9["text"] == "X"):
        bu1.configure( background="red")
        bu5.configure( background="red")
        bu9.configure( background="red")
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X","you have just won a game")

    if(bu7["text"] == "X" and bu4 ["text"] == "X" and bu1["text"] == "X"):
        bu7.configure( background="red")
        bu4.configure( background="red")
        bu1.configure( background="red")
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X","you have just won a game")

    if (bu8["text"] == "X" and bu5["text"] == "X" and bu2["text"] == "X"):
        bu8.configure( background="red" )
        bu5.configure( background="red" )
        bu2.configure( background="red" )
        n = float( playerX.get() )
        score = (n + 1)
        playerX.set( score )
        tkinter.messagebox.showinfo( "winner X", "you have just won a game" )

    if(bu9["text"] == "X" and bu6 ["text"] == "X" and bu3["text"] == "X"):
        bu9.configure( background="red")
        bu6.configure( background="red")
        bu3.configure( background="red")
        n = float(playerX.get())
        score = (n + 1)
        playerX.set(score)
        tkinter.messagebox.showinfo("winner X","you have just won a game")
#******************************************************************************

    if (bu1["text"] == "O" and bu2["text"] == "O" and bu3["text"] == "O"):
        bu1.configure( background="red" )
        bu2.configure( background="red" )
        bu3.configure( background="red" )
        n = float( playerO.get() )
        score = (n + 1)
        playerO.set( score )
        tkinter.messagebox.showinfo( "winner O", "you have just won a game" )

    if (bu4["text"] == "O" and bu5["text"] == "O" and bu6["text"] == "O"):
        bu4.configure( background="red" )
        bu5.configure( background="red" )
        bu6.configure( background="red" )
        n = float( playerO.get() )
        score = (n + 1)
        playerO.set( score )
        tkinter.messagebox.showinfo( "winner O", "you have just won a game" )

    if (bu7["text"] == "O" and bu8["text"] == "O" and bu9["text"] == "O"):
        bu7.configure( background="red" )
        bu8.configure( background="red" )
        bu9.configure( background="red" )
        n = float( playerO.get() )
        score = (n + 1)
        playerO.set( score )
        tkinter.messagebox.showinfo( "winner O", "you have just won a game" )

    if (bu7["text"] == "O" and bu5["text"] == "O" and bu3["text"] == "O"):
        bu7.configure( background="red" )
        bu5.configure( background="red" )
        bu3.configure( background="red" )
        n = float( playerO.get() )
        score = (n + 1)
        playerO.set( score )
        tkinter.messagebox.showinfo( "winner O", "you have just won a game" )

    if (bu1["text"] == "O" and bu5["text"] == "O" and bu9["text"] == "O"):
        bu1.configure( background="red" )
        bu5.configure( background="red" )
        bu9.configure( background="red" )
        n = float( playerO.get() )
        score = (n + 1)
        playerO.set( score )
        tkinter.messagebox.showinfo( "winner O", "you have just won a game" )

    if (bu7["text"] == "O" and bu4["text"] == "O" and bu1["text"] == "O"):
        bu7.configure( background="red" )
        bu4.configure( background="red" )
        bu1.configure( background="red" )
        n = float( playerO.get() )
        score = (n + 1)
        playerO.set( score )
        tkinter.messagebox.showinfo( "winner O", "you have just won a game" )

    if (bu8["text"] == "O" and bu5["text"] == "O" and bu2["text"] == "O"):
        bu8.configure( background="red" )
        bu5.configure( background="red" )
        bu2.configure( background="red" )
        n = float( playerO.get() )
        score = (n + 1)
        playerO.set( score )
        tkinter.messagebox.showinfo( "winner O", "you have just won a game" )

    if (bu9["text"] == "O" and bu6["text"] == "O" and bu3["text"] == "O"):
        bu9.configure( background="red" )
        bu6.configure( background="red" )
        bu3.configure( background="red" )
        n = float( playerO.get() )
        score = (n + 1)
        playerO.set( score )
        tkinter.messagebox.showinfo( "winner O", "you have just won a game" )


def reset():
    bu1['text'] = " "
    bu2['text'] = " "
    bu3['text'] = " "
    bu4['text'] = " "
    bu5['text'] = " "
    bu6['text'] = " "
    bu7['text'] = " "
    bu8['text'] = " "
    bu9['text'] = " "

    bu1.configure(background = 'gainsboro')
    bu2.configure(background = 'gainsboro')
    bu3.configure(background = 'gainsboro')
    bu4.configure(background = 'gainsboro')
    bu5.configure(background = 'gainsboro')
    bu6.configure(background = 'gainsboro')
    bu7.configure(background = 'gainsboro')
    bu8.configure(background = 'gainsboro')
    bu9.configure(background = 'gainsboro')

def NewGame():
    reset()
    playerO.set(0)
    playerX.set(0)


lblplayrX =Label(RightFrame1,font=('arial',40,'bold'), text="Player X ",padx=2,pady=2,bg='cadet Blue')
lblplayrX.grid(row=0,column=0,sticky=W)
textplayerX=Entry(RightFrame1, font=('arial',40,'bold'),bd=2,fg='black',textvariable=playerX,width=14,justify=LEFT).grid(row=0,column=1)

lblplayrO =Label(RightFrame1,font=('arial',40,'bold'), text="Player O",padx=2,pady=2,bg='cadet Blue')
lblplayrO.grid(row=1,column=0,sticky=W)
textplayerO=Entry(RightFrame1, font=('arial',40,'bold'),bd=2,fg='black',textvariable=playerO,width=14,justify=LEFT).grid(row=1,column=1)

btnReset=Button(RightFrame2,text="Reset",font=('Times 26 bold'), width=20,height=1,bg='gainsboro',command=reset)
btnReset.grid (row=0 ,column=0 )

btnNewGame =Button(RightFrame2,text="New Game ",font=('Times 26 bold'), width=20,height=1,bg='gainsboro',command=NewGame)
btnNewGame.grid (row=1 ,column=0 )




#*********************************
bu1 =Button(LeftFrame,text=" ",font=('Times 26 bold'), width=8,height=3,bg='gainsboro',command=lambda:checker(bu1))
bu1.grid (row=1 ,column=0 ,sticky='snew' )
bu2 =Button(LeftFrame,text=" ",font=('Times 26 bold'), width=8,height=3,bg='gainsboro',command=lambda:checker(bu2))
bu2.grid (row=1 ,column=1 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu3 =Button(LeftFrame,text=" ",font=('Times 26 bold'), width=8,height=3,bg='gainsboro',command=lambda:checker(bu3))
bu3.grid (row=1 ,column=2 ,sticky='snew' ,ipadx=20 ,ipady=20)
bu4 =Button(LeftFrame,text=" ",font=('Times 26 bold'), width=8,height=3,bg='gainsboro',command=lambda:checker(bu4))
bu4.grid (row=2 ,column=0,sticky='snew' ,ipadx=20 ,ipady=20)
bu5 =Button(LeftFrame,text=" ",font=('Times 26 bold'), width=8,height=3,bg='gainsboro',command=lambda:checker(bu5))
bu5.grid (row=2 ,column=1,sticky='snew' ,ipadx=20 ,ipady=20)
bu6 =Button(LeftFrame,text=" ",font=('Times 26 bold'), width=8,height=3,bg='gainsboro',command=lambda:checker(bu6))
bu6.grid (row=2 ,column=2,sticky='snew' ,ipadx=20 ,ipady=20)
bu7 =Button(LeftFrame,text=" ",font=('Times 26 bold'), width=8,height=3,bg='gainsboro',command=lambda:checker(bu7))
bu7.grid (row=3 ,column=0,sticky='snew' ,ipadx=20 ,ipady=20)
bu8 =Button(LeftFrame,text=" ",font=('Times 26 bold'), width=8,height=3,bg='gainsboro',command=lambda:checker(bu8))
bu8.grid (row=3 ,column=1,sticky='snew' ,ipadx=20 ,ipady=20)
bu9 =Button(LeftFrame,text=" ",font=('Times 26 bold'), width=8,height=3,bg='gainsboro',command=lambda:checker(bu9))
bu9.grid (row=3 ,column=2,sticky='snew' ,ipadx=20 ,ipady=20)
#*********************************


root.mainloop()