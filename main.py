from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random


class Game:
    dif = None
    # random number generate for jackpot number
    jackpot = None
    counter = 0
    L = []

    def __init__(self):
        self.load_gui_window(self.load_1st_window)

    def load_gui_window(self, gui_type):

        self.root = Tk()

        self.root.title("Jackpot")
        self.root.minsize(420, 500)
        self.root.maxsize(420, 500)

        self.root.configure(background="#3dadbc")
        # load gui window
        gui_type()
        self.root.mainloop()

    def load_new_gui(self, new_gui):
        self.root.destroy()
        self.load_gui_window(new_gui)

    def refresh_window(self):
        self.dif = None
        self.jackpot = None
        self.counter = 0
        self.L = []
        self.load_new_gui(self.load_1st_window)

    def load_1st_window(self):

        def sel():
            selection = (var.get())
            if selection == 1:
                self.jackpot = random.randint(1, 100)
                self.range = 100
            elif selection == 2:
                self.jackpot = random.randint(1, 500)
                self.range = 500
            else:
                self.jackpot = random.randint(1, 1000)
                self.range = 1000
            self.dif = 1

        self.label0 = Label(self.root, text="Guess The Number", bg="#3dadbc", fg="#fff", font=("Times", 32, "bold")).pack(pady=(20, 10))
        self.label1 = Label(self.root, text="Choose the difficulty level", bg="#3dadbc", fg="#fff", font=("Times", 20, "italic")).pack(pady=(10, 2))

        var = IntVar()
        R1 = Radiobutton(self.root, text="   Easy   ", variable=var, value=1, bg="#3dadbc", fg="red", font=("Times", 20, "bold"), width=6, command=sel).pack()
        R2 = Radiobutton(self.root, text="Medium", variable=var, value=2, bg="#3dadbc", fg="red", font=("Times", 20, "bold"), width=6, command=sel).pack()
        R3 = Radiobutton(self.root, text="   Hurd  ", variable=var, value=3, bg="#3dadbc", fg="red", font=("Times", 20, "bold"), width=6, command=sel).pack()
        self.start_btn = Button(self.root, text="Start Game", bg="#fff", fg="#FF5357", font=("Times", 20, "bold"), command=lambda: self.difficulty_set(self.dif)).pack(pady=(10, 10))

    def difficulty_set(self, get):
        if get is None:
            self.jackpot = random.randint(1, 100)
            self.range = 100
        self.load_new_gui(self.gaming_window)

    def header_menu(self):
        menu = Menu(self.root)
        self.root.configure(menu=menu)
        filemenu = Menu(menu)
        menu.add_command(label="Back", command=lambda: self.load_new_gui(self.load_1st_window))

    def gaming_window(self):
        self.header_menu()

        self.label1 = Label(self.root, text="Your jackpot number stands between 1 to " + str(self.range), bg="#3dadbc", fg="#fff", font=("Times", 15, "bold")).pack(pady=(20, 10))

        self.frame1 = Frame(self.root, bg="#3dabbc")
        self.frame1.pack(pady=(10, 10))
        self.label2 = Label(self.frame1, text="Guess a number", bg="#3dadbc", fg="yellow", font=("Times", 15, "italic")).pack(side=LEFT)
        self.input = Entry(self.frame1)
        self.input.pack(pady=(2, 10), ipady=7, ipadx=15, side=LEFT)
        self.btn = Button(self.frame1, text="Go", bg="#fff", fg="#FF5357", font=("Times", 15), command=lambda: self.gaming_rule()).pack(side=LEFT)

        if len(self.L) > 0:
            self.frame2 = Frame(self.root, bg="#3dabbc")
            self.frame2.configure(height=20)
            self.frame2.pack(pady=(10, 10))
            self.label3 = Label(self.frame2, text="Previous guesses", bg="#3dadbc", fg="red",  font=("Times New Roman", 15)).pack(side=LEFT)

            n = StringVar()
            Previous_guesses = ttk.Combobox(self.frame2, width=35, textvariable=n)
            # Adding combobox drop down list
            Previous_guesses['values'] = self.L
            Previous_guesses.pack(side=LEFT)
            Previous_guesses.current()

    def gaming_rule(self):
        guess = int(self.input.get())
        if guess <= self.range:
            self.counter += 1
            if guess > self.jackpot:
                result = "Jackpot number is lower than " + str(guess)
                self.L.insert(0, result)
                data = messagebox.askyesno("Wrong Guess", "Your guess is higher than jackpot  number, guess low. Are you want to continue?")
                if data == True:
                    self.load_new_gui(self.gaming_window)
                else:
                    ms1 = "The jackpot number is " + str(self.jackpot)
                    messagebox.showinfo("Bad luck!", str(ms1))
                    self.refresh_window()

            elif guess < self.jackpot:
                result = "Jackpot number is higher than " + str(guess)
                self.L.insert(0, result)
                data = messagebox.askyesno("Wrong Guess", "Your guess is lower than jackpot  number, guess high. Are you want to continue?")
                if data is True:
                    self.load_new_gui(self.gaming_window)
                else:
                    ms2 = "The jackpot number is " + str(self.jackpot)
                    messagebox.showinfo("Bad luck!", str(ms2))
                    self.refresh_window()

            else:
                ms3 = "Your find the jackpot number and you take total " + str(self.counter) + " step. Are you want to play again?"
                messagebox.showinfo("Congratulation!", str(ms3))
                self.refresh_window()

        else:
            ms4 = "You need to guess numbers between 1 to " + str(self.range) + ". Sorry please try again......"
            messagebox.showerror("Error", str(ms4))
            self.load_new_gui(self.gaming_window)


Game()
