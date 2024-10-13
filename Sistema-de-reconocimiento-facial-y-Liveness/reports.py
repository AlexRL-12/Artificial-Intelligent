from admin_reports.get_reports import Reports
from tkinter import *
from tkinter import ttk

def get_screen_resolution():
  root = Tk()
  width = root.winfo_screenwidth()
  height = root.winfo_screenheight()
  root.destroy()
  return (width, height)

if __name__ == '__main__':
  resolution = get_screen_resolution()
  reports = Reports()
  reports.show_reports(resolution)
