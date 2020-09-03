# todo -------------- TRIS AVANZATO --------------
import tkinter.messagebox
from tkinter import *

root = Tk()
root.geometry("1350x750+0+0")
root.title("Tris Con Bottoni")
root.configure(bg="Cadet Blue")

# todo -------------- frame vari e label --------------
Tops = Frame(root, bg="Cadet Blue", pady=2, width=1350, height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lblTitle = Label(Tops, font="arial 50 bold", text="Tris Avanzato", bd=21, bg="cadet blue", fg="cornsilk",
                 justify=CENTER)
lblTitle.grid(row=0, column=0)

MainFrame = Frame(root, bg="Powder Blue", bd=10, width=1350, height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=750, height=500, pady=2, padx=10, bg="cadet blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=560, height=500, pady=2, padx=10, bg="cadet blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="cadet blue", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=560, height=200, pady=2, padx=10, bg="cadet blue", relief=RIDGE)
RightFrame2.grid(row=1, column=0)

# todo -------------- variabili --------------
PlayerX = IntVar()
PlayerO = IntVar()

PlayerX.set(0)
PlayerO.set(0)

buttons = StringVar()
click = True
won = False


def checker(buttons):
    global click
    if buttons["text"] == " " and click:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and not click:
        buttons["text"] = "O"
        click = True
        scorekeeper()


def scorekeeper():
    global won
    if button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X":
        button1.configure(bg="powder blue")
        button2.configure(bg="powder blue")
        button3.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore X ha vinto!", "La vittoria va al giocatore X!")

    # todo ===================== SPACER =====================

    if button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X":
        button4.configure(bg="powder blue")
        button5.configure(bg="powder blue")
        button6.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore X ha vinto!", "La vittoria va al giocatore X!")

    if button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X":
        button7.configure(bg="powder blue")
        button8.configure(bg="powder blue")
        button9.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore X ha vinto!", "La vittoria va al giocatore X!")

        # todo ===================== SPACER =====================

    if button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X":
        button3.configure(bg="powder blue")
        button5.configure(bg="powder blue")
        button7.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore X ha vinto!", "La vittoria va al giocatore X!")

    if button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X":
        button1.configure(bg="powder blue")
        button5.configure(bg="powder blue")
        button9.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore X ha vinto!", "La vittoria va al giocatore X!")

        # todo ===================== SPACER =====================

    if button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X":
        button1.configure(bg="powder blue")
        button4.configure(bg="powder blue")
        button7.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore X ha vinto!", "La vittoria va al giocatore X!")

    if button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X":
        button2.configure(bg="powder blue")
        button5.configure(bg="powder blue")
        button8.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore X ha vinto!", "La vittoria va al giocatore X!")

        # todo ===================== SPACER =====================

    if button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X":
        button3.configure(bg="powder blue")
        button6.configure(bg="powder blue")
        button9.configure(bg="powder blue")
        n = int(PlayerX.get())
        score = (n + 1)
        PlayerX.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore X ha vinto!", "La vittoria va al giocatore X!")

    # todo ============== SPACER ========================================================
    # todo =============  SPACER ========================================================

    if button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O":
        button1.configure(bg="light green")
        button2.configure(bg="light green")
        button3.configure(bg="light green")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore O ha vinto!", "La vittoria va al giocatore O!")

    if button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O":
        button4.configure(bg="light green")
        button5.configure(bg="light green")
        button6.configure(bg="light green")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore O ha vinto!", "La vittoria va al giocatore O!")

    if button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O":
        button7.configure(bg="light green")
        button8.configure(bg="light green")
        button9.configure(bg="light green")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore O ha vinto!", "La vittoria va al giocatore O!")

    if button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O":
        button3.configure(bg="light green")
        button5.configure(bg="light green")
        button7.configure(bg="light green")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore O ha vinto!", "La vittoria va al giocatore O!")

    if button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O":
        button1.configure(bg="light green")
        button5.configure(bg="light green")
        button9.configure(bg="light green")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore O ha vinto!", "La vittoria va al giocatore O!")

        # todo ===================== SPACER =====================

    if button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O":
        button1.configure(bg="light green")
        button4.configure(bg="light green")
        button7.configure(bg="light green")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore O ha vinto!", "La vittoria va al giocatore O!")

    if button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O":
        button2.configure(bg="light green")
        button5.configure(bg="light green")
        button8.configure(bg="light green")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore O ha vinto!", "La vittoria va al giocatore O!")

        # todo ===================== SPACER =====================

    if button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O":
        button3.configure(bg="light green")
        button6.configure(bg="light green")
        button9.configure(bg="light green")
        n = int(PlayerO.get())
        score = (n + 1)
        PlayerO.set(score)
        won = True
        tkinter.messagebox.showinfo("Il giocatore O ha vinto!", "La vittoria va al giocatore O!")

    if ((button1["text"] == "X" or button1["text"] == "O") and (button2["text"] == "X" or button2["text"] == "O")
            and (button3["text"] == "X" or button3["text"] == "O") and (
                    button4["text"] == "X" or button4["text"] == "O")
            and (button5["text"] == "X" or button5["text"] == "O") and (
                    button6["text"] == "X" or button6["text"] == "O")
            and (button7["text"] == "X" or button7["text"] == "O") and (
                    button8["text"] == "X" or button8["text"] == "O")
            and (button9["text"] == "X" or button9["text"] == "O") and (not won)):
        tkinter.messagebox.showinfo("Pareggio!", "Giocatore X e Giocatore O hanno pareggiato!!")


def reset():
    global won
    won = False
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(bg="gainsboro")
    button2.configure(bg="gainsboro")
    button3.configure(bg="gainsboro")
    button4.configure(bg="gainsboro")
    button5.configure(bg="gainsboro")
    button6.configure(bg="gainsboro")
    button7.configure(bg="gainsboro")
    button8.configure(bg="gainsboro")
    button9.configure(bg="gainsboro")


def NewGame():
    reset()
    PlayerX.set(0)
    PlayerO.set(0)


lblPlayerX = Label(RightFrame1, font="arial 50 bold", text="Giocatore X: ", padx=2, pady=2, bg="Cadet Blue")
lblPlayerX.grid(row=0, column=0, sticky=W)
txtPlayerX = Entry(RightFrame1, font="arial 40 bold", bd=2, fg="black", textvariable=PlayerX, width=14,
                   justify=LEFT).grid(row=0, column=1)

lblPlayerO = Label(RightFrame1, font="arial 50 bold", text="Giocatore O: ", padx=2, pady=2, bg="Cadet Blue")
lblPlayerO.grid(row=1, column=0, sticky=W)
txtPlayerO = Entry(RightFrame1, font="arial 40 bold", bd=2, fg="black", textvariable=PlayerO, width=14,
                   justify=LEFT).grid(row=1, column=1)
# todo -------------- bottoni --------------
btnReset = Button(RightFrame2, text="Reset", font="Times 26 bold", height=3, width=20, bg="gainsboro", command=reset)
btnReset.grid(row=0, column=0, padx=6, pady=11)

btnNewGame = Button(RightFrame2, text="Nuova Partita", font="Times 26 bold", height=3, width=20, bg="gainsboro",
                    command=NewGame)
btnNewGame.grid(row=1, column=0, padx=6, pady=11)

# todo ---------------------------- spacer -------------------------------

button1 = Button(LeftFrame, text=" ", font="Times 26 bold", height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky=S + N + E + W)

button2 = Button(LeftFrame, text=" ", font="Times 26 bold", height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky=S + N + E + W)

button3 = Button(LeftFrame, text=" ", font="Times 26 bold", height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky=S + N + E + W)

button4 = Button(LeftFrame, text=" ", font="Times 26 bold", height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky=S + N + E + W)

button5 = Button(LeftFrame, text=" ", font="Times 26 bold", height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky=S + N + E + W)

button6 = Button(LeftFrame, text=" ", font="Times 26 bold", height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky=S + N + E + W)

button7 = Button(LeftFrame, text=" ", font="Times 26 bold", height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky=S + N + E + W)

button8 = Button(LeftFrame, text=" ", font="Times 26 bold", height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky=S + N + E + W)

button9 = Button(LeftFrame, text=" ", font="Times 26 bold", height=3, width=8, bg="gainsboro",
                 command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky=S + N + E + W)

# mainloop
root.mainloop()
