# coding=UTF-8
# version 0.8
# importing needed modules
import tkinter as tk
import random
import threading
import time
from functools import partial
# lists and variables needed for program functionality
suits_list = ['Red', 'Black', "Green"]
cards_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
cards_dict = {'A': '1', '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
              '6': '6', '7': '7', '8': '8', '9': '9', '10': '10', 'J': '11',
              'Q': '12', 'K': '13'}
history_list = []
picked_card = ''
firsttime = True
coins = 10000
counter = 0


class MainApp:  # Main class for aplication which does most of the work
    def __init__(self, parent):
        default_bg = 'grey20'
        button_bg = 'grey10'
        button_fg = 'grey90'
        font = 'Bahnschrift Light SemiCondensed'

        self.Mainframe = tk.Frame(bg='grey50',  # Frame holding all widgts (everything)
                                  padx=0, pady=0)
        self.Mainframe.grid()

        # Title bar frame
        self.title_bar_frame = tk.Frame(self.Mainframe,
                                        bg=default_bg,
                                        padx=0, pady=0)
        self.title_bar_frame.grid()

        # Title bar drag button
        self.title_bar_drag_button = tk.Button(self.title_bar_frame,
                                               text='Hi-Low game version 0.8',
                                               font=(font, '9'),
                                               bg="grey5",
                                               fg="white",
                                               anchor=tk.W,
                                               relief=tk.SUNKEN,
                                               activebackground="grey5",
                                               activeforeground="white",
                                               borderwidth=0,
                                               height=0, width=141,
                                               padx=0, pady=0)
        self.title_bar_drag_button.grid(row=0, column=0, sticky=tk.W)

        # Minimise button
        self.minimise_button = tk.Button(self.title_bar_frame,
                                         text="—",
                                         font=(font, '9', 'bold'),
                                         justify=tk.LEFT,
                                         bg="grey3",
                                         fg="white",
                                         activebackground="grey3",
                                         activeforeground="white",
                                         borderwidth=0,
                                         height=0, width=3,
                                         padx=0, pady=0,
                                         command=self.minimise)
        self.minimise_button.grid(row=0, column=1)

        # Close button
        self.close_button = tk.Button(self.title_bar_frame,
                                      text="X",
                                      font=(font, '9', 'bold'),
                                      justify=tk.LEFT,
                                      bg="grey3",
                                      fg="White",
                                      activebackground="Red",
                                      activeforeground="White",
                                      borderwidth=0,
                                      height=0, width=3,
                                      padx=0, pady=0,
                                      command=root.destroy)
        self.close_button.grid(row=0, column=2)

        # Content frame holding game content
        self.content_frame = tk.Frame(self.Mainframe,
                                      bg=default_bg,
                                      padx=0, pady=0)
        self.content_frame.grid(row=1)

        # Topbar frame which holds the buttons and options for the top bar
        self.topbar_frame = tk.Frame(self.content_frame,
                                     bg="grey80",
                                     padx=0, pady=0)
        self.topbar_frame.grid(row=0, column=0, columnspan=3)

        #  label showing title of the game
        self.title_label = tk.Label(self.topbar_frame,
                                    text="Hi-Low",
                                    font="Arial 10 italic",
                                    justify=tk.LEFT,
                                    anchor=tk.W,
                                    bg="grey10",
                                    fg="white",
                                    height=0, width=63,
                                    padx=5, pady=10)
        self.title_label.grid(row=0)

        #  help button, Opens help dialouge with class Help
        self.help_button = tk.Button(self.topbar_frame,
                                     text="Help",
                                     font="Arial 10 bold",
                                     justify=tk.LEFT,
                                     bg="grey10",
                                     fg="white",
                                     bd=0,
                                     padx=10, pady=9,
                                     command=lambda: self.get_help())
        self.help_button.grid(row=0, column=1)

        #  leaderboard button, Opens the leaderboard with class Leaderboard
        self.leaderboard_button = tk.Button(self.topbar_frame,
                                            text="Leaderboard",
                                            font="Arial 10 bold",
                                            justify=tk.LEFT,
                                            bg="grey10",
                                            fg="white",
                                            bd=0,
                                            padx=10, pady=9,
                                            command=lambda: self.get_leaderboard())
        self.leaderboard_button.grid(row=0, column=2)

        #  withdraw button, Opens the leaderboard with class withdraw
        self.withdraw_button = tk.Button(self.topbar_frame,
                                         text="Withdraw",
                                         font="Arial 10 bold",
                                         justify=tk.LEFT,
                                         bg="grey10",
                                         fg="white",
                                         bd=0,
                                         padx=10, pady=9,
                                         command=lambda: self.get_withdraw())
        self.withdraw_button.grid(row=0, column=3)

        #  shows the user the amount of coins they have
        self.coins_label = tk.Label(self.topbar_frame,
                                    text=str(coins) + " coins",
                                    font="Arial 10 bold",
                                    justify=tk.LEFT,
                                    bg="grey10",
                                    fg="white",
                                    height=0, width=16,
                                    padx=0, pady=10)
        self.coins_label.grid(row=0, column=4)

        # frame to hold higher or lower buttons
        self.left_frame = tk.Frame(self.content_frame,
                                   bg=default_bg,
                                   padx=2, pady=2)
        self.left_frame.grid(row=1, column=0, padx=0, pady=20)

        #  shows user information
        self.info_label = tk.Label(self.left_frame,
                                   text='Welcome!',
                                   font='Arial 12 bold',
                                   justify=tk.LEFT,
                                   bg=default_bg,
                                   fg='white',
                                   height=0, width=25,
                                   padx=0, pady=2)
        self.info_label.grid(row=0, column=0)

        #  shows the multiplyer for betting for a higher number
        self.higher_label = tk.Label(self.left_frame,
                                     bg=default_bg,
                                     fg=button_fg,
                                     text='X10',
                                     font=(font, '14'),
                                     padx=2, pady=2)
        self.higher_label.grid(row=1)
        #  bet higher button
        self.higher_button = tk.Button(self.left_frame,
                                       bg=button_bg,
                                       fg=button_fg,
                                       text='▲',
                                       font=(font, '28'),
                                       borderwidth=0,
                                       padx=0, pady=0,
                                       width=14, height=0,
                                       command=lambda: self.inputcheck(0, 'Higher'))
        self.higher_button.grid(row=2, padx=0, pady=1)
        #  user entes amount of coins here to bet
        self.entry_box = tk.Entry(self.left_frame,
                                  font=(font, '18', 'bold'),
                                  justify=tk.CENTER,
                                  bg="grey40",
                                  fg="grey90",
                                  borderwidth=0,
                                  width=19)
        self.entry_box.grid(row=3, padx=0, pady=5)

        #  frame holding input edit button
        self.input_edit_frame = tk.Frame(self.left_frame,
                                         bg=default_bg,
                                         padx=2, pady=2)
        self.input_edit_frame.grid(row=4, column=0)

        #  clear value in input box
        self.input_clear_button = tk.Button(self.input_edit_frame,
                                            bg=button_bg,
                                            fg=button_fg,
                                            text='Clear',
                                            font=(font, '9'),
                                            borderwidth=0,
                                            padx=0, pady=0,
                                            width=4, height=0,
                                            command=lambda: self.inputmultiply('Clear'))
        self.input_clear_button.grid(row=0, column=0, padx=2, pady=0)

        #  add 100 to input button
        self.input_add_100_button = tk.Button(self.input_edit_frame,
                                              bg=button_bg,
                                              fg=button_fg,
                                              text='+100',
                                              font=(font, '9'),
                                              borderwidth=0,
                                              padx=0, pady=0,
                                              width=0, height=0,
                                              command=lambda: self.inputmultiply('+100'))
        self.input_add_100_button.grid(row=0, column=1, padx=2, pady=0)

        #   add 1000 to input button
        self.input_add_1000_button = tk.Button(self.input_edit_frame,
                                               bg=button_bg,
                                               fg=button_fg,
                                               text='+1000',
                                               font=(font, '9'),
                                               borderwidth=0,
                                               padx=0, pady=0,
                                               width=0, height=0,
                                               command=lambda: self.inputmultiply('+1000'))
        self.input_add_1000_button.grid(row=0, column=2, padx=2, pady=0)

        #  half input button
        self.inputx0_5_button = tk.Button(self.input_edit_frame,
                                          bg=button_bg,
                                          fg=button_fg,
                                          text='1/2',
                                          font=(font, '9'),
                                          borderwidth=0,
                                          padx=0, pady=0,
                                          width=0, height=0,
                                          command=lambda: self.inputmultiply(0.5))
        self.inputx0_5_button.grid(row=0, column=3, padx=2, pady=0)

        #  multiply input by 1.33 button
        self.inputx1_33_button = tk.Button(self.input_edit_frame,
                                           bg=button_bg,
                                           fg=button_fg,
                                           text='x1.33',
                                           font=(font, '9'),
                                           borderwidth=0,
                                           padx=0, pady=0,
                                           width=0, height=0,
                                           command=lambda: self.inputmultiply(1.33))
        self.inputx1_33_button.grid(row=0, column=4, padx=2, pady=0)

        #  multiply input by 1.5 button
        self.inputx1_5_button = tk.Button(self.input_edit_frame,
                                          bg=button_bg,
                                          fg=button_fg,
                                          text='x1.5',
                                          font=(font, '9'),
                                          borderwidth=0,
                                          padx=0, pady=0,
                                          width=0, height=0,
                                          command=lambda: self.inputmultiply(1.5))
        self.inputx1_5_button.grid(row=0, column=5, padx=2, pady=0)

        #  multiply input by 2 button
        self.inputx2_button = tk.Button(self.input_edit_frame,
                                        bg=button_bg,
                                        fg=button_fg,
                                        text='x2',
                                        font=(font, '9'),
                                        borderwidth=0,
                                        padx=0, pady=0,
                                        width=0, height=0,
                                        command=lambda: self.inputmultiply(2))
        self.inputx2_button.grid(row=0, column=6, padx=2, pady=0)

        #  multiply input by 2.5 button
        self.inputx2_5_button = tk.Button(self.input_edit_frame,
                                          bg=button_bg,
                                          fg=button_fg,
                                          text='x2.5',
                                          font=(font, '9'),
                                          borderwidth=0,
                                          padx=0, pady=0,
                                          width=0, height=0,
                                          command=lambda: self.inputmultiply(2.5))
        self.inputx2_5_button.grid(row=0, column=7, padx=2, pady=0)

        #  multiply input by 3 button
        self.inputx3_button = tk.Button(self.input_edit_frame,
                                        bg=button_bg,
                                        fg=button_fg,
                                        text='x3',
                                        font=(font, '9'),
                                        borderwidth=0,
                                        padx=0, pady=0,
                                        width=0, height=0,
                                        command=lambda: self.inputmultiply(3))
        self.inputx3_button.grid(row=0, column=8, padx=2, pady=0)

        #  Enters max amount of coins into input box
        self.input_max_button = tk.Button(self.input_edit_frame,
                                          bg=button_bg,
                                          fg=button_fg,
                                          text='Max',
                                          font=(font, '9'),
                                          borderwidth=0,
                                          padx=0, pady=0,
                                          width=0, height=0,
                                          command=lambda: self.inputmultiply('Max'))
        self.input_max_button.grid(row=0, column=9, padx=2, pady=0)

        #  bet lower button
        self.lower_button = tk.Button(self.left_frame,
                                      bg=button_bg,
                                      fg=button_fg,
                                      text='▼',
                                      font=(font, '28'),
                                      borderwidth=0,
                                      padx=0, pady=0,
                                      width=14, height=0,
                                      command=lambda: self.inputcheck(0, 'Lower'))
        self.lower_button.grid(row=5, padx=0, pady=1)

        #  shows the multiplyer for betting for a lower number
        self.lower_label = tk.Label(self.left_frame,
                                    bg=default_bg,
                                    fg=button_fg,
                                    text='X1',
                                    font=(font, '14'),
                                    padx=2, pady=2)
        self.lower_label.grid(row=6)

        #  history button that shows the history using class History
        self.history_button = tk.Button(self.left_frame,
                                        bg=button_bg,
                                        fg=button_fg,
                                        text='History',
                                        font=(font, '13', "bold"),
                                        borderwidth=0,
                                        padx=4, pady=0,
                                        width=27, height=0,
                                        command=lambda: self.get_history())
        self.history_button.grid(row=7, column=0, padx=0, pady=2)

        # frame to hold cards
        self.center_frame = tk.Frame(self.content_frame,
                                     bg=default_bg,
                                     padx=2, pady=2)
        self.center_frame.grid(row=1, column=1, padx=0, pady=20)

        #  loads random card and shows it on screen
        self.random_card()

        cardback = 'Images/Back.png'
        root.Back = Back = tk.PhotoImage(file=cardback)
        self.card = tk.Canvas(self.center_frame,
                              bg=default_bg,
                              highlightthickness=0,
                              width=242, height=336)
        self.card.create_image(121, 0, image=Cardbg, anchor=tk.N)
        self.card.create_image(121, 0, image=Cardfg, anchor=tk.N)
        self.card.create_image(121, -336, image=Back, anchor=tk.N)
        self.card.grid(row=1, padx=2, pady=10)

        # frame to hold other buttons
        self.right_frame = tk.Frame(self.content_frame,
                                    bg=default_bg,
                                    padx=2, pady=2)
        self.right_frame.grid(row=1, column=2, padx=0, pady=20)

        #  shows information to the user such as errors and which card is drawn
        self.card_label = tk.Label(self.right_frame,
                                   text='',
                                   font='Arial 12 bold',
                                   justify=tk.LEFT,
                                   bg=default_bg,
                                   fg='white',
                                   height=0, width=25,
                                   padx=0, pady=10)
        self.card_label.grid(row=0, column=0)

        self.card_label.configure(text=card_label_set)

        #  bet between 2-10
        self.two_to_ten_button = tk.Button(self.right_frame,
                                           bg=button_bg,
                                           fg=button_fg,
                                           text='2-10   x1.44',
                                           font=(font, '18', "bold"),
                                           borderwidth=0,
                                           padx=5, pady=0,
                                           width=20, height=0,
                                           command=lambda: self.inputcheck(1.44, '2,3,4,5,6,7,8,9,10'))
        self.two_to_ten_button.grid(row=1, padx=0, pady=0)

        #  frame holding  R B G bet buttons
        self.RBG_button_frame = tk.Frame(self.right_frame,
                                         bg=default_bg,
                                         padx=0, pady=2)
        self.RBG_button_frame.grid(row=2, column=0)

        #  bet Red
        self.R_button = tk.Button(self.RBG_button_frame,
                                  bg='red3',
                                  fg=button_fg,
                                  text='Red  x3',
                                  font=(font, '14', "bold"),
                                  borderwidth=0,
                                  padx=0, pady=5,
                                  width=8, height=1,
                                  command=lambda: self.inputcheck(3, 'Red'))
        self.R_button.grid(row=0, column=0, padx=0, pady=0)

        #  bet Black
        self.B_button = tk.Button(self.RBG_button_frame,
                                  bg='grey2',
                                  fg=button_fg,
                                  text='Black  x3',
                                  font=(font, '14', "bold"),
                                  borderwidth=0,
                                  padx=0, pady=5,
                                  width=8, height=1,
                                  command=lambda: self.inputcheck(3, 'Black'))
        self.B_button.grid(row=0, column=1, padx=1, pady=0)

        #  bet Green
        self.G_button = tk.Button(self.RBG_button_frame,
                                  bg='darkgreen',
                                  fg=button_fg,
                                  text='Green  x3',
                                  font=(font, '14', "bold"),
                                  borderwidth=0,
                                  padx=0, pady=5,
                                  width=8, height=1,
                                  command=lambda: self.inputcheck(3, 'Green'))
        self.G_button.grid(row=0, column=2, padx=0, pady=0)

        #  bet J, Q or K
        self.JQK_button = tk.Button(self.right_frame,
                                    bg=button_bg,
                                    fg=button_fg,
                                    text='J, Q, K   x4.33',
                                    font=(font, '18', "bold"),
                                    borderwidth=0,
                                    padx=5, pady=0,
                                    width=20, height=0,
                                    command=lambda: self.inputcheck(4.33, 'J,Q,K'))
        self.JQK_button.grid(row=3, padx=0, pady=0)

        #  ak and a bet buttons frame
        self.ak_and_a_button_frame = tk.Frame(self.right_frame,
                                              bg=default_bg,
                                              padx=2, pady=2)
        self.ak_and_a_button_frame.grid(row=4, column=0)

        #  bet A or K
        self.AK_button = tk.Button(self.ak_and_a_button_frame,
                                   bg=button_bg,
                                   fg=button_fg,
                                   text='A, K   x6.5',
                                   font=(font, '18', "bold"),
                                   borderwidth=0,
                                   padx=1, pady=0,
                                   width=10, height=0,
                                   command=lambda: self.inputcheck(6.5, 'A,K'))
        self.AK_button.grid(row=0, column=0, padx=1, pady=0)

        #  bet A
        self.A_button = tk.Button(self.ak_and_a_button_frame,
                                  bg=button_bg,
                                  fg=button_fg,
                                  text='A   x13',
                                  font=(font, '18', "bold"),
                                  borderwidth=0,
                                  padx=1, pady=0,
                                  width=10, height=0,
                                  command=lambda: self.inputcheck(13, 'A'))
        self.A_button.grid(row=0, column=1, padx=1, pady=0)

        #  bet Joker
        self.Joker_button = tk.Button(self.right_frame,
                                      bg='purple',
                                      fg=button_fg,
                                      text='JOKER   x39',
                                      font=(font, '18', "bold"),
                                      borderwidth=0,
                                      padx=5, pady=0,
                                      width=20, height=0,
                                      command=lambda: self.inputcheck(39, 'Joker'))
        self.Joker_button.grid(row=5, padx=0, pady=0)

        # Drag window if button down on title bar
        self.title_bar_drag_button.bind('<Button-1>', self.Main_pos)

        self.minimise_button.bind("<Enter>", self.minimise_on_enter)
        self.minimise_button.bind("<Leave>", self.minimise_on_leave)

        self.close_button.bind("<Enter>", self.close_on_enter)
        self.close_button.bind("<Leave>", self.close_on_leave)

        # Show window when icon poressed in taskbar
        self.Mainframe.bind("<Map>", self.mapped)

        call_popup = Popup(self)

    # Make window moveable
    def get_help(self):
        call_help = Help(self)

    def get_leaderboard(self):
        call_leaderboard = Leaderboard(self)

    def get_withdraw(self):
        call_withdraw = Withdraw(self)

    def get_history(self):
        call_history = History(self)

    def Main_pos(self, partner):
        windowx, windowy = root.winfo_rootx(), root.winfo_rooty()
        pointerx, pointery = root.winfo_pointerx(), root.winfo_pointery()
        newx, newy = (pointerx - windowx), (pointery - windowy)

        def move_window(self):
            newpointx, newpointy = root.winfo_pointerx(), root.winfo_pointery()
            root.geometry('{}x{}+{}+{}'.format(wwidth, wheight, newpointx - newx,
                                               newpointy - newy))
        self.title_bar_drag_button.bind('<B1-Motion>', move_window)

    # These definitions allow the program to be minimised
    def minimise(self):
        root.update_idletasks()
        root.overrideredirect(False)
        # root.state('withdrawn')
        root.state('iconic')

    def mapped(self, parent):
        root.update_idletasks()
        root.overrideredirect(True)
        root.state('normal')
    # These defnintions change the colour of the minimise and close button when the mouse hovers over them

    def close_on_enter(self, partner):
        self.close_button['background'] = 'red'
        self.close_button['foreground'] = 'white'

    def close_on_leave(self, partner):
        self.close_button['background'] = 'grey3'
        self.close_button['foreground'] = 'white'

    def minimise_on_enter(self, partner):
        self.minimise_button['background'] = 'grey40'
        self.minimise_button['foreground'] = 'white'

    def minimise_on_leave(self, partner):
        self.minimise_button['background'] = 'grey3'
        self.minimise_button['foreground'] = 'white'

    def inputmultiply(self, multiply):  # this definition allows the user to quickly
        # edit their betting amount so they dont have to type it out every time
        global coins
        valid_characters = '1234567890'
        inputvalue = self.entry_box.get()
        if multiply == 'Clear':
            self.entry_box.delete(0, tk.END)
        elif inputvalue != '':
            if all(char in valid_characters for char in inputvalue):
                if multiply == '+100':
                    self.entry_box.delete(0, tk.END)
                    self.entry_box.insert(0, int(inputvalue) + 100)
                elif multiply == '+1000':
                    self.entry_box.delete(0, tk.END)
                    self.entry_box.insert(0, int(inputvalue) + 1000)
                elif multiply == 'Max':
                    self.entry_box.delete(0, tk.END)
                    self.entry_box.insert(0, coins)
                else:
                    self.entry_box.delete(0, tk.END)
                    self.entry_box.insert(
                        0, int(round(float(inputvalue) * multiply)))
        if inputvalue == '':
            if multiply == '+100':
                self.entry_box.delete(0, tk.END)
                self.entry_box.insert(0, 100)
            elif multiply == '+1000':
                self.entry_box.delete(0, tk.END)
                self.entry_box.insert(0, 1000)
            elif multiply == 'Max':
                self.entry_box.delete(0, tk.END)
                self.entry_box.insert(0, coins)

    # This definition choses a random card from the deck and places it on the screen
    def random_card(self):
        global Cardbg
        global Cardfg
        global randomfg
        global randombg
        global firsttime
        global card_label_set
        if random.randint(1, 40) == 1:
            randombg = 'Joker.png'
            randomfg = 'Joker.png'
        else:
            randombg = str(random.choice(suits_list)) + '.png'
            randomfg = str(random.choice(cards_list)) + '.png'
        root.Cardbg = Cardbg = tk.PhotoImage(file='Images/' + randombg)
        root.Cardfg = Cardfg = tk.PhotoImage(file='Images/' + randomfg)
        if firsttime is True:
            if randomfg == 'Joker.png':
                picked_card = 'Joker!'
            else:
                picked_card = str(randomfg[:-4]) + ' ' + str(randombg[:-4])
            card_label_set = text = picked_card
            self.configure_higher_lower()
            firsttime = False

    #  This definition is run when a person enters an amount to bet and presses one of the bet buttons
    #  It checks if the value entred is a valid amount, if it is the Bet definition is run
    def inputcheck(self, multiplier, button):
        valid_characters = '1234567890.'
        inputvalue = self.entry_box.get()
        if inputvalue == '':
            self.info_label.configure(text="Enter an amount!")
            self.buttons_on(self, False)
        else:
            if all(char in valid_characters for char in inputvalue):
                if '.'in inputvalue:
                    self.info_label.configure(text="No decimals!")
                    self.buttons_on(self, False)
                else:
                    inputvalue = int(inputvalue)
                    if inputvalue > coins:
                        self.info_label.configure(text="insufficient funds!")
                        self.buttons_on(self, False)
                    elif inputvalue < 100:
                        self.info_label.configure(text="Minimum bet is 100!")
                        self.buttons_on(self, False)
                    else:
                        self.Bet(self, multiplier, button)
            else:
                self.info_label.configure(text="Whole numbers only!")
                self.buttons_on(self, False)

    #  This definition takes the random card made by the random_card definition and displays it with
    #  an animation and also updates the display text and updates the users balance
    def Bet(self, partner, multiplier, button):
        global counter
        global randomfg
        global randombg
        global coins

        def animate():  # This definition runs on a diffrent thread so time.sleep can be used without hanging the program
            global coins
            inputvalue = self.entry_box.get()
            self.card.delete("all")
            self.card.create_image(121, 0, image=Cardbg, anchor=tk.N)
            self.card.create_image(121, 0, image=Cardfg, anchor=tk.N)
            self.card.create_image(121, 0, image=Oldbg, anchor=tk.N)
            self.card.create_image(121, 0, image=Oldfg, anchor=tk.N)
            oldcards = str(self.card.find_all()[-1])
            if randomfg == 'Joker.png':
                picked_card = 'Joker!'
            else:
                picked_card = str(randomfg[:-4]) + ' ' + str(randombg[:-4])
            self.card_label.configure(text="Drawing card...")
            for i in range(28):
                time.sleep(0.014)
                # Parabola equation which is used to make a smooth animation
                y = 0.42857142857 * (i - 28)**2 + 336
                y = 336 - y
                self.card.create_image(121, y, image=root.Back, anchor=tk.N)
            self.card.delete(oldcards)
            self.card.delete(str(int(oldcards) - 1))
            last = self.card.find_all()[-1]
            last = last + 1
            time.sleep(0.2)
            for i in range(27):
                time.sleep(0.014)
                last = last - 1
                self.card.delete(last)
            self.card_label.configure(text=picked_card)
            # this section calculates
            card, suite = randomfg[:-4], randombg[:-4]
            # reward/loss
            if card != 'Joker':
                card_number = int(cards_dict.get(str(randomfg[:-4])))
            if card in button or suite in button:
                newcoins = int(round(float(inputvalue) * float(multiplier)))
                coins = coins + newcoins
                self.coins_label.configure(text=str(coins) + ' coins')
            if button == 'Higher':
                if card != 'Joker':
                    if card_number > int(cards_dict.get(str(Old_card[0]))):
                        newcoins = round(
                            float(self.higher_label.cget('text')[1:]) * float(inputvalue))
                        coins = coins + newcoins
            if button == 'Lower':
                if card != 'Joker':
                    if card_number < int(cards_dict.get(str(Old_card[0]))):
                        newcoins = round(
                            float(self.lower_label.cget('text')[1:]) * float(inputvalue))
                        coins = coins + newcoins
            coins = int(coins) - int(inputvalue)
            self.coins_label.configure(text=str(coins) + ' coins')
            self.buttons_on(self, False)
            if button == 'Higher':
                hilomultiplier = float(self.higher_label.cget('text')[1:])
            elif button == 'Lower':
                hilomultiplier = float(self.lower_label.cget('text')[1:])
            else:
                hilomultiplier = 0
            history_list.append(str(str(card) + '|' + suite + '|' +
                                    str(coins) + '|' + str(multiplier) + '|' + str(hilomultiplier) +
                                    '|' + str(inputvalue) + '|' + str(button)))
            self.configure_higher_lower()
        counter += 1
        self.info_label.configure(text='Welcome!')
        self.buttons_off(self, full=False)
        Oldbg, Oldfg = Cardbg, Cardfg
        if self.card_label.cget('text') != 'Joker!':
            Old_card = self.card_label.cget('text').split(' ')
        self.random_card()
        animation_thred = threading.Thread(target=animate)
        animation_thred.start()

    # definition that sets teh multipliers for high or low bet
    def configure_higher_lower(self):
        global randomfg
        card = randomfg[:-4]
        if card != 'Joker':
            card_number = int(cards_dict.get(str(randomfg[:-4])))
        if card == 'Joker':
            self.higher_label.configure(text='')
            self.higher_button['state'] = tk.DISABLED
            self.lower_label.configure(text='')
            self.lower_button['state'] = tk.DISABLED
        else:
            if card_number > 1:
                self.lower_label.configure(
                    text='x' + str(round(0.975 / (((3 * (card_number - 1)) / 40)), 2)))
            else:
                self.lower_label.configure(text='')
                self.lower_button['state'] = tk.DISABLED
            if card_number < 13:
                self.higher_label.configure(
                    text='x' + str(round(0.975 / (((3 * (13 - card_number)) / 40)), 2)))
            else:
                self.higher_label.configure(text='')
                self.higher_button['state'] = tk.DISABLED

    def buttons_off(self, partner, full):  # definition dissables all buttons
        self.higher_button['state'] = tk.DISABLED
        self.lower_button['state'] = tk.DISABLED
        self.two_to_ten_button['state'] = tk.DISABLED
        self.R_button['state'] = tk.DISABLED
        self.B_button['state'] = tk.DISABLED
        self.G_button['state'] = tk.DISABLED
        self.JQK_button['state'] = tk.DISABLED
        self.AK_button['state'] = tk.DISABLED
        self.A_button['state'] = tk.DISABLED
        self.Joker_button['state'] = tk.DISABLED
        if full is True:
            self.leaderboard_button['state'] = tk.DISABLED
            self.help_button['state'] = tk.DISABLED
            self.withdraw_button['state'] = tk.DISABLED
            self.history_button['state'] = tk.DISABLED

    def buttons_on(self, partner, full):  # definition that enables all buttons
        self.higher_button['state'] = tk.NORMAL
        self.lower_button['state'] = tk.NORMAL
        self.two_to_ten_button['state'] = tk.NORMAL
        self.R_button['state'] = tk.NORMAL
        self.B_button['state'] = tk.NORMAL
        self.G_button['state'] = tk.NORMAL
        self.JQK_button['state'] = tk.NORMAL
        self.AK_button['state'] = tk.NORMAL
        self.A_button['state'] = tk.NORMAL
        self.Joker_button['state'] = tk.NORMAL
        if full is True:
            self.leaderboard_button['state'] = tk.NORMAL
            self.help_button['state'] = tk.NORMAL
            self.withdraw_button['state'] = tk.NORMAL
            self.history_button['state'] = tk.NORMAL


class Help:
    def __init__(self, partner):
        default_bg = 'grey20'
        button_bg = 'grey10'
        button_fg = 'grey90'
        font = 'Bahnschrift Light SemiCondensed'
        self.helptoplevel = tk.Toplevel()
        self.helptoplevel.overrideredirect(True)
        self.helptoplevel.attributes('-alpha', 0.99)
        self.helptoplevel.attributes("-topmost", 1)
        hwidth, hheight = 499, 250
        self.helptoplevel.geometry('{}x{}+{}+{}'.format(hwidth, hheight, int(screen_width / 2 - hwidth / 2),
                                                        int(screen_height / 2 - hheight / 2)))
        self.helptoplevel.attributes('-alpha', 0.99)

        partner.help_button.config(state=tk.DISABLED)

        # Title bar frame
        self.title_bar_frame = tk.Frame(self.helptoplevel,
                                        bg=default_bg,
                                        padx=0, pady=0)
        self.title_bar_frame.grid(row=0, column=0)

        self.help_content_frame = tk.Frame(self.helptoplevel,
                                           bg=default_bg,
                                           padx=0, pady=0)
        self.help_content_frame.grid(row=1, column=0)

        # Title bar drag button
        self.title_bar_drag_button = tk.Button(self.title_bar_frame,
                                               text='Hi-Low game version 0.8 Help',
                                               font=(font, '9'),
                                               bg="grey5",
                                               fg="white",
                                               anchor=tk.W,
                                               relief=tk.SUNKEN,
                                               activebackground="grey5",
                                               activeforeground="white",
                                               borderwidth=0,
                                               height=0, width=77,
                                               padx=4, pady=0)
        self.title_bar_drag_button.grid(row=0, column=0, sticky=tk.W)

        # Close button
        self.close_button = tk.Button(self.title_bar_frame,
                                      text="X",
                                      font=(font, '9', 'bold'),
                                      justify=tk.LEFT,
                                      bg="grey3",
                                      fg="White",
                                      activebackground="Red",
                                      activeforeground="White",
                                      borderwidth=0,
                                      height=0, width=3,
                                      padx=0, pady=0,
                                      command=partial(self.close_help, partner))
        self.close_button.grid(row=0, column=1)

        self.help_text = tk.Label(self.help_content_frame,
                                  text='',
                                  font=(font, '12'),
                                  justify=tk.LEFT,
                                  width=0,
                                  wrap=490,
                                  bg=default_bg,
                                  fg=button_fg,
                                  padx=10, pady=10)
        self.help_text.grid(row=2)
        self.help_text.configure(text='Welcome To Hi-Low! Bet a certain amount of coins on what the next card will be. Type your ammount into the enry box or use the buttons underneth to help you quickly change your amount. Click one of the buttons to bet higher, lower, red suit, joker, etc. You can see your coins in the top left. Minimum bet is 100 coins. Try to win the most amount of coins and hit withdraw to have your name on the leaderboard. You can see other players high scores on the leaderboard aswell. Press the history button to see the past cards drawn. Good luck!\nWARNING: Gambling can be addictive, if you have gambling problems stop imediatly and call (NZ)0800 654 655 or visit www.gamblinghelpline.co.nz\nRecomended age 18+')

        self.title_bar_drag_button.bind('<Button-1>', self.Main_pos)

        self.close_button.bind("<Enter>", self.close_on_enter)
        self.close_button.bind("<Leave>", self.close_on_leave)

    # These defnintions change the colour of the minimise and close button when the mouse hovers over them
    def close_on_enter(self, partner):
        self.close_button['background'] = 'red'
        self.close_button['foreground'] = 'white'

    def close_on_leave(self, partner):
        self.close_button['background'] = 'grey3'
        self.close_button['foreground'] = 'white'

    #  Close help menue
    def close_help(self, partner):
        # Put help button back to normal
        partner.help_button.config(state=tk.NORMAL)
        self.helptoplevel.destroy()

    def Main_pos(self, partner):
        helproot = self.helptoplevel
        windowx, windowy = helproot.winfo_rootx(), helproot.winfo_rooty()
        pointerx, pointery = helproot.winfo_pointerx(), helproot.winfo_pointery()
        newx, newy = (pointerx - windowx), (pointery - windowy)

        def move_window(self):
            newpointx, newpointy = helproot.winfo_pointerx(), helproot.winfo_pointery()
            helproot.geometry('{}x{}+{}+{}'.format(499, 250, newpointx - newx,
                                                   newpointy - newy))
        self.title_bar_drag_button.bind('<B1-Motion>', move_window)


class Leaderboard:
    def __init__(self, partner):
        default_bg = 'grey20'
        button_bg = 'grey10'
        button_fg = 'grey90'
        font = 'Bahnschrift Light SemiCondensed'
        self.leaderboardtoplevel = tk.Toplevel()
        self.leaderboardtoplevel.overrideredirect(True)
        self.leaderboardtoplevel.attributes('-alpha', 0.99)
        self.leaderboardtoplevel.attributes("-topmost", 1)
        wwidth, wheight = 450, 450
        self.leaderboardtoplevel.geometry('{}x{}+{}+{}'.format(wwidth, wheight, int(screen_width / 2 - wwidth / 2),
                                                               int(screen_height / 2 - wheight / 2)))
        self.leaderboardtoplevel.attributes('-alpha', 0.99)

        partner.leaderboard_button.config(state=tk.DISABLED)

        # Title bar frame
        self.title_bar_frame = tk.Frame(self.leaderboardtoplevel,
                                        bg=default_bg,
                                        padx=0, pady=0)
        self.title_bar_frame.grid()

        # Title bar drag button
        self.title_bar_drag_button = tk.Button(self.title_bar_frame,
                                               text='Hi-Low game version 0.8 Leaderboard',
                                               font=(font, '9'),
                                               bg="grey5",
                                               fg="white",
                                               anchor=tk.W,
                                               relief=tk.SUNKEN,
                                               activebackground="grey5",
                                               activeforeground="white",
                                               borderwidth=0,
                                               height=0, width=62,
                                               padx=0, pady=0)
        self.title_bar_drag_button.grid(row=0, column=0, sticky=tk.W)

        # Close button
        self.close_button = tk.Button(self.title_bar_frame,
                                      text="X",
                                      font=(font, '9', 'bold'),
                                      justify=tk.LEFT,
                                      bg="grey3",
                                      fg="White",
                                      activebackground="Red",
                                      activeforeground="White",
                                      borderwidth=0,
                                      height=0, width=3,
                                      padx=0, pady=0,
                                      command=partial(self.close_leaderboard, partner))
        self.close_button.grid(row=0, column=1)

        self.title_bar_drag_button.bind('<Button-1>', self.Main_pos)

        self.close_button.bind("<Enter>", self.close_on_enter)
        self.close_button.bind("<Leave>", self.close_on_leave)

    # These defnintions change the colour of the minimise and close button when the mouse hovers over them
    def close_on_enter(self, partner):
        self.close_button['background'] = 'red'
        self.close_button['foreground'] = 'white'

    def close_on_leave(self, partner):
        self.close_button['background'] = 'grey3'
        self.close_button['foreground'] = 'white'

    #  Close help menue
    def close_leaderboard(self, partner):
        # Put help button back to normal
        partner.leaderboard_button.config(state=tk.NORMAL)
        self.leaderboardtoplevel.destroy()

    def Main_pos(self, partner):
        helproot = self.leaderboardtoplevel
        windowx, windowy = helproot.winfo_rootx(), helproot.winfo_rooty()
        pointerx, pointery = helproot.winfo_pointerx(), helproot.winfo_pointery()
        newx, newy = (pointerx - windowx), (pointery - windowy)

        def move_window(self):
            newpointx, newpointy = helproot.winfo_pointerx(), helproot.winfo_pointery()
            helproot.geometry('{}x{}+{}+{}'.format(450, 450, newpointx - newx,
                                                   newpointy - newy))
        self.title_bar_drag_button.bind('<B1-Motion>', move_window)


class Withdraw:
    def __init__(self, partner):
        default_bg = 'grey20'
        button_bg = 'grey10'
        button_fg = 'grey90'
        font = 'Bahnschrift Light SemiCondensed'
        self.withdrawtoplevel = tk.Toplevel()
        self.withdrawtoplevel.overrideredirect(True)
        self.withdrawtoplevel.attributes('-alpha', 0.99)
        self.withdrawtoplevel.attributes("-topmost", 1)
        _wwidth_, _wheight_ = 300, 300
        self.withdrawtoplevel.geometry('{}x{}+{}+{}'.format(_wwidth_, _wheight_, int(screen_width / 2 - _wwidth_ / 2),
                                                            int(screen_height / 2 - _wheight_ / 2)))
        self.withdrawtoplevel.attributes('-alpha', 0.99)

        partner.withdraw_button.config(state=tk.DISABLED)

        # Title bar frame
        self.title_bar_frame = tk.Frame(self.withdrawtoplevel,
                                        bg=default_bg,
                                        padx=0, pady=0)
        self.title_bar_frame.grid()

        # Title bar drag button
        self.title_bar_drag_button = tk.Button(self.title_bar_frame,
                                               text='Hi-Low game version 0.8 Withdraw',
                                               font=(font, '9'),
                                               bg="grey5",
                                               fg="white",
                                               anchor=tk.W,
                                               relief=tk.SUNKEN,
                                               activebackground="grey5",
                                               activeforeground="white",
                                               borderwidth=0,
                                               height=0, width=40,
                                               padx=0, pady=0)
        self.title_bar_drag_button.grid(row=0, column=0, sticky=tk.W)

        # Close button
        self.close_button = tk.Button(self.title_bar_frame,
                                      text="X",
                                      font=(font, '9', 'bold'),
                                      justify=tk.LEFT,
                                      bg="grey3",
                                      fg="White",
                                      activebackground="Red",
                                      activeforeground="White",
                                      borderwidth=0,
                                      height=0, width=3,
                                      padx=0, pady=0,
                                      command=partial(self.close_withdraw, partner))
        self.close_button.grid(row=0, column=1)

        self.title_bar_drag_button.bind('<Button-1>', self.Main_pos)

        self.close_button.bind("<Enter>", self.close_on_enter)
        self.close_button.bind("<Leave>", self.close_on_leave)

    # These defnintions change the colour of the minimise and close button when the mouse hovers over them
    def close_on_enter(self, partner):
        self.close_button['background'] = 'red'
        self.close_button['foreground'] = 'white'

    def close_on_leave(self, partner):
        self.close_button['background'] = 'grey3'
        self.close_button['foreground'] = 'white'

    #  Close help menue
    def close_withdraw(self, partner):
        # Put help button back to normal
        partner.withdraw_button.config(state=tk.NORMAL)
        self.withdrawtoplevel.destroy()

    def Main_pos(self, partner):
        withdrawroot = self.withdrawtoplevel
        windowx, windowy = withdrawroot.winfo_rootx(), withdrawroot.winfo_rooty()
        pointerx, pointery = withdrawroot.winfo_pointerx(), withdrawroot.winfo_pointery()
        newx, newy = (pointerx - windowx), (pointery - windowy)

        def move_window(self):
            newpointx, newpointy = withdrawroot.winfo_pointerx(), withdrawroot.winfo_pointery()
            withdrawroot.geometry('{}x{}+{}+{}'.format(300, 300, newpointx - newx,
                                                       newpointy - newy))
        self.title_bar_drag_button.bind('<B1-Motion>', move_window)


class History:
    def __init__(self, partner):
        default_bg = 'grey20'
        button_bg = 'grey10'
        button_fg = 'grey90'
        font = 'Bahnschrift Light SemiCondensed'
        self.historytoplevel = tk.Toplevel()
        self.historytoplevel.overrideredirect(True)
        self.historytoplevel.attributes('-alpha', 0.99)
        self.historytoplevel.attributes("-topmost", 1)
        _hwidth_, _hheight_ = 471, 459
        self.historytoplevel.geometry('{}x{}+{}+{}'.format(_hwidth_, _hheight_, int(screen_width / 2 - _hwidth_ / 2),
                                                           int(screen_height / 2 - _hheight_ / 2)))
        self.historytoplevel.attributes('-alpha', 0.99)

        partner.history_button.config(state=tk.DISABLED)

        # Title bar frame
        self.title_bar_frame = tk.Frame(self.historytoplevel,
                                        bg=default_bg,
                                        padx=0, pady=0)
        self.title_bar_frame.grid(row=0, column=0)

        self.history_content_frame = tk.Frame(self.historytoplevel,
                                              bg=default_bg,
                                              padx=0, pady=0)
        self.history_content_frame.grid(row=1, column=0)

        # Title bar drag button
        self.title_bar_drag_button = tk.Button(self.title_bar_frame,
                                               text='Hi-Low game version 0.8 History',
                                               font=(font, '9'),
                                               bg="grey5",
                                               fg="white",
                                               anchor=tk.W,
                                               relief=tk.SUNKEN,
                                               activebackground="grey5",
                                               activeforeground="white",
                                               borderwidth=0,
                                               height=0, width=74,
                                               padx=0, pady=0)
        self.title_bar_drag_button.grid(row=0, column=0, sticky=tk.W)

        # Close button
        self.close_button = tk.Button(self.title_bar_frame,
                                      text="X",
                                      font=(font, '9', 'bold'),
                                      justify=tk.LEFT,
                                      bg="grey3",
                                      fg="White",
                                      activebackground="Red",
                                      activeforeground="White",
                                      borderwidth=0,
                                      height=0, width=3,
                                      padx=0, pady=0,
                                      command=partial(self.close_withdraw, partner))
        self.close_button.grid(row=0, column=1, sticky=tk.W)
        self.title_bar_drag_button.bind('<Button-1>', self.Main_pos)

        self.history_text = tk.Text(self.history_content_frame,
                                    font="Arial 10 bold",
                                    bg=default_bg,
                                    fg=button_fg,
                                    height=26, width=65,
                                    padx=8, pady=12)
        self.history_text.grid(row=0, column=0)

        self.history_text.tag_configure(
            "Red", background="#8E0000", foreground=button_fg, font=(font, '14', 'bold'))
        self.history_text.tag_configure(
            "Black", background="#191919", foreground=button_fg, font=(font, '14', 'bold'))
        self.history_text.tag_configure(
            "Green", background="#008E00", foreground=button_fg, font=(font, '14', 'bold'))
        self.history_text.tag_configure(
            "Joker", background="#4E088C", foreground=button_fg, font=(font, '14', 'bold'))
        self.history_text.tag_configure(
            "Gain", background=default_bg, foreground='Green', font=(font, '11'))
        self.history_text.tag_configure(
            "Loss", background=default_bg, foreground='Red', font=(font, '11'))
        self.history_text.tag_configure(
            "extra", foreground='grey50', font=(font, '11'))

        self.close_button.bind("<Enter>", self.close_on_enter)
        self.close_button.bind("<Leave>", self.close_on_leave)
        self.update_history(partner)

    # These defnintions change the colour of the minimise and close button when the mouse hovers over them
    def close_on_enter(self, partner):
        self.close_button['background'] = 'red'
        self.close_button['foreground'] = 'white'

    def close_on_leave(self, partner):
        self.close_button['background'] = 'grey3'
        self.close_button['foreground'] = 'white'

    #  Close help menue
    def close_withdraw(self, partner):
        # Put help button back to normal
        partner.history_button.config(state=tk.NORMAL)
        self.historytoplevel.destroy()

    def update_history(self, partner):
        previous_amount = 10000
        self.history_text.configure(state="normal")
        self.history_text.delete('1.0', tk.END)
        if len(history_list) > 0:
            for items in history_list:
                history_listbreak = items.split('|')
                card, suite, amount = history_listbreak[0], history_listbreak[1], history_listbreak[2]
                gainloss = int(amount) - int(previous_amount)
                previous_amount = amount
                if history_listbreak[3] == '0':
                    multiplier = history_listbreak[4]
                else:
                    multiplier = history_listbreak[3]
                bet, btn = history_listbreak[5], history_listbreak[6]
                if btn == '2,3,4,5,6,7,8,9,10':
                    btn = '2-10'
                if suite == 'Joker':
                    self.history_text.insert('end', '[%s]' % (suite), suite)
                else:
                    self.history_text.insert(
                        'end', '[%s %s]' % (card, suite), suite)
                if gainloss >= 0:
                    self.history_text.insert('end', ' Gain:', 'extra')
                    self.history_text.insert(
                        'end', '	r +%s' % (gainloss), 'Gain')
                elif gainloss < 0:
                    self.history_text.insert('end', ' Loss:', 'extra')
                    self.history_text.insert(
                        'end', ' %s' % (gainloss), 'Loss')
                self.history_text.insert('end', '\nBet on: %s, Multiplier: x%s, Bet amount: %s, Total: %s coins\n' % (
                    btn, multiplier, bet, amount), 'extra')
        self.history_text.see("end")
        self.history_text.configure(state="disabled")

    def Main_pos(self, partner):
        historyroot = self.historytoplevel
        windowx, windowy = historyroot.winfo_rootx(), historyroot.winfo_rooty()
        pointerx, pointery = historyroot.winfo_pointerx(), historyroot.winfo_pointery()
        newx, newy = (pointerx - windowx), (pointery - windowy)

        def move_window(self):
            newpointx, newpointy = historyroot.winfo_pointerx(), historyroot.winfo_pointery()
            historyroot.geometry('{}x{}+{}+{}'.format(471, 459, newpointx - newx,
                                                      newpointy - newy))
        self.title_bar_drag_button.bind('<B1-Motion>', move_window)


class Popup:
    global randomfg

    def __init__(self, partner):
        default_bg = 'grey20'
        button_bg = 'grey10'
        button_fg = 'grey90'
        font = 'Bahnschrift Light SemiCondensed'
        self.popuptoplevel = tk.Toplevel()
        self.popuptoplevel.overrideredirect(True)
        self.popuptoplevel.attributes('-alpha', 0.99)
        self.popuptoplevel.attributes("-topmost", 1)
        _hwidth_, _hheight_ = 500, 200
        self.popuptoplevel.geometry('{}x{}+{}+{}'.format(_hwidth_, _hheight_, int(screen_width / 2 - _hwidth_ / 2),
                                                         int(screen_height / 2 - _hheight_ / 2)))
        self.popuptoplevel.attributes('-alpha', 0.99)

        partner.buttons_off(self, True)

        # Title bar frame
        self.title_bar_frame = tk.Frame(self.popuptoplevel,
                                        bg=default_bg,
                                        padx=0, pady=0)
        self.title_bar_frame.grid()

        # Title bar drag button
        self.title_bar_drag_button = tk.Button(self.title_bar_frame,
                                               text='Hi-Low game version 0.8 Popup',
                                               font=(font, '9'),
                                               bg="grey5",
                                               fg="white",
                                               anchor=tk.W,
                                               relief=tk.SUNKEN,
                                               activebackground="grey5",
                                               activeforeground="white",
                                               borderwidth=0,
                                               height=0, width=83,
                                               padx=0, pady=0)
        self.title_bar_drag_button.grid(row=0, column=0, sticky=tk.W)

        self.accept_button = tk.Button(self.popuptoplevel,
                                       text='Accept',
                                       bg=default_bg,
                                       fg=button_fg,
                                       padx=0, pady=0,
                                       command=lambda: self.close_popup(partner, True))
        self.accept_button.grid(row=1, column=0)

        self.reject_button = tk.Button(self.popuptoplevel,
                                       text='Reject',
                                       bg=default_bg,
                                       fg=button_fg,
                                       padx=0, pady=0,
                                       command=lambda: self.close_popup(partner, False))
        self.reject_button.grid(row=2, column=0)

        self.title_bar_drag_button.bind('<Button-1>', self.Main_pos)
    #  Close help menue

    def close_popup(self, partner, allow):
        if allow is True:
            partner.buttons_on(self, True)
            if str(randomfg[:-4]) == 'K':
                partner.higher_button['state'] = tk.DISABLED
            elif str(randomfg[:-4]) == 'A':
                partner.lower_button['state'] = tk.DISABLED
            elif str(randomfg[:-4]) == 'Joker':
                partner.higher_button['state'] = tk.DISABLED
                partner.lower_button['state'] = tk.DISABLED
            self.popuptoplevel.destroy()
        elif allow is False:
            root.destroy()

    def Main_pos(self, partner):
        popuproot = self.popuptoplevel
        windowx, windowy = popuproot.winfo_rootx(), popuproot.winfo_rooty()
        pointerx, pointery = popuproot.winfo_pointerx(), popuproot.winfo_pointery()
        newx, newy = (pointerx - windowx), (pointery - windowy)

        def move_window(self):
            newpointx, newpointy = popuproot.winfo_pointerx(), popuproot.winfo_pointery()
            popuproot.geometry('{}x{}+{}+{}'.format(500, 200, newpointx - newx,
                                                    newpointy - newy))
        self.title_bar_drag_button.bind('<B1-Motion>', move_window)


if __name__ == "__main__":
    root = tk.Tk()
    root.title('main')
    root.overrideredirect(True)  # turns off title bar, geometry
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    wwidth, wheight = 900, 459
    root.geometry('{}x{}+{}+{}'.format(wwidth, wheight, int(screen_width /
                                                            2 - wwidth / 2), int(screen_height / 2 - wheight / 2)))
    root.attributes('-alpha', 0.99)
    App = MainApp(root)
    root.mainloop()

