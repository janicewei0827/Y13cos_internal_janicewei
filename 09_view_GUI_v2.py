from tkinter import *
import tkinter as tk
from functools import partial  #to prevent unwanted windows
import random

class Track:
    def __init__(self, parent):
        background_color = "#a81c07"

        #In actual program this is blank and is populated with user inputs and calculations
        self.job_numbers = [5, 4, 3, 2, 1]
        self.names = ["eeeee", "ddddd", "ccccc", "bbbbb", "aaaaa"]
        self.charges = [50, 40, 30, 20, 10]
        self.track_frame = Frame(padx=10, pady=10,
                                 bg=background_color)
        self.track_frame.grid()

        #Suzy's service Business Logo (row 0)
        logo = PhotoImage(file="logo.png")
        self.service_label = Label(self.track_frame, image=logo,
                                   bg=background_color, padx=10, pady=10)
        self.service_label.photo = logo
        self.service_label.grid(row=0)

        #view button
        self.view_help_frame = Frame(self.track_frame)
        self.view_help_frame.grid(row=1, pady=10)

        self.view_button = Button(self.view_help_frame, font="Verdana 15 bold",
                                  text="Show All Jobs", width=15, height=2,
                                  highlightbackground="#EC5800", fg="#A52A2A",
                                  command=lambda: self.view(self.job_numbers, self.names, self.charges))
        self.view_button.grid(row=0)
        if len(self.job_numbers) == 0:
            self.view_button.config(state=DISABLED)

    def view(self,job_numbers, names, charges):
        print("You asked for viewing your jobs.")
        get_info = View(self,job_numbers, names, charges)


class View:
    def __init__(self, partner,job_numbers, names, charges):
        background_color = "#a81c07"
        text_color="#303030"
        text_color1="#6f0000"

        #disable view button
        partner.view_button.config(state=DISABLED)

        #Sets up child window (ie:view box)
        self.view_box = Toplevel()

        #if user click press at the top, closes help and releases help button
        self.view_box.protocol('WM_DELETE_WINDOW', partial(self.close_view, partner))

        #set up GUI Frame
        self.view_frame = Frame(self.view_box, bg=background_color)
        self.view_frame.grid()

        #Suzy's service Business Logo (row 0)
        logo = PhotoImage(file="logo.png")
        self.service_label = Label(self.view_frame, image=logo,
                                   bg=background_color, padx=10, pady=10)
        self.service_label.photo = logo
        self.service_label.grid(row=0)

        #Show headings & provide an area which will show contents later...(row 1)
        #show user box for displaying details(row 1)
        background_color1= "#E9967A"
        self.details_frame = Frame(self.view_frame, bg=background_color1,
                                   borderwidth=2,relief="solid")
        self.details_frame.grid(row=1, padx=10,ipady=10)

        #display job information for the user
        #only display the most recent one in version 1
        self.current_index = 0

        #heading (row 0)
        self.heading_label = Label(self.details_frame,
                                   text="Information of your jobs...",
                                   bg=background_color1,
                                   font="Arial 21 italic bold",width=29,
                                   padx=10, pady=10)
        self.heading_label.grid(row=0, columnspan=2)

        #display job number(row 1)
        self.job_number_label = Label(self.details_frame, text="Job Number:",
                                      font="Arial 18", bg=background_color1, fg=text_color,
                                      justify=LEFT)
        self.job_number_label.grid(row=1, column=0, sticky='e')
        self.job_number_value_label = Label(self.details_frame, text=job_numbers[self.current_index],
                                            font="Arial 18", bg=background_color1, fg=text_color1,
                                             justify=LEFT)
        self.job_number_value_label.grid(row=1, column=1, sticky='w', padx=20)

        #display customer name (row 2)
        self.name_label = Label(self.details_frame, text="Customer Name:",
                                font="Arial 18", bg=background_color1, fg=text_color,
                                justify=LEFT)
        self.name_label.grid(row=2, column=0, sticky='e')
        self.name_value_label = Label(self.details_frame, text=names[self.current_index],
                                      font="Arial 18", bg=background_color1, fg=text_color1,
                                      justify=LEFT, wrap=150)
        self.name_value_label.grid(row=2, column=1, sticky='w', padx=20)

        #display job charges (row 3)
        self.charge_label = Label(self.details_frame, text="Job Charge:",
                                  font="Arial 18", bg=background_color1, fg=text_color,
                                   justify=LEFT)
        self.charge_label.grid(row=3, column=0, sticky='e')
        self.charge_value_label = Label(self.details_frame, text=charges[self.current_index],
                                        font="Arial 18", bg=background_color1, fg=text_color1,
                                         justify=LEFT)
        self.charge_value_label.grid(row=3, column=1, sticky='w', padx=20)

        #Dimiss Button (row 2)
        self.dismiss_button_frame = Frame(self.view_frame)
        self.dismiss_button_frame.grid(row=2, pady=10)

        self.dismiss_button = Button(self.dismiss_button_frame, text="Dismiss",
                                     font="Verdana 22 bold", width=10,
                                     highlightbackground="#A52A2A",
                                     padx=10, pady=10, fg="white",
                                     command=partial(self.close_view,partner))
        self.dismiss_button.grid(row=0)

        #Previous/Next buttons (row=3)
        self.prev_next_frame = Frame(self.view_frame)
        self.prev_next_frame.grid(row=3, pady=10)

        self.prev_button = Button(self.prev_next_frame, font="Verdana 15 bold",
                                  text="Previous", width=15, height=2,
                                  highlightbackground="#EC5800", fg="#A52A2A",
                                  command=lambda: self.show_prev_next('prev',job_numbers, names, charges))
        self.prev_button.grid(row=0, column=0)

        self.next_button = Button(self.prev_next_frame, font="Verdana 15 bold",
                                  text="Next", width=15, height=2,
                                  highlightbackground="#EC5800", fg="#A52A2A",
                                  command=lambda: self.show_prev_next('next',job_numbers, names, charges))
        self.next_button.grid(row=0, column=1)

    def show_prev_next(self, seq, job_numbers, names, charges):
        if seq == "prev":
            self.current_index -= 1

            #make the current_index always within range 0~len(list)
            if self.current_index == -1:
                self.current_index = len(job_numbers)-1

            #change the job information output in GUI
            self.job_number_value_label.configure(text=job_numbers[self.current_index])
            self.name_value_label.configure(text=names[self.current_index])
            self.charge_value_label.configure(text=charges[self.current_index])
        elif seq == "next":
            self.current_index += 1

            #make the current_index always within range 0~len(list)
            if self.current_index == len(job_numbers):
                self.current_index = 0

            #change the job information output in GUI
            self.job_number_value_label.configure(text=job_numbers[self.current_index])
            self.name_value_label.configure(text=names[self.current_index])
            self.charge_value_label.configure(text=charges[self.current_index])


    def close_view(self, partner):
        #put view button back to normal
        partner.view_button.config(state=NORMAL)
        self.view_box.destroy()



#main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Suzy's Professional Mobile Service")
    something = Track(root)
    root.mainloop()
