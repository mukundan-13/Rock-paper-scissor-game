from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
from random import randint

root=tk.Tk()
root.title("Rock,Paper,Scissor Game")
root.configure(background="black")


image_rock1=ImageTk.PhotoImage(Image.open("E:/rockpaper/rock1.png"))
image_paper1=ImageTk.PhotoImage(Image.open("E:/rockpaper/papermi.jpg"))
image_scissor1=ImageTk.PhotoImage(Image.open("E:/rockpaper/scissor1.png"))
image_rock2=ImageTk.PhotoImage(Image.open("E:/rockpaper/rock2.png"))
image_paper2=ImageTk.PhotoImage(Image.open("E:/rockpaper/papermm.jpg"))
image_scissor2=ImageTk.PhotoImage(Image.open("E:/rockpaper/scissor2.png"))


label_player=Label(root,image=image_scissor2)
label_computer=Label(root,image=image_scissor1)
label_computer.grid(row=1,column=0)
label_player.grid(row=1,column=3)

computer_score=Label(root,font=('arial',50,"bold"),text=0,fg="red")
player_score=Label(root,font=('arial',50,"bold"),text=0,fg="red")
computer_score.grid(row=1,column=1)
player_score.grid(row=1,column=2)

player_indicator=Label(root,font=('arial',40,'bold'),text="PLAYER",bg="orange",fg="blue")
computer_indicator=Label(root,font=('arial',40,'bold'),text="COMPUTER",bg="orange",fg="blue")
player_indicator.grid(row=0,column=3)
computer_indicator.grid(row=0,column=0)
def updateMessage(a):
    final_message['text']=a

def computer_update():
    final=int(computer_score['text'])
    final+=1
    computer_score["text"]=str(final)

def player_update():
    final=int(player_score['text'])
    final+=1
    player_score["text"]=str(final)

def winner_check(p,c):
    if p==c:
        updateMessage("Its a tie")
    elif p=="rock":
        if c=="paper":
            updateMessage("Computer wins")
            computer_update()
        else:
            updateMessage("Player wins")
            player_update()
    elif p=="paper":
        if c=="scissor":
            updateMessage("Computer wins")
            computer_update()
        else:
            updateMessage("Player wins")
            player_update()
    elif p=="scissor":
        if c=="rock":
            updateMessage("Computer wins")
            computer_update()
        else:
            updateMessage("Player wins")
            player_update()
    else:
        pass
to_select=["rock","paper","scissor"]

def choice_update(a):
    choice_computer=to_select[randint(0,2)]
    if choice_computer=="rock":
        label_computer.configure(image=image_rock2)
    elif choice_computer=="paper":
        label_computer.configure(image=image_paper2)
    else:
        label_computer.configure(image=image_scissor2)
    if a=="rock":
        label_player.configure(image=image_rock1)
    elif a=="paper":
        label_player.configure(image=image_paper1)
    else:
        label_player.configure(image=image_scissor1)

    winner_check(a,choice_computer)


        
final_message=Label(root,font=("arial",40,"bold"),bg="red",fg="white")
final_message.grid(row=3,column=2)





Button_rock=Button(root,width=16,height=3,text="ROCK",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("rock")).grid(row=2,column=0)
Button_paper=Button(root,width=16,height=3,text="PAPER",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("paper")).grid(row=2,column=2)
Button_scissor=Button(root,width=16,height=3,text="SCISSOR",font=("arial",20,"bold"),bg="yellow",fg="red",command=lambda:choice_update("scissor")).grid(row=2,column=3)



root.mainloop()





