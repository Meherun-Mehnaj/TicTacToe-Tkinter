from tkinter import *
import tkinter as tk
import customtkinter as ctk


class TicTacToe2(Tk):
    def __init__(self):
        super().__init__()
        self.title("TicTacToe")
        self.player = "X"
        self["bg"]="white"
        self.create_base()

    def create_base(self):
        self.button1 = Button(self, text=" ", width=10, height=5,bg="#89CFF0", command=lambda: self.clicked(self.button1))
        self.button2 = Button(self, text=" ", width=10, height=5,bg="#89CFF0",  command=lambda: self.clicked(self.button2))
        self.button3 = Button(self, text=" ", width=10, height=5,bg="#89CFF0",  command=lambda: self.clicked(self.button3))
        self.button4 = Button(self, text=" ", width=10, height=5,bg="#89CFF0",  command=lambda: self.clicked(self.button4))
        self.button5 = Button(self, text=" ", width=10, height=5,bg="#89CFF0",  command=lambda: self.clicked(self.button5))
        self.button6 = Button(self, text=" ", width=10, height=5,bg="#89CFF0",  command=lambda: self.clicked(self.button6))
        self.button7 = Button(self, text=" ", width=10, height=5,bg="#89CFF0",  command=lambda: self.clicked(self.button7))
        self.button8 = Button(self, text=" ", width=10, height=5,bg="#89CFF0",  command=lambda: self.clicked(self.button8))
        self.button9 = Button(self, text=" ", width=10, height=5,bg="#89CFF0",  command=lambda: self.clicked(self.button9))

  
        self.reset_button = ctk.CTkButton(self, width=10,text="Reset",font=("Helvetica", 16),bg_color="white", fg_color="#13274F",command=self.reset)
  
        self.menu_button = ctk.CTkButton(self, width=10,text="Menu",font=("Helvetica", 16),bg_color="white", fg_color="#13274F",command=self.back_menu)
  
        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)
        self.button4.grid(row=1, column=0)
        self.button5.grid(row=1, column=1)
        self.button6.grid(row=1, column=2)
        self.button7.grid(row=2, column=0)
        self.button8.grid(row=2, column=1)
        self.button9.grid(row=2, column=2)
  
        self.reset_button.grid(row=5, column=2)
        self.menu_button.grid(row=5, column=0)
        self.space=Label(self, text=" ", font=("Helvetica", 10),bg="white")
        self.space.grid(row=6, column=0, columnspan=3)
  

        self.label1=Label(self, text="Player X's turn", font=("Helvetica", 16),bg="white")
        self.label1.grid(row=3, column=0, columnspan=3)
        self.label2=Label(self, text="", font=("Helvetica", 16),bg="white")
        self.label2.grid(row=5, column=0, columnspan=3)

    def back_menu(self):
      self.destroy()
      from main import TicTacToeMainMenu
      c = TicTacToeMainMenu()
      c.mainloop()
      
    def clicked(self, button):
        if self.player == "X" and button["text"] == " ":
            button.config(text="X")
            self.player = "O"
            self.label1.config(text="Player O's turn")
        elif self.player == "O" and button["text"] == " ":
            button.config(text="O")
            self.player = "X"
            self.label1.config(text="Player X's turn")
        self.winner()

    def winner(self):
        if (self.button1["text"] == self.button2["text"] == self.button3["text"] != " " or
            self.button4["text"] == self.button5["text"] == self.button6["text"] != " " or
            self.button7["text"] == self.button8["text"] == self.button9["text"] != " " or
            self.button1["text"] == self.button4["text"] == self.button7["text"] != " " or
            self.button2["text"] == self.button5["text"] == self.button8["text"] != " " or
            self.button3["text"] == self.button6["text"] == self.button9["text"] != " " or
            self.button1["text"] == self.button5["text"] == self.button9["text"] != " " or
            self.button3["text"] == self.button5["text"] == self.button7["text"] != " "):
          if self.player=="X":
            self.player="O"
            self.label1.config(text=f"Player {self.player} won")

          else:
            self.player="X"
            self.label1.config(text=f"Player {self.player} won")



          # self.label1.grid(row=3,column=0,columnspan=3)

        elif (self.button1["text"] != " " and self.button2["text"] != " " and self.button3["text"] != " " and self.button4["text"] != " " and self.button5["text"] != " " and self.button6["text"] != " " and self.button7["text"] != " " and self.button8["text"] != " " and self.button9["text"] != " "):
          self.label1.config(text="Draw")

    def reset(self):
        self.button1.config(text=" ")
        self.button2.config(text=" ")
        self.button3.config(text=" ")
        self.button4.config(text=" ")
        self.button5.config(text=" ")
        self.button6.config(text=" ")
        self.button7.config(text=" ")
        self.button8.config(text=" ")
        self.button9.config(text=" ")
        self.label1.config(text="Player X's turn")

# c = TicTacToe2()
# c.mainloop()
