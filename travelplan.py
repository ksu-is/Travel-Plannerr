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


