import tkinter as tk
from tkinter import ttk
from tkcalendar import calendar

#add a calander event
def add_event():
    selected_date = cal.get_date()
    event = event_entry.get()
    if selected_date and event:
        event_calendar.insert(
            " ",
            "end"
            values=(selected_date,event))
        event_entry.delete(0,"end") 

#delete selected event
def delete_event():
    selected_item= event_calendar.seletion()
    if selected_item:
        event_calendar.delete(selected_item)      

# main window
root = tk.Tk()
root.title("Travel Planner") 
root.geometry("600x600")

#Header
header_frame = tk.Frame(root, bg="#3498db")
header_frame.pack(fill="x")

header_label = tk.Label(
    text= "Travel Planner"
    font= ("Helvetica",24),
    bg="#3498db",
    fg="white")
header_label.pack(pady=10)

#Calendar widget
cal= calendar(
    root,
    selectmode="day",
    date_pattern= "mm-dd-yyyy",
    font= ("Helvetica",16),
    background="white",
    forgeground="black"
)
cal.pack(pady=20, padx=10)
