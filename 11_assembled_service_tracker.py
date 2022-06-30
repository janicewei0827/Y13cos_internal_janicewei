from tkinter import *
import tkinter as tk
from functools import partial  #to prevent unwanted windows
import random
import math

class Track:
    def __init__(self, parent):
        background_color = "#a81c07"

        self.job_numbers=[]
        self.names=[]
        self.charges=[]

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
                                   font="Arial 21 italic bold",width=29,
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

        #customer name (row 3)
        self.customer_name_label = Label(self.input_boxes_frame, text="Customer Name",
                                         font="Arial 16", bg=background_color1, fg=text_color,
                                         wrap=160, justify=LEFT)
        self.customer_name_label.grid(row=3, column=0, sticky='w', padx=20)
        self.customer_name_entry = Entry(self.input_boxes_frame, width=15,
                                         font="Arial 13 bold")
        self.customer_name_entry.grid(row=3, column=1, sticky='e', padx=20)

        #name error label (row=4)
        self.name_error_label = Label(self.input_boxes_frame, fg="maroon",
                                      text="", font="Arial 12 bold", wrap=275,
                                      justify=LEFT, bg=background_color1)
        self.name_error_label.grid(row=4, columnspan=2, sticky="e", padx=20)

        #distance travelled (row 5)
        self.distance_travelled_label = Label(self.input_boxes_frame, text="Distance Travelled (km)",
                                              font="Arial 16", bg=background_color1, fg=text_color,
                                              wrap=160, justify=LEFT)
        self.distance_travelled_label.grid(row=5, column=0, sticky='w', padx=20)
        self.distance_travelled_entry = Entry(self.input_boxes_frame, width=15,
                                              font="Arial 13 bold")
        self.distance_travelled_entry.grid(row=5, column=1, sticky='e', padx=20)

        #distance error label (row=6)
        self.distance_error_label = Label(self.input_boxes_frame, fg="maroon",
                                          text="", font="Arial 12 bold", wrap=275,
                                          justify=LEFT, bg=background_color1)
        self.distance_error_label.grid(row=6, columnspan=2, sticky="e", padx=20)

        #service type check box (row 7)
        self.var0 = IntVar()
        self.var1 = IntVar()
        self.var0_check = Checkbutton(self.input_boxes_frame, text="Virus Protection was required",
                                      variable=self.var0, font="Arial 16", wrap=120, justify=LEFT,
                                      bg=background_color1, fg=text_color,
                                      command=self.check_service, onvalue=1, offvalue=0)
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

        #minutes spent on virus protection (row 9)
        #diabled at the start as user doesn't select the corresponding checkbox
        self.mins_spent_label = Label(self.input_boxes_frame, text="Minutes Spent On Virus Protection ",
                                      font="Arial 16", bg=background_color1, fg=disabled_color,
                                      wrap=160, justify=LEFT)
        self.mins_spent_label.grid(row=9, column=0, sticky='w', padx=20)
        self.mins_spent_entry = Entry(self.input_boxes_frame, width=15,
                                      font="Arial 13 bold")
        self.mins_spent_entry.grid(row=9, column=1, sticky='e', padx=20)
        self.mins_spent_entry.config(state=DISABLED, disabledbackground=disabled_color)

        #minutes spent error label (row=10)
        self.minutes_error_label = Label(self.input_boxes_frame, fg="maroon",
                                         text="", font="Arial 12 bold", wrap=275,
                                         justify=LEFT, bg=background_color1)
        self.minutes_error_label.grid(row=10, columnspan=2, sticky="e", padx=20)

        #Enter jobs button (row 2)
        self.enter_button_frame = Frame(self.track_frame)
        self.enter_button_frame.grid(row=2, pady=10)

        self.enter_button = Button(self.enter_button_frame, text="Enter Job",
                                   font="Verdana 22 bold", width=10,
                                   highlightbackground="#A52A2A",
                                   padx=10, pady=10, fg="white",
                                   command=lambda: self.input_checker())
        self.enter_button.grid(row=0)

        #Help & Show All Jobs (row=3)
        self.view_help_frame = Frame(self.track_frame)
        self.view_help_frame.grid(row=3, pady=10)

        self.help_button = Button(self.view_help_frame, font="Verdana 15 bold",
                                  text="Help", width=15, height=2,
                                  highlightbackground="#EC5800", fg="#A52A2A",
                                  command=lambda: self.help())
        self.help_button.grid(row=0, column=0)

        self.view_button = Button(self.view_help_frame, font="Verdana 15 bold",
                                  text="Show All Jobs", width=15, height=2,
                                  highlightbackground="#EC5800", fg="#A52A2A",
                                  command=lambda: self.view(self.job_numbers, self.names, self.charges))
        self.view_button.grid(row=0, column=1)

        #disable the view button when no information is entered/stored
        if len(self.job_numbers) == 0:
            self.view_button.config(state=DISABLED)

    def check_service(self):
        disabled_color="#999999"
        text_color="#303030"
        if self.var0.get() == 1:
            self.mins_spent_entry.configure(state=NORMAL)
            self.mins_spent_label.configure(fg=text_color)
        else:
            self.mins_spent_entry.configure(state=DISABLED, disabledbackground=disabled_color)
            self.mins_spent_label.configure(fg=disabled_color)

    def input_checker(self):
        job_number = self.job_num_entry.get()
        customer_name = self.customer_name_entry.get()
        distance_travelled = self.distance_travelled_entry.get()
        minutes_spent = self.mins_spent_entry.get()

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

        #check customer name
        if len(customer_name)==0 or customer_name.isspace():
            has_error2="yes"
            answer="Please enter a valid name!"
        else:
            has_error2="no"
            #display error messages
        if has_error2 == "yes":
            self.customer_name_entry.configure(bg=error)
            self.name_error_label.configure(text=answer)
        else:
            self.customer_name_entry.configure(bg="white")
            self.name_error_label.configure(text="")

        #check distance travelled
        try:
            distance_travelled=float(distance_travelled)
            if 0<=distance_travelled<=800:
                has_error3="no"
            elif distance_travelled<0:
                answer="Please enter a valid number for distance!"
                has_error3="yes"
            else:
                answer="Too far away! That seems impossible!"
                has_error3="yes"
        except ValueError:
            has_error3="yes"
            answer="Please enter a valid number for distance!"
            #display error messages
        if has_error3 == "yes":
            self.distance_travelled_entry.configure(bg=error)
            self.distance_error_label.configure(text=answer)
        else:
            self.distance_travelled_entry.configure(bg="white")
            self.distance_error_label.configure(text="")

        #check service type
        if self.var0.get() == 0 and self.var1.get() == 0:
            answer="You must select one of the services!"
            has_error4="yes"
        else:
            has_error4="no"
            #display error message
        if has_error4 == "yes":
            self.service_error_label.configure(text=answer)
        else:
            self.service_error_label.configure(text="")

        #check minutes spent
        if self.var0.get() == 1:
            try:
                minutes_spent=int(minutes_spent)
                if 0<minutes_spent:
                    has_error5="no"
                else:
                    has_error5="yes"
                    answer="Please enter a valid whole number!"
            except ValueError:
                has_error5="yes"
                answer="Please enter a valid whole number!"
        else:
            has_error5="no"
            #display error messages
        if has_error5 == "yes":
            self.mins_spent_entry.configure(bg=error)
            self.minutes_error_label.configure(text=answer)
        else:
            self.mins_spent_entry.configure(bg="white")
            self.minutes_error_label.configure(text="")

        #clear entry boxes if there are no errors
        if has_error1=="no" and has_error2=="no" and has_error3=="no" and has_error4=="no" and has_error5=="no":
            self.job_numbers.insert(0, job_number)
            self.names.insert(0, customer_name)
            self.view_button.config(state=NORMAL)
            self.calc_charges(distance_travelled, minutes_spent, self.var0, self.var1)
            self.clear_entry()

    def calc_charges(self, distance, minutes, var0, var1):
        #rounding distance
        if distance % 0.5 == 0:
            distance_travelled=math.ceil(distance)
        else:
            distance_travelled=round(distance)
        #calculate charge1
        if distance_travelled<=5:
            charge1=10
        else:
            charge1=(distance_travelled - 5) * 0.5 + 10

        #calculate charge2 (virus_protection service)
        if var0==1:
            charge2=0.8 * minutes
        else:
            charge2=0

        #claculate charge3 (wof and tune service)
        if var1==1:
            charge3=100
        else:
            charge3=0

        #calculate final job charge
        job_charge = charge1 + charge2 + charge3

        #store job charge
        self.charges.insert(0, job_charge)

    def view(self, job_numbers, names, charges):
        print("You asked for viewing your jobs.")
        get_info = View(self, job_numbers, names, charges)

    def help(self):
        get_help = Help(self)

    def clear_entry(self):
        self.job_num_entry.delete(first=0,last=END)
        self.customer_name_entry.delete(first=0,last=END)
        self.distance_travelled_entry.delete(first=0,last=END)
        self.mins_spent_entry.delete(first=0,last=END)
        self.var0.set(0)
        self.var1.set(0)
        self.check_service()


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

class View:
    def __init__(self, partner, job_numbers, names, charges):
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
        self.job_number_value_label = Label(self.details_frame, text=job_numbers[ self.current_index],
                                            font="Arial 18", bg=background_color1, fg=text_color1,
                                             justify=LEFT)
        self.job_number_value_label.grid(row=1, column=1, sticky='w', padx=20)

        #display customer name (row 2)
        self.name_label = Label(self.details_frame, text="Customer Name:",
                                font="Arial 18", bg=background_color1, fg=text_color,
                                justify=LEFT)
        self.name_label.grid(row=2, column=0, sticky='e')
        self.name_value_label = Label(self.details_frame, text=names[ self.current_index],
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
