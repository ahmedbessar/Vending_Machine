import tkinter as ttk
import csv
import os
import input_variable as inp 
import report as rpt
import data_load as dl

"""This is a Vending Machine Program with four items selection and generate visualization reports of sales data"""

# Popup window for Report Selection
def popup():
    popup_window  = ttk.Tk()
    popup_window.title("Reports")
    popup_window.geometry("200x100")
    label = ttk.Label(popup_window, text="Reports Selection")
    label.pack()
    ttk.Button(popup_window, text = "Daily Sales Button", command=lambda: rpt.daily_sales() if os.path.exists(inp.database_file(inp.file_name)) else msg()).pack()
    ttk.Button(popup_window, text= "Product Sales Button", command=lambda: rpt.product_sales() if os.path.exists(inp.database_file(inp.file_name)) else msg()).pack()
    popup_window.mainloop()

# Error handing message when no data file is missing or not created
def msg():
    msg_window = ttk.Tk()
    msg_window.title("Error Message")
    msg_window.geometry("200x100")
    label = ttk.Label(msg_window, text="Error: no purchased made till date")
    label.pack()
    msg_window.mainloop()

# Popup main window
main_window = ttk.Tk()
main_window.title("Vending Machine")
main_window.geometry("800x400")
welcome_lbl = ttk.Label(main_window,text="Welcome to \n Vending Machine \n Program \n Today's Date : {}".format(inp.today_date),font="Verdana 14 bold")
welcome_lbl.pack()


# Message Frame
message_frame = ttk.Frame(main_window)
message_frame.pack(side=ttk.LEFT)
# Selection Frame
selection_frame = ttk.Frame(main_window)
selection_frame.pack(side=ttk.TOP)
# Payment button frame
payment_frame = ttk.Frame(main_window)
payment_frame.pack(side=ttk.BOTTOM)
# Report button frame
report_frame = ttk.Frame(main_window)
report_frame.pack(side=ttk.RIGHT)


# Selection button response message and store selection item in temp file
def payment(value):
    payment_label = ttk.Label(message_frame,text="\t\tPayment Due : $ {} \t\t".format(inp.product_price)).grid(row=0,column=0)
    with open(inp.database_file(inp.temp_file), 'w') as tp:
        csv_writer = csv.writer(tp)
        csv_writer.writerow([value])

# Cancel button to reset the message contain:
def clear_payment():
    if os.path.exists(inp.database_file(inp.temp_file)):
        payment_label = ttk.Label(message_frame, text="\tSelect your product\t\t").grid(row=0,column=0)
        inp.remove_file()
    else:
        payment_label = ttk.Label(message_frame, text="\tSelect Your Product\t\t").grid(row=0,column=0)

# Payment button function with response message and dataload to csv file
def payment_complete():
    if os.path.exists(inp.database_file(inp.temp_file)):
        payment_label = ttk.Label(message_frame, text="\tThank You for Your Payment\t\t").grid(row=0,column=0)
        with open(inp.database_file(inp.temp_file), 'r') as sel:
            pass_val = sel.readline().rstrip()
            dl.data_entry(pass_val)
        inp.remove_file()
    else:
        payment_label = ttk.Label(message_frame, text="\tSelect Your Product")
    
# Selection Image Location
coke = ttk.PhotoImage(file=inp.database_file(inp.coke)).subsample(2,2)
sprite = ttk.PhotoImage(file=inp.database_file(inp.sprite)).subsample(2,2)
fanta = ttk.PhotoImage(file=inp.database_file(inp.fanta)).subsample(2,2)
water = ttk.PhotoImage(file=inp.database_file(inp.water)).subsample(2,2)

# Selection Button
s1_button = ttk.Button(selection_frame, text="Coke", image=coke, command=lambda: payment(1)).grid(row=0,column=0)
s2_button = ttk.Button(selection_frame, text="Sprite", image=sprite, command=lambda: payment(1)).grid(row=0,column=1)
s3_button = ttk.Button(selection_frame, text="Fanta", image=fanta, command=lambda: payment(3)).grid(row=1, column=0)
s4_button = ttk.Button(selection_frame, text="Water", image=water, command=lambda: payment(4)).grid(row=1,column=1)

# Payment button
p1_button = ttk.Button(payment_frame, text="Payment", command=payment_complete).grid(row=0,column=0)
p2_button = ttk.Button(payment_frame, text="Cancel", command=clear_payment).grid(row=0,column=1)

# Report button 
r_button = ttk.Button(report_frame, text="Report", command=popup).grid(row=0, column=0)

main_window.mainloop()