# coding=UTF-8
# version alpha0.1
import tkinter as tk
from functools import partial

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
                                     height=0, width=93,
                                     padx=5, pady=10)
        self.title_label.grid(row=0)
        
        self.withdraw_button = tk.Button(self.topbar_frame,
                                     text="Withdraw",
                                     font="Arial 10 bold",
                                     justify=tk.LEFT,
                                     bg="grey10",
                                     fg="white",
                                     bd=0,
                                     padx=10, pady=9)
        self.withdraw_button.grid(row=0, column=1)
        
        self.help_button = tk.Button(self.topbar_frame,
                                     text="Help",
                                     font="Arial 10 bold",
                                     justify=tk.LEFT,
                                     bg="grey10",
                                     fg="white",
                                     bd=0,
                                     padx=10, pady=9)
        self.help_button.grid(row=0, column=2) 
        
        
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
                                       padx=6, pady=0)
        self.higher_button.grid(row=1, padx=0, pady=1)
        
        self.lower_button = tk.Button(self.left_frame,
                                       bg=default_bg,
                                       text='▼',
                                       font=(font, '28'),
                                       padx=6, pady=0)
        self.lower_button.grid(row=2, padx=0, pady=1)        
        
        self.lower_label = tk.Label(self.left_frame,
                                    bg=default_bg,
                                    text='X1',
                                    font=(font, '14'),
                                    padx=2, pady=2)
        self.lower_label.grid(row=3)        
        
        
        # frame to hold cards
        self.center_frame = tk.Frame(self.content_frame,
                                     bg=default_bg,
                                     padx=2, pady=2)
        self.center_frame.grid(row=1, column=1)
        
        root.Cardbg = Cardbg = tk.PhotoImage(file='card.png')
        self.card = tk.Canvas(self.center_frame,
                              bg=default_bg,
                              highlightthickness=0,
                              width=272, height=397)
        self.card.create_image(136, 0, image=Cardbg, anchor=tk.N)
        self.card.create_text(20, -10, text='A', font=(font, '72', 'bold'), anchor=tk.NW, justify=tk.CENTER)
        self.card.create_text(200, 280, text='B', font=(font, '72', 'bold'), anchor=tk.NW, justify=tk.CENTER)
        self.card.grid(row=0, padx=2, pady=2)        
        
        
        # frame to hold other buttons 
        self.right_frame = tk.Frame(self.content_frame,
                                       bg="blue",
                                       padx=2, pady=2)
        self.right_frame.grid(row=1, column=2)        
        
        self.two_to_ten_button = tk.Button(self.right_frame,
                                       bg=default_bg,
                                       text='2-10',
                                       font=(font, '18', "bold"),
                                       padx=0, pady=0,
                                       width=10, height=0)
        self.two_to_ten_button.grid(row=0, padx=0, pady=0)          
        
        self.RBG_button_frame = tk.Frame(self.right_frame,
                                         bg="pink",
                                         padx=2, pady=2)
        self.RBG_button_frame.grid(row=1, column=0)     
        
        self.R_button = tk.Button(self.RBG_button_frame,
                                       bg=default_bg,
                                       text='R',
                                       font=(font, '18', "bold"),
                                       padx=0, pady=0,
                                       width=0, height=0)
        self.R_button.grid(row=0, column=0, padx=2, pady=0)
        
        self.R_button = tk.Button(self.RBG_button_frame,
                                       bg=default_bg,
                                       text='B',
                                       font=(font, '18', "bold"),
                                       padx=0, pady=0,
                                       width=0, height=0)
        self.R_button.grid(row=0, column=1, padx=2, pady=0)
        
        self.G_button = tk.Button(self.RBG_button_frame,
                                       bg=default_bg,
                                       text='G',
                                       font=(font, '18', "bold"),
                                       padx=0, pady=0,
                                       width=0, height=0)
        self.G_button.grid(row=0, column=2, padx=2, pady=0)
        
        self.JQK_button = tk.Button(self.right_frame,
                                       bg=default_bg,
                                       text='JQK',
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
                                       text='AK',
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
