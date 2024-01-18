from tkinter import *
from tkinter import ttk
import csv
import random
from tkinter import messagebox
from tkinter.simpledialog import askstring


window=Tk()
window.title("Hangman")
window.geometry("750x600")
window.resizable(0,0)
window["background"]="#ffffff"
img1=PhotoImage(file="Images/VTKSCHALK.png")
img2=PhotoImage(file="Images/Play.png")
img3=PhotoImage(file="Images/Help.png")
img4=PhotoImage(file="Images/instructions.png")
img5=PhotoImage(file="Images/Highscores.png")
img6=PhotoImage(file="Images/back.png")
img8=PhotoImage(file="Images/goodluck.png")
img9=PhotoImage(file="Images/Congratulations.png")

def menu():
    global label1
    global button1
    global button2
    global button3
    label1=Label(window,image=img1,borderwidth=0,bg="#ffffff",fg="#ffffff")
    label1.pack()
    button1=Button(window,image=img2,borderwidth=0,bg="#ffffff",fg="#ffffff",command=play1,activebackground="#ffffff")
    button1.pack()
    button2=Button(window,image=img3,borderwidth=0,bg="#ffffff",fg="#ffffff",command=help1,activebackground="#ffffff")
    button2.pack()
    button3=Button(window,image=img5,borderwidth=0,bg="#ffffff",fg="#ffffff",command=highscores,activebackground="#ffffff")
    button3.pack()

def play1():
    global label1
    global button1
    global button2
    global button3
    global score
    label1.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()
    f=open("words.txt","r+")
    words=f.read()
    words=words.split(",")
    score=0
    global length
    length=len(words)
    def play():
        global guesses
        global wrong_guess
        global length
        global word
        global var
        global str_wg
        global entry
        global space
        global letter
        guess=(var.get()).upper()
        guess=guess[0]
        letter+=guess
        entry.delete(0,"end")
        if guess in word:
            for a in range(0,length):
                if guess==word[a]:
                    space[a]=guess
                    guesses+=1
        elif guess not in word:
            wrong_guess-=1
            str_wg=str(wrong_guess)
        label6.configure(text=space)
        label8.configure(text=str_wg)
        label9.configure(text=letter)
        if wrong_guess<=0 or guesses==length:
            return win()
    def win():
        global wrong_guess
        global guesses
        global length
        global word
        global score
        if wrong_guess>=1 and guesses==length:
            messagebox.showinfo("Correct","Your guesses were correct!\nYou win!")
            score+=100
            return destroy()
        elif wrong_guess==0:
            messagebox.showinfo("Wrong","Your guesses were incorrect!\nYou lose!\nThe word was:"+word)
            name=askstring("Name","Please enter your name(Otherwise, please click cancel):")
            if name is not None:
                name=str(name)
                f=open("highscores.csv","r+")
                file=csv.reader(f)
                scores={}
                for r in file:
                    scores[r[0]]=int(r[1])
                f.close()
                f=open("highscores.csv","w+")
                f.truncate(0)
                f.close()
                f=open("highscores.csv","w+")
                file=csv.writer(f,lineterminator='\n')
                if name in scores.keys():
                    if scores[name]<score:
                        scores[name]=score
                else:
                    scores[name]=score
                keys=list(scores.keys())
                for l in keys:
                    file.writerow([l,scores[l]])
                f.close()
            messagebox.showinfo("Score","Your final score is:"+str(score))
            return back1()
    def destroy():
        global label6
        global label7
        global label8
        global button6
        global entry
        global label9
        global label10
        global button7
        label6.destroy()
        label7.destroy()
        label8.destroy()
        button6.destroy()
        entry.destroy()
        label9.destroy()
        label10.destroy()
        button7.destroy()
        return game()
    def game():
        global r_int
        global guesses
        global wrong_guess
        global length
        global word
        global var
        global str_wg
        global entry
        global space
        global label6
        global label7
        global label8
        global button6
        global label9
        global letter
        global label10
        global button7
        r_int=random.randint(0,length-1)
        word=words[r_int].upper()
        length=len(word)
        space="_"
        space*=length
        space=list(space)
        label6=ttk.Label(window,text=space,borderwidth=0,background="#ffffff",foreground="#fa8072",font=("Bombtrack Demo",50))
        label6.pack(pady=20)
        label7=Label(window,text="Enter one letter per guess!",bg="#ffffff",fg="#ffa500",font=("fail",50))
        label7.pack()
        var=StringVar()
        entry=ttk.Entry(window,width=1,font=("Bombtrack Demo",50),textvariable=var)
        entry.pack()
        wrong_guess=6
        str_wg=str(wrong_guess)
        guesses=0
        button6=ttk.Button(window,text="Enter Guess!",command=play)
        button6.pack(pady=5)
        label10=Label(window,text="Number of lives left-",background="#ffffff",foreground="#ffdab9",font=("Karmatic Arcade",30))
        label10.pack()
        label8=ttk.Label(window,text=str_wg,background="#ffffff",foreground="#ffdab9",font=("Karmatic Arcade",30))
        label8.pack(pady=5)
        letter=[]
        label9=ttk.Label(window,text=letter,background="#ffffff",foreground="#2e8b57",font=("GOURMET",80))
        label9.pack()
        button7=Button(window,image=img6,borderwidth=0,bg="#ffffff",fg="#ffffff",command=back12,activebackground="#ffffff")
        button7.pack(side="right",padx=50)
    game()

def back1():
    global label6
    global label7
    global label8
    global button6
    global entry
    global label9
    global label10
    global button7
    label6.destroy()
    label7.destroy()
    label8.destroy()
    button6.destroy()
    entry.destroy()
    label9.destroy()
    label10.destroy()
    button7.destroy()
    return menu()

def back12():
    global score
    name=askstring("Name","Please enter your name(otherwise, please click cancel):")
    if name is not None:
        name=str(name)
        f=open("highscores.csv","r+")
        file=csv.reader(f)
        scores={}
        for r in file:
            scores[r[0]]=int(r[1])
        f.close()
        f=open("highscores.csv","w+")
        f.truncate(0)
        f.close()
        f=open("highscores.csv","w+")
        file=csv.writer(f,lineterminator='\n')
        if name in scores.keys():
            if scores[name]<score:
                scores[name]=score
        else:
            scores[name]=score
        keys=list(scores.keys())
        for l in keys:
            file.writerow([l,scores[l]])
        f.close()
    messagebox.showinfo("Score","Your final score is:"+str(score))      
    return back1()

def help1():
    global label1
    global button1
    global button2
    global button3
    label1.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()
    global label2
    f=open("help1.txt","r+")
    data=f.read()
    f.close()
    label2=Label(window,image=img4,borderwidth=0,bg="#ffffff",fg="#ffffff")
    label2.pack()
    global label3
    label3=Label(window,text=data,background="#ffffff",foreground="#141414",font=("Cambria",14),justify="left",wraplength=600)
    label3.pack()
    global button4
    button4=Button(window,image=img8,borderwidth=0,bg="#ffffff",fg="#ffffff",command=back2,activebackground="#ffffff")
    button4.pack(side="right",padx=50)
    
def back2():
    global label2
    global label3
    global button4
    label2.destroy()
    label3.destroy()
    button4.destroy()
    menu()

def highscores():
    global label1
    global button1
    global button2
    global button3
    label1.destroy()
    button1.destroy()
    button2.destroy()
    button3.destroy()
    global label4
    label4=Label(window,image=img9,borderwidth=0,bg="#ffffff",fg="#ffffff")
    label4.pack()
    global label5
    f=open("highscores.csv","r+")
    file=csv.reader(f)
    scores={}
    for r in file:
        scores[r[0]]=int(r[1])
    f.close()
    key=list(scores.keys())
    value=list(scores.values())
    value.sort()
    key.sort()
    output=""
    for b in range(-1,-4,-1):
        for a in key:
            if scores[a]==value[b]:
                output+=str(b)
                output+=")"
                output+=a
                output+="----"
                output+=str(value[b])
                output+="\n"
    label5=Label(window,text=output,background="#ffffff",foreground="#55342b",font=("GOURMET",85),wraplength=550)
    label5.pack()
    global button5
    button5=Button(window,image=img6,borderwidth=0,bg="#ffffff",fg="#ffffff",command=back3,activebackground="#ffffff")
    button5.pack(side="right",padx=60)

def back3():
    global label4
    global label5
    global button5
    label4.destroy()
    label5.destroy()
    button5.destroy()
    menu()

menu()

window.mainloop()
