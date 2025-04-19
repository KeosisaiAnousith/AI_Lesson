from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('OX Game')

# Player 1 [X] goes first, Player 2 [O] goes second
clicked = True
count = 0
win = False

# List to store button references
button_list = []

# Function to disable all buttons after a win
def disableButtons():
    for btn in button_list:
        btn.config(state=DISABLED)

# Function to check the winner
def checkWinner():
    global win
    win = False
    # Winning conditions for Player 1 [X]
    win_conditions = [
        # Horizontal wins (5 in a row)
        [button1, button2, button3, button4, button5],
        [button2, button3, button4, button5, button6],
        [button3, button4, button5, button6, button7],
        [button4, button5, button6, button7, button8],
        [button5, button6, button7, button8, button9],
        [button10, button11, button12, button13, button14],
        [button11, button12, button13, button14, button15],
        [button12, button13, button14, button15, button16],
        [button13, button14, button15, button16, button17],
        [button14, button15, button16, button17, button18],
        [button19, button20, button21, button22, button23],
        [button20, button21, button22, button23, button24],
        [button21, button22, button23, button24, button25],
        [button22, button23, button24, button25, button26],
        [button23, button24, button25, button26, button27],
        [button28, button29, button30, button31, button32],
        [button29, button30, button31, button32, button33],
        [button30, button31, button32, button33, button34],
        [button31, button32, button33, button34, button35],
        [button32, button33, button34, button35, button36],
        [button37, button38, button39, button40, button41],
        [button38, button39, button40, button41, button42],
        [button39, button40, button41, button42, button43],
        [button40, button41, button42, button43, button44],
        [button41, button42, button43, button44, button45],
        [button46, button47, button48, button49, button50],
        [button47, button48, button49, button50, button51],
        [button48, button49, button50, button51, button52],
        [button49, button50, button51, button52, button53],
        [button50, button51, button52, button53, button54],
        [button55, button56, button57, button58, button59],
        [button56, button57, button58, button59, button60],
        [button57, button58, button59, button60, button61],
        [button58, button59, button60, button61, button62],
        [button59, button60, button61, button62, button63],
        [button64, button65, button66, button67, button68],
        [button65, button66, button67, button68, button69],
        [button66, button67, button68, button69, button70],
        [button67, button68, button69, button70, button71],
        [button68, button69, button70, button71, button72],
        [button73, button74, button75, button76, button77],
        [button74, button75, button76, button77, button78],
        [button75, button76, button77, button78, button79],
        [button76, button77, button78, button79, button80],
        [button77, button78, button79, button80, button81],

        # Vertical wins (5 in a row)
        [button1, button10, button19, button28, button37],
        [button10, button19, button28, button37, button46],
        [button19, button28, button37, button46, button55],
        [button28, button37, button46, button55, button64],
        [button37, button46, button55, button64, button73],
        [button2, button11, button20, button29, button38],
        [button11, button20, button29, button38, button47],
        [button20, button29, button38, button47, button56],
        [button29, button38, button47, button56, button65],
        [button38, button47, button56, button65, button74],
        [button3, button12, button21, button30, button39],
        [button12, button21, button30, button39, button48],
        [button21, button30, button39, button48, button57],
        [button30, button39, button48, button57, button66],
        [button39, button48, button57, button66, button75],
        [button4, button13, button22, button31, button40],
        [button13, button22, button31, button40, button49],
        [button22, button31, button40, button49, button58],
        [button31, button40, button49, button58, button67],
        [button40, button49, button58, button67, button76],
        [button5, button14, button23, button32, button41],
        [button14, button23, button32, button41, button50],
        [button23, button32, button41, button50, button59],
        [button32, button41, button50, button59, button68],
        [button41, button50, button59, button68, button77],
        [button6, button15, button24, button33, button42],
        [button15, button24, button33, button42, button51],
        [button24, button33, button42, button51, button60],
        [button33, button42, button51, button60, button69],
        [button42, button51, button60, button69, button78],
        [button7, button16, button25, button34, button43],
        [button16, button25, button34, button43, button52],
        [button25, button34, button43, button52, button61],
        [button34, button43, button52, button61, button70],
        [button43, button52, button61, button70, button79],
        [button8, button17, button26, button35, button44],
        [button17, button26, button35, button44, button53],
        [button26, button35, button44, button53, button62],
        [button35, button44, button53, button62, button71],
        [button44, button53, button62, button71, button80],
        [button9, button18, button27, button36, button45],
        [button18, button27, button36, button45, button54],
        [button27, button36, button45, button54, button63],
        [button36, button45, button54, button63, button72],
        [button45, button54, button63, button72, button81],

        # Diagonal wins (top-left to bottom-right)
        [button1, button11, button21, button31, button41],
        [button11, button21, button31, button41, button51],
        [button21, button31, button41, button51, button61],
        [button31, button41, button51, button61, button71],
        [button41, button51, button61, button71, button81],
        [button2, button12, button22, button32, button42],
        [button12, button22, button32, button42, button52],
        [button22, button32, button42, button52, button62],
        [button32, button42, button52, button62, button72],
        [button3, button13, button23, button33, button43],
        [button13, button23, button33, button43, button53],
        [button23, button33, button43, button53, button63],
        [button4, button14, button24, button34, button44],
        [button14, button24, button34, button44, button54],
        [button5, button15, button25, button35, button45],

        # Diagonal wins (top-right to bottom-left)
        [button9, button17, button25, button33, button41],
        [button17, button25, button33, button41, button49],
        [button25, button33, button41, button49, button57],
        [button33, button41, button49, button57, button65],
        [button41, button49, button57, button65, button73],
        [button8, button16, button24, button32, button40],
        [button16, button24, button32, button40, button48],
        [button24, button32, button40, button48, button56],
        [button32, button40, button48, button56, button64],
        [button7, button15, button23, button31, button39],
        [button15, button23, button31, button39, button47],
        [button23, button31, button39, button47, button55],
        [button6, button14, button22, button30, button38],
        [button14, button22, button30, button38, button46],
        [button5, button13, button21, button29, button37]
    ]
    
    for condition in win_conditions:
        if all(btn["text"] == "X" for btn in condition):
            for btn in condition:
                btn.config(bg="#80ffaa")
            win = True
            messagebox.showinfo("OX Game", "Player 1 WINNER!!")
            disableButtons()
            return
    
    # Winning conditions for Player 2 [O]
    for condition in win_conditions:
        if all(btn["text"] == "O" for btn in condition):
            for btn in condition:
                btn.config(bg="#80ffaa")
            win = True
            messagebox.showinfo("OX Game", "Player 2 WINNER!!")
            disableButtons()
            return

# Check for a draw
def checkDraw():
    if count == 81 and win == False:
        messagebox.showinfo("OX Game", "It's a draw!")
        disableButtons()

# Button click function
def buttonClicked(button):
    global clicked, count
    if button["text"] == " " and clicked:
        button["text"] = "X"
        clicked = False
        count += 1
        checkWinner()
        checkDraw()
    elif button["text"] == " " and not clicked:
        button["text"] = "O"
        clicked = True
        count += 1
        checkWinner()
        checkDraw()
    else:
        messagebox.showerror("OX Game", "This box has already been selected!\nPick another box.")
        # Start/restart the game
def start():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global button10, button11, button12, button13, button14, button15, button16, button17, button18
    global button19, button20, button21, button22, button23, button24, button25, button26, button27
    global button28, button29, button30, button31, button32, button33, button34, button35, button36
    global button37, button38, button39, button40, button41, button42, button43, button44, button45
    global button46, button47, button48, button49, button50, button51, button52, button53, button54
    global button55, button56, button57, button58, button59, button60, button61, button62, button63
    global button64, button65, button66, button67, button68, button69, button70, button71, button72
    global button73, button74, button75, button76, button77, button78, button79, button80, button81
    global clicked, count, win

    clicked = True
    count = 0
    win = False

    # Create buttons for the game
    button1 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button1))
    button2 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button2))
    button3 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button3))
    button4 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button4))
    button5 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button5))
    button6 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button6))
    button7 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button7))
    button8 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button8))
    button9 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button9))
    button10 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button10))
    button11 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button11))
    button12 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button12))
    button13 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button13))
    button14 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button14))
    button15 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button15))
    button16 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button16))
    button17 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button17))
    button18 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button18))
    button19 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button19))
    button20 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button20))
    button21 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button21))
    button22 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button22))
    button23 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button23))
    button24 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button24))
    button25 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button25))
    button26 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button26))
    button27 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button27))
    button28 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button28))
    button29 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button29))
    button30 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button30))
    button31 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button31))
    button32 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button32))
    button33 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button33))
    button34 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button34))
    button35 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button35))
    button36 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button36))
    button37 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button37))
    button38 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button38))
    button39 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button39))
    button40 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button40))
    button41 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button41))
    button42 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button42))
    button43 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button43))
    button44 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button44))
    button45 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button45))
    button46 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button46))
    button47 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button47))
    button48 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button48))
    button49 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button49))
    button50 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button50))
    button51 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button51))
    button52 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button52))
    button53 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button53))
    button54 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button54))
    button55 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button55))
    button56 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button56))
    button57 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button57))
    button58 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button58))
    button59 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button59))
    button60 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button60))
    button61 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button61))
    button62 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button62))
    button63 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button63))
    button64 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button64))
    button65 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button65))
    button66 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button66))
    button67 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button67))
    button68 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button68))
    button69 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button69))
    button70 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button70))
    button71 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button71))
    button72 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button72))
    button73 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button73))
    button74 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button74))
    button75 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button75))
    button76 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button76))
    button77 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button77))
    button78 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button78))
    button79 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button79))
    button80 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button80))
    button81 = Button(root, text=" ", font=("Helvetica", 12), height=2, width=4, command=lambda: buttonClicked(button81))

    # Store buttons in the list
    button_list.extend([
        button1, button2, button3, button4, button5, button6, button7, button8, button9,
        button10, button11, button12, button13, button14, button15, button16, button17, button18,
        button19, button20, button21, button22, button23, button24, button25, button26, button27,
        button28, button29, button30, button31, button32, button33, button34, button35, button36,
        button37, button38, button39, button40, button41, button42, button43, button44, button45,
        button46, button47, button48, button49, button50, button51, button52, button53, button54,
        button55, button56, button57, button58, button59, button60, button61, button62, button63,
        button64, button65, button66, button67, button68, button69, button70, button71, button72,
        button73, button74, button75, button76, button77, button78, button79, button80, button81
    ])

    # Arrange buttons in a 9x9 grid
    button1.grid(row=0, column=0)
    button2.grid(row=0, column=button2.grid(row=0, column=1)
    button3.grid(row=0, column=2)
    button4.grid(row=0, column=3)
    button5.grid(row=0, column=4)
    button6.grid(row=0, column=5)
    button7.grid(row=0, column=6)
    button8.grid(row=0, column=7)
    button9.grid(row=0, column=8)

    button10.grid(row=1, column=0)
    button11.grid(row=1, column=1)
    button12.grid(row=1, column=2)
    button13.grid(row=1, column=3)
    button14.grid(row=1, column=4)
    button15.grid(row=1, column=5)
    button16.grid(row=1, column=6)
    button17.grid(row=1, column=7)
    button18.grid(row=1, column=8)

    button19.grid(row=2, column=0)
    button20.grid(row=2, column=1)
    button21.grid(row=2, column=2)
    button22.grid(row=2, column=3)
    button23.grid(row=2, column=4)
    button24.grid(row=2, column=5)
    button25.grid(row=2, column=6)
    button26.grid(row=2, column=7)
    button27.grid(row=2, column=8)

    button28.grid(row=3, column=0)
    button29.grid(row=3, column=1)
    button30.grid(row=3, column=2)
    button31.grid(row=3, column=3)
    button32.grid(row=3, column=4)
    button33.grid(row=3, column=5)
    button34.grid(row=3, column=6)
    button35.grid(row=3, column=7)
    button36.grid(row=3, column=8)

    button37.grid(row=4, column=0)
    button38.grid(row=4, column=1)
    button39.grid(row=4, column=2)
    button40.grid(row=4, column=3)
    button41.grid(row=4, column=4)
    button42.grid(row=4, column=5)
    button43.grid(row=4, column=6)
    button44.grid(row=4, column=7)
    button45.grid(row=4, column=8)

    button46.grid(row=5, column=0)
    button47.grid(row=5, column=1)
    button48.grid(row=5, column=2)
    button49.grid(row=5, column=3)
    button50.grid(row=5, column=4)
    button51.grid(row=5, column=5)
    button52.grid(row=5, column=6)
    button53.grid(row=5, column=7)
    button54.grid(row=5, column=8)

    button55.grid(row=6, column=0)
    button56.grid(row=6, column=1)
    button57.grid(row=6, column=2)
    button58.grid(row=6, column=3)
    button59.grid(row=6, column=4)
    button60.grid(row=6, column=5)
    button61.grid(row=6, column=6)
    button62.grid(row=6, column=7)
    button63.grid(row=6, column=8)

    button64.grid(row=7, column=0)
    button65.grid(row=7, column=1)
    button66.grid(row=7, column=2)
    button67.grid(row=7, column=3)
    button68.grid(row=7, column=4)
    button69.grid(row=7, column=5)
    button70.grid(row=7, column=6)
    button71.grid(row=7, column=7)
    button72.grid(row=7, column=8)

    button73.grid(row=8, column=0)
    button74.grid(row=8, column=1)
    button75.grid(row=8, column=2)
    button76.grid(row=8, column=3)
    button77.grid(row=8, column=4)
    button78.grid(row=8, column=5)
    button79.grid(row=8, column=6)
    button80.grid(row=8, column=7)
    button81.grid(row=8, column=8)

# Create menu
gameMenu = Menu(root)
root.config(menu=gameMenu)

# Create Options menu
optionMenu = Menu(gameMenu, tearoff=False)
gameMenu.add_cascade(label="Options", menu=optionMenu)
optionMenu.add_command(label="Restart Game", command=start)

# Start the game
start()
root.mainloop()