from tkinter import *
from tkinter import  ttk


def check_winner(arr):
    if any ([arr[0][0]==arr[0][1]==arr[0][2]==0,
             arr[1][0] == arr[1][1] == arr[1][2]==0,
             arr[2][0] == arr[2][1] == arr[2][2]==0,
             arr[0][0] == arr[1][0] == arr[2][0]==0,
             arr[0][1] == arr[1][1] == arr[2][1]==0,
             arr[0][2] == arr[1][2] == arr[2][2]==0,
             arr[0][0] == arr[1][1] == arr[2][2]==0,
             arr[0][2] == arr[1][1] == arr[2][0]==0,
             ]):
        return "Noughts"
    elif any([arr[0][0]==arr[0][1]==arr[0][2]==1,
             arr[1][0] == arr[1][1] == arr[1][2]==1,
             arr[2][0] == arr[2][1] == arr[2][2]==1,
             arr[0][0] == arr[1][0] == arr[2][0]==1,
             arr[0][1] == arr[1][1] == arr[2][1]==1,
             arr[0][2] == arr[1][2] == arr[2][2]==1,
             arr[0][0] == arr[1][1] == arr[2][2]==1,
             arr[0][2] == arr[1][1] == arr[2][0]==1,
             ]):
        return "Crosses"
    else:
        return ""

def On_Click(a):
    global x
    if x == "Crosses":
        start_arr[a//3][a%3] = 1
        Button(content, text=" X ", state="disabled", width=6, height=4).grid(row=a // 3 + 1, column=a % 3 + 1)
        if check_winner(start_arr) == "Crosses":
            end_game()
            return
        x = "Noughts"
        return
    if x == "Noughts":
        start_arr[a//3][a%3] = 0
        Button(content, text=" O ", state="disabled", width=6, height=4).grid(row=a // 3 + 1, column=a % 3 + 1)
        if check_winner(start_arr) == "Noughts":
            end_game()
            return
        x = "Crosses"
        return

def end_game():
    global x, start_arr, restart_btn, result_label
    for i in range(3):
        for j in range(3):
            if start_arr[i][j] == -1:
                Button(content, text="", width=6, height=4, state="disabled").grid(row=i + 1, column=j + 1)
    result_label = Label(content, text= x + " win this game")
    result_label.grid(row = 4, column = 1, columnspan = 3)
    restart_btn.grid(row = 5, column = 1)
    return

def restart():
    global start_arr, restart_btn, result_label
    start_arr = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    Button(content, text="", command=lambda: On_Click(0), width=6, height=4).grid(row=1, column=1)
    Button(content, text="", command=lambda: On_Click(1), width=6, height=4).grid(row=1, column=2)
    Button(content, text="", command=lambda: On_Click(2), width=6, height=4).grid(row=1, column=3)
    Button(content, text="", command=lambda: On_Click(3), width=6, height=4).grid(row=2, column=1)
    Button(content, text="", command=lambda: On_Click(4), width=6, height=4).grid(row=2, column=2)
    Button(content, text="", command=lambda: On_Click(5), width=6, height=4).grid(row=2, column=3)
    Button(content, text="", command=lambda: On_Click(6), width=6, height=4).grid(row=3, column=1)
    Button(content, text="", command=lambda: On_Click(7), width=6, height=4).grid(row=3, column=2)
    Button(content, text="", command=lambda: On_Click(8), width=6, height=4).grid(row=3, column=3)
    result_label.grid_forget()
    restart_btn.grid_forget()
    x = "Crosses"
    return


root = Tk()
content = ttk.Frame(root)
content.grid(column=0, row=0)
result_label = Label(content, text= "")
result_label.grid(row = 4, column = 1, columnspan = 3)
restart_btn = Button(content, text= "Restart", command= restart, width=6, height=2)
x = "Crosses"
start_arr = [[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
Label(content, text ="").grid(row = 0, column = 0)
Label(content, text =" 0 ").grid(row = 0, column = 1)
Label(content, text =" 1 ").grid(row = 0, column = 2)
Label(content, text =" 2 ").grid(row = 0, column = 3)
Label(content, text =" 0 ").grid(row = 1, column = 0)
Label(content, text =" 1 ").grid(row = 2, column = 0)
Label(content, text =" 2 ").grid(row = 3, column = 0)
#Button_0 = Button(content, )
Button(content, text="", command=lambda : On_Click(0), width=6, height=4).grid(row = 1, column = 1)
Button(content, text="", command=lambda : On_Click(1), width=6, height=4).grid(row = 1, column = 2)
Button(content, text="", command=lambda : On_Click(2), width=6, height=4).grid(row = 1, column = 3)
Button(content, text="", command=lambda : On_Click(3), width=6, height=4).grid(row = 2, column = 1)
Button(content, text="", command=lambda : On_Click(4), width=6, height=4).grid(row = 2, column = 2)
Button(content, text="", command=lambda : On_Click(5), width=6, height=4).grid(row = 2, column = 3)
Button(content, text="", command=lambda : On_Click(6), width=6, height=4).grid(row = 3, column = 1)
Button(content, text="", command=lambda : On_Click(7), width=6, height=4).grid(row = 3, column = 2)
Button(content, text="", command=lambda : On_Click(8), width=6, height=4).grid(row = 3, column = 3)

Button(content, text="Quit \ngame", command=lambda : root.destroy(), width=6, height=2).grid(row = 5, column = 4)
content.mainloop()
