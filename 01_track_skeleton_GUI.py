from tkinter import *
import tkinter as tk
from functools import partial  #to prevent unwanted windows
import random

class Track: 
    def __init__(self, parent):
        background_color = "#a81c07"

        self.track_frame = Frame(padx=10, pady=10,
                                 bg=background_color)
        self.track_frame.grid()

        #Suzy's service Business Logo (row 0)
        logo = PhotoImage(file="logo.png")
        self.service_label = Label(self.track_frame, image=logo,
                                   bg=background_color, padx=10, pady=10)
        self.service_label.photo = logo
        self.service_label.grid(row=0)

        #Show headings & provide an area which will show contents later...(row 1)
        self.heading_label = Label(self.track_frame,
                                   text="""Enter the information of your jobs...
                                   
                                   
                                   
                                   
                                   
                                   
                                   """,
                                   font="Arial 21 italic", wrap=350,
                                   justify=LEFT, bg="#E9967A",
                                   borderwidth=2, relief="solid",
                                   padx=10, pady=10)
        self.heading_label.grid(row=1)

        #Main button (Enter jobs button) (row 2)
        self.enter_button_frame = Frame(self.track_frame)
        self.enter_button_frame.grid(row=2, pady=10)

        self.enter_button = Button(self.enter_button_frame, text="Enter Job",
                                   font="Verdana 22 bold", width=10,
                                   highlightbackground="#A52A2A",
                                   padx=10, pady=10, fg="white")
        self.enter_button.grid(row=0)

        #other buttons (Help & Show All Jobs) (row=3)
        self.view_help_frame = Frame(self.track_frame)
        self.view_help_frame.grid(row=3, pady=10)

        self.help_button = Button(self.view_help_frame, font="Verdana 15 bold",
                                  text="Help", width=15, height=2,
                                  highlightbackground="#EC5800", fg="#A52A2A")
        self.help_button.grid(row=0, column=0)

        self.view_button = Button(self.view_help_frame, font="Verdana 15 bold",
                                  text="Show All Jobs", width=15, height=2,
                                  highlightbackground="#EC5800", fg="#A52A2A")
        self.view_button.grid(row=0, column=1)




#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Track(root)
    root.mainloop()
