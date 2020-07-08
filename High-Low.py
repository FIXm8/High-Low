# coding=UTF-8
# version alpha0.1
import tkinter as tk
from functools import partial

class MainApp:
    def __init__(self, parent):
        default_bg='White'
        font = 'Bahnschrift Light SemiCondensed'
        
        self.Mainframe = tk.Frame(bg=default_bg,
                                  padx=0, pady=0)
        self.Mainframe.grid()
        
        # Title bar drag button
        self.title_bar_drag_button = tk.Button(self.Mainframe,
                                               text='Hi-Low game version alpha0.1',
                                               font=(font, '8'),
                                               bg="dark grey",
                                               fg="white",
                                               anchor=tk.W,
                                               relief=tk.SUNKEN,
                                               activebackground="dark grey",
                                               activeforeground="white",
                                               borderwidth=0,
                                               height=0, width=56,
                                               padx=3, pady=0)
        self.title_bar_drag_button.grid(row=0, column=0, sticky=tk.W)

        # Close button
        self.close_button = tk.Button(self.Mainframe,
                                      text="X",
                                      font=(font, '8', 'bold'),
                                      justify=tk.LEFT,
                                      bg="black",
                                      fg="white",
                                      activebackground="Red",
                                      activeforeground="white",
                                      borderwidth=0,
                                      height=0, width=3,
                                      padx=0, pady=0,
                                      command=root.destroy)
        self.close_button.grid(row=0, column=2)

        # Minimise button
        self.minimise_button = tk.Button(self.Mainframe,
                                         text="—",
                                         font=(font, '8', 'bold'),
                                         justify=tk.LEFT,
                                         bg="black",
                                         fg="white",
                                         activebackground="dark grey",
                                         activeforeground="white",
                                         borderwidth=0,
                                         height=0, width=3,
                                         padx=0, pady=0,
                                         command=self.minimise)
        self.minimise_button.grid(row=0, column=1)

        # Content frame holding content
        self.content_frame = tk.Frame(self.Mainframe,
                                      bg=default_bg,
                                      padx=10, pady=10)
        self.content_frame.grid(row=1)
        
        # frame to hold higher or lower buttons
        self.left_frame = tk.Frame(self.content_frame,
                                   bg=default_bg,
                                   padx=10, pady=10)
        self.left_frame.grid(column=0)
        
        # frame to hold cards
        self.center_frame = tk.Frame(self.content_frame,
                                       bg=default_bg,
                                       padx=10, pady=10)
        self.center_frame.grid(column=1)
        
        # frame to hold other buttons 
        self.right_frame = tk.Frame(self.content_frame,
                                       bg=default_bg,
                                       padx=10, pady=10)
        self.right_frame.grid(column=2)        
        
        
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
            root.geometry("334x130" + '+{}+{}'.format(newpointx-newx,
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
    root.geometry("334x130" + '+{}+{}'.format(int(screen_width/2-171),
                                              int(screen_height/2-141)))    
    root.attributes('-alpha', 0.99)
    App = MainApp(root)
    root.mainloop()
    