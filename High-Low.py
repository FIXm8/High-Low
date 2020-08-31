# coding=UTF-8
# version alpha0.1
import tkinter as tk
import random
import threading
import time
from functools import partial
suits_list=['Red','Black',"Green"]
cards_list=[1,2,3,4,5,6,7,8,9,'J','Q','K']
coins=10000
counter=0

class MainApp:
    def __init__(self, parent):
        default_bg='grey20'
        
        font = 'Bahnschrift Light SemiCondensed'
        
        self.Mainframe = tk.Frame(bg='grey50',
                                  padx=0, pady=0)
        self.Mainframe.grid()
        

        # Title bar frame
        self.title_bar_frame = tk.Frame(self.Mainframe,
                                        bg=default_bg,
                                        padx=0, pady=0)
        self.title_bar_frame.grid()        
        
        # Title bar drag button
        self.title_bar_drag_button = tk.Button(self.title_bar_frame,
                                               text='Hi-Low game version alpha0.1',
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

        # Content frame holding content
        self.content_frame = tk.Frame(self.Mainframe,
                                      bg=default_bg,
                                      padx=0, pady=0)
        self.content_frame.grid(row=1)
        
        
        # Topbar frame
        self.topbar_frame = tk.Frame(self.content_frame,
                                   bg="grey80",
                                   padx=0, pady=0)
        self.topbar_frame.grid(row=0, column=0, columnspan=3)   
        
        self.title_label = tk.Label(self.topbar_frame,
                                     text="Hi-Low",
                                     font="Arial 10 italic",
                                     justify=tk.LEFT,
                                     anchor=tk.W,
                                     bg="grey10",
                                     fg="white",
                                     height=0, width=65,
                                     padx=3, pady=10)
        self.title_label.grid(row=0)
        
        self.help_button = tk.Button(self.topbar_frame,
                                     text="Help",
                                     font="Arial 10 bold",
                                     justify=tk.LEFT,
                                     bg="grey10",
                                     fg="white",
                                     bd=0,
                                     padx=10, pady=9)
        self.help_button.grid(row=0, column=1)
        
        self.leaderboard_button = tk.Button(self.topbar_frame,
                                     text="Leaderboard",
                                     font="Arial 10 bold",
                                     justify=tk.LEFT,
                                     bg="grey10",
                                     fg="white",
                                     bd=0,
                                     padx=10, pady=9)
        self.leaderboard_button.grid(row=0, column=2)             
        
        self.withdraw_button = tk.Button(self.topbar_frame,
                                     text="Withdraw",
                                     font="Arial 10 bold",
                                     justify=tk.LEFT,
                                     bg="grey10",
                                     fg="white",
                                     bd=0,
                                     padx=10, pady=9)
        self.withdraw_button.grid(row=0, column=3)
        
        self.coins_label = tk.Label(self.topbar_frame,
                                     text="0 Coins",
                                     font="Arial 10 bold",
                                     justify=tk.LEFT,
                                     bg="grey10",
                                     fg="white",
                                     height=0, width=14,
                                     padx=0, pady=10)
        self.coins_label.grid(row=0, column=4)      


        # frame to hold higher or lower buttons
        self.left_frame = tk.Frame(self.content_frame,
                                   bg="red",
                                   padx=2, pady=2)
        self.left_frame.grid(row=1, column=0)
        
        self.higher_label = tk.Label(self.left_frame,
                                     bg=default_bg,
                                     text='X10',
                                     font=(font, '14'),                                
                                     padx=2, pady=2)
        self.higher_label.grid(row=0)
        
        self.higher_button = tk.Button(self.left_frame,
                                       bg=default_bg,
                                       text='▲',
                                       font=(font, '28'),
                                       padx=0, pady=0,
                                       width=8, height=0)
        self.higher_button.grid(row=1, padx=0, pady=1)
        
        self.entry_box = tk.Entry(self.left_frame,
                                  width=12,
                                  font=(font, '18', 'bold'),
                                  justify=tk.CENTER,
                                  bg="grey40",
                                  fg="grey90",
                                  borderwidth=0)
        self.entry_box.grid(row=2, padx=0, pady=1)        
        
        self.lower_button = tk.Button(self.left_frame,
                                      bg=default_bg,
                                      text='▼',
                                      font=(font, '28'),
                                      padx=0, pady=0,
                                      width=8, height=0)
        self.lower_button.grid(row=3, padx=0, pady=1)        
        
        self.lower_label = tk.Label(self.left_frame,
                                    bg=default_bg,
                                    text='X1',
                                    font=(font, '14'),
                                    padx=2, pady=2)
        self.lower_label.grid(row=4)        
        
        
        # frame to hold cards
        self.center_frame = tk.Frame(self.content_frame,
                                     bg=default_bg,
                                     padx=2, pady=2)
        self.center_frame.grid(row=1, column=1)
        
        self.info_label = tk.Label(self.center_frame,
                                     text="Welcome!",
                                     font="Arial 12 bold",
                                     justify=tk.LEFT,
                                     bg=default_bg,
                                     fg="white",
                                     height=0, width=25,
                                     padx=0, pady=10)
        self.info_label.grid(row=0, column=0)        

        root.Cardbg = Cardbg = tk.PhotoImage(file='card.png')
        self.card = tk.Canvas(self.center_frame,
                              bg=default_bg,
                              highlightthickness=0,
                              width=272, height=330)
        self.card.create_image(136, 0, image=Cardbg, anchor=tk.N)
        self.card.create_text(20, -10, text='A', font=(font, '72', 'bold'), anchor=tk.NW, justify=tk.CENTER)
        self.card.create_text(200, 280, text='B', font=(font, '72', 'bold'), anchor=tk.NW, justify=tk.CENTER)
        self.card.grid(row=1, padx=2, pady=2)        
        
        self.history_button = tk.Button(self.center_frame,
                                        bg=default_bg,
                                        text='History and stats',
                                        font=(font, '18'),
                                        padx=0, pady=0,
                                        width=20, height=0)
        self.history_button.grid(row=2, column=0, padx=0, pady=5,)        
        
        # frame to hold other buttons 
        self.right_frame = tk.Frame(self.content_frame,
                                       bg="blue",
                                       padx=2, pady=2)
        self.right_frame.grid(row=1, column=2)        
        
        self.two_to_ten_button = tk.Button(self.right_frame,
                                       bg=default_bg,
                                       text='2-10 x1.44',
                                       font=(font, '18', "bold"),
                                       padx=0, pady=0,
                                       width=10, height=0,
                                       command=lambda: self.inputcheck(1.44))
        self.two_to_ten_button.grid(row=0, padx=0, pady=0)          
        
        self.RBG_button_frame = tk.Frame(self.right_frame,
                                         bg="pink",
                                         padx=2, pady=2)
        self.RBG_button_frame.grid(row=1, column=0)     
        
        self.R_button = tk.Button(self.RBG_button_frame,
                                       bg=default_bg,
                                       text='R x3',
                                       font=(font, '17', "bold"),
                                       padx=0, pady=0,
                                       width=0, height=0)
        self.R_button.grid(row=0, column=0, padx=0, pady=0)
        
        self.B_button = tk.Button(self.RBG_button_frame,
                                       bg=default_bg,
                                       text='B x3',
                                       font=(font, '17', "bold"),
                                       padx=0, pady=0,
                                       width=0, height=0)
        self.B_button.grid(row=0, column=1, padx=0, pady=0)
        
        self.G_button = tk.Button(self.RBG_button_frame,
                                       bg=default_bg,
                                       text='G x3',
                                       font=(font, '17', "bold"),
                                       padx=0, pady=0,
                                       width=0, height=0)
        self.G_button.grid(row=0, column=2, padx=2, pady=0)
        
        self.JQK_button = tk.Button(self.right_frame,
                                       bg=default_bg,
                                       text='J, Q, K',
                                       font=(font, '18', "bold"),
                                       padx=0, pady=0,
                                       width=10, height=0)
        self.JQK_button.grid(row=3, padx=0, pady=0)
        
        self.ak_and_a_button_frame = tk.Frame(self.right_frame,
                                         bg="orange",
                                         padx=2, pady=2)
        self.ak_and_a_button_frame.grid(row=4, column=0)
        
        self.AK_button = tk.Button(self.ak_and_a_button_frame,
                                       bg=default_bg,
                                       text='A, K',
                                       font=(font, '18', "bold"),
                                       padx=0, pady=0,
                                       width=4, height=0)
        self.AK_button.grid(row=0, column=0, padx=2, pady=0)
        
        self.A_button = tk.Button(self.ak_and_a_button_frame,
                                       bg=default_bg,
                                       text='A',
                                       font=(font, '18', "bold"),
                                       padx=0, pady=0,
                                       width=4, height=0)
        self.A_button.grid(row=0, column=1, padx=2, pady=0)
        
        self.Joker_button = tk.Button(self.right_frame,
                                       bg=default_bg,
                                       text='JOKER',
                                       font=(font, '18', "bold"),
                                       padx=0, pady=0,
                                       width=10, height=0)
        self.Joker_button.grid(row=5, padx=0, pady=0)        
        
        
        # Drag window if button down on title bar
        self.title_bar_drag_button.bind('<Button-1>', self.Main_pos)
        
        self.minimise_button.bind("<Enter>", self.minimise_on_enter)
        self.minimise_button.bind("<Leave>", self.minimise_on_leave)        
        
        self.close_button.bind("<Enter>", self.close_on_enter)
        self.close_button.bind("<Leave>", self.close_on_leave)        

        # Show window when icon poressed in taskbar
        self.Mainframe.bind("<Map>", self.Mapped) 
        
    # Make window moveable
    def Main_pos(self, partner):
        windowx, windowy = root.winfo_rootx(), root.winfo_rooty()
        pointerx, pointery = root.winfo_pointerx(), root.winfo_pointery()
        newx, newy = (pointerx-windowx), (pointery-windowy)

        def move_window(self):
            newpointx, newpointy = root.winfo_pointerx(), root.winfo_pointery()
            root.geometry('{}x{}+{}+{}'.format(wwidth,wheight,newpointx-newx,
                                               newpointy-newy))
        self.title_bar_drag_button.bind('<B1-Motion>', move_window)

    def minimise(self):
        root.update_idletasks()
        root.overrideredirect(False)
        # root.state('withdrawn')
        root.state('iconic')

    def Mapped(self, parent):
        root.update_idletasks()
        root.overrideredirect(True)
        root.state('normal')
        
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
    
    def inputcheck(self, multiplier):
        valid_characters='1234567890.'
        inputvalue=self.entry_box.get()
        print(inputvalue)
        print(coins)
        if inputvalue=='':
            self.info_label.configure(text="Enter an amount!")
            self.buttons_on(self)
        else:
            if all(char in valid_characters for char in inputvalue):
                if '.'in inputvalue:
                    self.info_label.configure(text="No decimals!")
                    self.buttons_on(self)
                else:
                    inputvalue = int(inputvalue)
                    if inputvalue > coins:
                        self.info_label.configure(text="Lack of funds!")
                        self.buttons_on(self)
                    elif inputvalue < 100:
                        self.info_label.configure(text="Minimum bet is 100!")
                        self.buttons_on(self)
                    else:
                        self.draw_card(self)
            else:
                self.info_label.configure(text="Whole numbers only!")
                self.buttons_on(self)
        
    def draw_card(self, partner):
        def countdown():
            self.info_label.configure(text="Drawing card...")
            time.sleep(1)
            self.info_label.configure(text=picked_card)
            self.buttons_on(self)
        global counter
        counter+=1
        self.buttons_off(self, full=False)
        if random.randint(1, 40)==40:
            picked_card='Joker'
        else:
            card_suit=random.choice(suits_list)
            card_numeral=random.choice(cards_list)
            picked_card=str(card_numeral)+' '+str(card_suit)
        print(picked_card)
        countdown_thread = threading.Thread(target=countdown)
        countdown_thread.start()
    
    def buttons_off(self, partner, full):
        self.higher_button['state']=tk.DISABLED
        self.lower_button['state']=tk.DISABLED
        self.two_to_ten_button['state']=tk.DISABLED
        self.R_button['state']=tk.DISABLED
        self.B_button['state']=tk.DISABLED
        self.G_button['state']=tk.DISABLED
        self.JQK_button['state']=tk.DISABLED
        self.AK_button['state']=tk.DISABLED
        self.A_button['state']=tk.DISABLED
        self.Joker_button['state']=tk.DISABLED
        if full==True:   
            self.leaderboard_button['state']=tk.DISABLED
            self.help_button['state']=tk.DISABLED
            self.withdraw_button['state']=tk.DISABLED
            self.history_button['state']=tk.DISABLED
    
    def buttons_on(self, partner):
        self.higher_button['state']=tk.NORMAL
        self.lower_button['state']=tk.NORMAL
        self.two_to_ten_button['state']=tk.NORMAL
        self.R_button['state']=tk.NORMAL
        self.B_button['state']=tk.NORMAL
        self.G_button['state']=tk.NORMAL
        self.JQK_button['state']=tk.NORMAL
        self.AK_button['state']=tk.NORMAL
        self.A_button['state']=tk.NORMAL
        self.Joker_button['state']=tk.NORMAL
        self.leaderboard_button['state']=tk.NORMAL
        self.help_button['state']=tk.NORMAL
        self.withdraw_button['state']=tk.NORMAL
        self.history_button['state']=tk.NORMAL
        
if __name__ == "__main__":
    root = tk.Tk()
    root.title('main')
    root.overrideredirect(True)  # turns off title bar, geometry
    screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
    wwidth,wheight = 900, 500
    root.geometry('{}x{}+{}+{}'.format(wwidth,wheight,int(screen_width/2-wwidth/2),
                                      int(screen_height/2-wheight/2)))    
    root.attributes('-alpha', 0.99)
    App = MainApp(root)
    root.mainloop()

# PLAN AND SAY WHAT YOUR DOING

#total balance, bet amount and help and history buttons all on left frame. or maybe middle frame for history. bet button instantly bets or toggle time
#say loss or win on center frame
# cards partially drawn using canvas
#

#def countdown(count):
    ## change text in label        
    #label['text'] = count

    #if count > 0:
        ## call countdown again after 1000ms (1s)
        #root.after(1000, countdown, count-1)

#label = tk.Label(root)
#label.place(x=35, y=15)

## call countdown first time    
#countdown(5)
## root.after(0, countdown, 5)
