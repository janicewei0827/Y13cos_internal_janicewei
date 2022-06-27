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

        #help button
        self.view_help_frame = Frame(self.track_frame)
        self.view_help_frame.grid(row=1, pady=10)

        self.help_button = Button(self.view_help_frame, font="Verdana 15 bold",
                                  text="Help", width=15, height=2,
                                  highlightbackground="#EC5800", fg="#A52A2A",
                                  command=lambda: self.help())
        self.help_button.grid(row=0)

    def help(self):
        print("You asked for help.")
        get_help = Help(self)



class Help:
    def __init__(self, partner):
        background_color = "#a81c07"

        #disable help button
        partner.help_button.config(state=DISABLED)

        #Sets up child window (ie:help box)
        self.help_box = Toplevel()

        #if user click press at the top, closes help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        #set up GUI Frame
        self.help_frame = Frame(self.help_box, bg=background_color)
        self.help_frame.grid()

        #Suzy's service Business Logo (row 0)
        logo = PhotoImage(file="logo.png")
        self.service_label = Label(self.help_frame, image=logo,
                                   bg=background_color, padx=10, pady=10)
        self.service_label.photo = logo
        self.service_label.grid(row=0)

        #show user box for displaying details(row 1)
        background_color1 = "#E9967A"
        self.details_frame = Frame(self.help_frame, bg=background_color1,
                                       borderwidth=2, relief="solid")
        self.details_frame.grid(row=1, padx=10)

        #heading (row 0)
        self.heading_label = Label(self.details_frame, justify=LEFT,
                                   text="Help / Instructions",
                                   bg=background_color1,
                                   font="Arial 21 italic bold",width=29,
                                   padx=10, pady=10)
        self.heading_label.grid(row=0, columnspan=2)

        #help text (label, row 1)
        self.help_text = Label(self.details_frame, text="""This program is aimed to help you keep track of your jobs whilst also calculating the job charge/cost.

You need to enter your:
  1. Job number
  2. Customer name
  3. Distance travelled to the customer
  4. Service types required by customers
  5. Minutes spent on virus protection (if it was required)

Once you finished entering your information, please press ‘Enter Job’ button, so that the program can collect your information.

Pressing the ‘Show All Jobs’ button allows you to view through all the jobs entered by pressing the ‘Next/Previous’ buttons. In this view, you will only see:
  1. Job number
  2. Customer number
  3. Job charge
""",
                               justify=LEFT, width=40, bg=background_color1,
                               wrap=320, font="Arial 15")
        self.help_text.grid(row=1)

        #Dismiss Button (row 2)
        self.dismiss_button_frame = Frame(self.help_frame)
        self.dismiss_button_frame.grid(row=2, pady=10)

        self.dismiss_button = Button(self.dismiss_button_frame, text="Dismiss",
                                     font="Verdana 22 bold", width=10,
                                     highlightbackground="#A52A2A",
                                     padx=10, pady=10, fg="white",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=0)



    def close_help(self, partner):
        #put help button back to normal
        partner.help_button.config(state=NORMAL)
        self.help_box.destroy()



#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Track(root)
    root.mainloop()
