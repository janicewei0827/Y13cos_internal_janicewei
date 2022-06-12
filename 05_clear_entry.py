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
        self.input_boxes_frame.grid(row=1, padx=10)

        #heading (row 0)
        self.heading_label = Label(self.input_boxes_frame,
                                   text="Enter the information of your jobs...",
                                   bg=background_color1,
                                   font="Arial 21 italic",width=29,
                                   padx=10, pady=10)
        self.heading_label.grid(row=0, columnspan=2)

        disabled_color="#999999"
        text_color="#303030"
        #job number (row 1)
        self.job_num_label = Label(self.input_boxes_frame, text="Job Number",
                                   font="Arial 16", bg=background_color1, fg=text_color
                                   , wrap=160, justify=LEFT)
        self.job_num_label.grid(row=1, column=0, sticky='w', padx=20)
        self.job_num_entry = Entry(self.input_boxes_frame, width=15,
                                   font="Arial 13 bold")
        self.job_num_entry.grid(row=1, column=1, sticky='e', padx=20)

        #job num error label (row=2)
        self.job_num_error_label = Label(self.input_boxes_frame, fg="maroon",
                                         text="", font="Arial 12 bold", wrap=275,
                                         justify=LEFT, bg=background_color1)
        self.job_num_error_label.grid(row=2, columnspan=2, sticky="e", padx=20)

        #service type check box (row 7)
        self.var0 = IntVar()
        self.var1 = IntVar()
        self.var0_check = Checkbutton(self.input_boxes_frame, text="Virus Protection was required",
                                      variable=self.var0, font="Arial 16", wrap=120, justify=LEFT,
                                      bg=background_color1, fg=text_color, onvalue=1, offvalue=0)
        self.var0_check.grid(row=7, column=0, padx=20, sticky="w")
        self.var1_check = tk.Checkbutton(self.input_boxes_frame, text="WOF and tune was required",
                                         variable=self.var1, font="Arial 16", wrap=120, justify=LEFT,
                                         bg=background_color1, fg=text_color,
                                         onvalue=1, offvalue=0)
        self.var1_check.grid(row=7, column=1, padx=20, sticky="e")

        #service type error label (row=8)
        self.service_error_label = Label(self.input_boxes_frame, fg="maroon",
                                         text="", font="Arial 12 bold", wrap=275,
                                         justify=LEFT, bg=background_color1)
        self.service_error_label.grid(row=8, columnspan=2)

        #Enter jobs button (row 2)
        self.enter_button_frame = Frame(self.track_frame)
        self.enter_button_frame.grid(row=2, pady=10)

        self.enter_button = Button(self.enter_button_frame, text="Enter Job",
                                   font="Verdana 22 bold", width=10,
                                   highlightbackground="#A52A2A",
                                   padx=10, pady=10, fg="white",
                                   command=lambda: self.input_checker())
        self.enter_button.grid(row=0)

    def input_checker(self):
        job_number = self.job_num_entry.get()

        error = "#ffafaf" #pale pink background for when entry box has errors

        #check job number
        try:
            job_number = int(job_number)
            if 0<=job_number:
                has_error1="no"
            else:
                answer="Please enter a valid number!"
                has_error1="yes"
        except ValueError:
            answer="Please enter a valid number!"
            has_error1="yes"
            #display error message
        if has_error1 == "yes":
            self.job_num_entry.configure(bg=error)
            self.job_num_error_label.configure(text=answer)
        else:
            self.job_num_entry.configure(bg="white")
            self.job_num_error_label.configure(text="")

        #check service type
        if self.var0.get() == 0 and self.var1.get() == 0:
            answer="You must select one of the services!"
            has_error2="yes"
        else:
            has_error2="no"
            #display error message
        if has_error2 == "yes":
            self.service_error_label.configure(text=answer)
        else:
            self.service_error_label.configure(text="")

        #clear entry boxes & checkbuttons
        if has_error1=="no" and has_error2=="no":
            self.clear_entry()

    def clear_entry(self):
        self.job_num_entry.delete(first=0,last=END)
        self.var0.set(0)
        self.var1.set(0)





#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Track(root)
    root.mainloop()
