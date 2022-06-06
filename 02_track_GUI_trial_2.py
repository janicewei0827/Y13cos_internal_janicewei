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

        #show user input boxes(row 1)
        background_color1 = "#E9967A"
        self.input_boxes_frame = Frame(self.track_frame, bg="#E9967A",
                                       borderwidth=2, relief="solid")
        self.input_boxes_frame.grid(row=1, pady=10, padx=10,ipady=10)

        #heading (row 0)
        self.heading_label = Label(self.input_boxes_frame,
                                   text="Enter the information of your jobs...",
                                   bg=background_color1,
                                   font="Arial 21 italic",width=29,
                                   padx=10, pady=10)
        self.heading_label.grid(row=0, columnspan=2)

        text_color="#303030"
        #job number (row 1)
        self.job_num_label = Label(self.input_boxes_frame, text="Job Number",
                                   font="Arial 16", bg=background_color1, fg=text_color
                                   , wrap=160, justify=LEFT)
        self.job_num_label.grid(row=1, column=0, sticky='w', padx=20, pady=5)
        self.job_num_entry = Entry(self.input_boxes_frame, width=15,
                                   font="Arial 13 bold")
        self.job_num_entry.grid(row=1, column=1, sticky='e', padx=20, pady=5)

        #customer name (row 2)
        self.customer_name_label = Label(self.input_boxes_frame, text="Customer Name",
                                         font="Arial 16", bg=background_color1, fg=text_color,
                                         wrap=160, justify=LEFT)
        self.customer_name_label.grid(row=2, column=0, sticky='w', padx=20, pady=5)
        self.customer_name_entry = Entry(self.input_boxes_frame, width=15,
                                         font="Arial 13 bold")
        self.customer_name_entry.grid(row=2, column=1, sticky='e', padx=20, pady=5)

        #distance travelled (row 3)
        self.distance_travelled_label = Label(self.input_boxes_frame, text="Distance Travelled",
                                              font="Arial 16", bg=background_color1, fg=text_color,
                                              wrap=160, justify=LEFT)
        self.distance_travelled_label.grid(row=3, column=0, sticky='w', padx=20, pady=5)
        self.distance_travelled_entry = Entry(self.input_boxes_frame, width=15,
                                              font="Arial 13 bold")
        self.distance_travelled_entry.grid(row=3, column=1, sticky='e', padx=20, pady=5)

        #service type check box (row 4)
        var0 = IntVar()
        var1 = IntVar()
        self.var0_check = Checkbutton(self.input_boxes_frame, text="Virus Protection was required",
                                      variable=var0, font="Arial 16", wrap=120, justify=LEFT,
                                      bg=background_color1, fg=text_color)
        self.var0_check.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        self.var1_check = Checkbutton(self.input_boxes_frame, text="WOF and tune was required",
                                      variable=var1, font="Arial 16", wrap=120, justify=LEFT,
                                      bg=background_color1, fg=text_color)
        self.var1_check.grid(row=4, column=1, padx=20, pady=5, sticky="e")

        #minutes spent on virus protection (row 5)
        self.mins_spent_label = Label(self.input_boxes_frame, text="Minutes Spent On Virus Protection ",
                                      font="Arial 16", bg=background_color1, fg=text_color,
                                      wrap=160, justify=LEFT)
        self.mins_spent_label.grid(row=5, column=0, sticky='w', padx=20, pady=5)
        self.mins_spent_entry = Entry(self.input_boxes_frame, width=15,
                                      font="Arial 13 bold")
        self.mins_spent_entry.grid(row=5, column=1, sticky='e', padx=20, pady=5)




        #Enter jobs button (row 2)
        self.enter_button_frame = Frame(self.track_frame)
        self.enter_button_frame.grid(row=2, pady=10)

        self.enter_button = Button(self.enter_button_frame, text="Enter Job",
                                   font="Verdana 22 bold", width=10,
                                   highlightbackground="#A52A2A",
                                   padx=10, pady=10, fg="white")
        self.enter_button.grid(row=0)

        #Help & Show All Jobs (row=3)
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
