import tkinter as tk
from tkinter import ttk

# Create a window
window = tk.Tk()
window.title('GUI')
window.geometry('1470x900')

# Add a label widget
titleLabel = ttk.Label(master = window, text='Hello', font = 'Calibri 24 bold')
titleLabel.pack()










# Start the main event loop
window.mainloop()