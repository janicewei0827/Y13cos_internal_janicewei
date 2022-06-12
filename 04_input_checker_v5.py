from tkinter import *
import tkinter as tk
from functools import partial  #to prevent unwanted windows
import random

class Track:
    def __init__(self, parent):
        background_color = "#a81c07"
        self.track_frame = Frame(padx=10, pady=10, bg=background_color)
        self.track_frame.grid()

        background_color1 = "#E9967A"
        self.input_boxes_frame = Frame(self.track_frame, bg=background_color1,
                                       borderwidth=2, relief="solid")
        self.input_boxes_frame.grid(row=1, pady=10, padx=10,ipady=10)

        disabled_color="#999999"
        text_color="#303030"

        #service type check box (row 4)
        self.var0 = IntVar()
        self.var1 = IntVar()
        self.var0_check = Checkbutton(self.input_boxes_frame, text="Virus Protection was required",
                                      variable=self.var0, font="Arial 16", wrap=120, justify=LEFT,
                                      bg=background_color1, fg=text_color,
                                      command=self.check_service, onvalue=1, offvalue=0)
        self.var0_check.grid(row=4, column=0, padx=20, pady=5, sticky="w")
        self.var1_check = tk.Checkbutton(self.input_boxes_frame, text="WOF and tune was required",
                                         variable=self.var1, font="Arial 16", wrap=120, justify=LEFT,
                                         bg=background_color1, fg=text_color,
                                         onvalue=1, offvalue=0)
        self.var1_check.grid(row=4, column=1, padx=20, pady=5, sticky="e")

        #minutes spent on virus protection (row 5)
        #diabled at the start as user doesn't select the corresponding checkbox
        self.mins_spent_label = Label(self.input_boxes_frame, text="Minutes Spent On Virus Protection ",
                                      font="Arial 16", bg=background_color1, fg=disabled_color,
                                      wrap=160, justify=LEFT)
        self.mins_spent_label.grid(row=5, column=0, sticky='w', padx=20, pady=5)
        self.mins_spent_entry = Entry(self.input_boxes_frame, width=15,
                                      font="Arial 13 bold")
        self.mins_spent_entry.grid(row=5, column=1, sticky='e', padx=20, pady=5)
        self.mins_spent_entry.config(state=DISABLED, disabledbackground=disabled_color)

        #Enter jobs button (row 2)
        self.enter_button_frame = Frame(self.track_frame)
        self.enter_button_frame.grid(row=2, pady=10)

        self.enter_button = Button(self.enter_button_frame, text="Enter Job",
                                   font="Verdana 22 bold", width=10,
                                   highlightbackground="#A52A2A",
                                   padx=10, pady=10, fg="white",
                                   command=lambda: self.input_checker())
        self.enter_button.grid(row=0)



    def check_service(self):
        disabled_color="#999999"
        text_color="#303030"
        if self.var0.get() == 1:
            self.mins_spent_entry.configure(state=NORMAL)
            self.mins_spent_label.configure(fg=text_color)
        else:
            self.mins_spent_entry.configure(state=DISABLED, disabledbackground=disabled_color)
            self.mins_spent_label.configure(fg=disabled_color)

        #for testing purpose
        print(self.var0.get(), self.var1.get())

    def input_checker(self):
        if self.var0.get() == 0 and self.var1.get() == 0:
            print("You must select one of the services!")



#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Track(root)
    root.mainloop()
