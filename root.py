import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import ttk
import requests
import webbrowser

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window CustomTkinter complex_example.py
        self.title("Patent Searcher")
        self.geometry(f"{1400}x{800}")
        self.minsize(1000, 600)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Patent Searcher", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.usptoWebsite, text= 'USPTO Website')
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.patentBasics, text= 'Patent Basics')
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.patentNews, text= 'Patent News')
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_frame, command=self.patentApplication, text= 'Patent Application')
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

       
        # create main entry and button
        self.logo_label = customtkinter.CTkLabel(self, text="Patent Searcher", font=customtkinter.CTkFont(size=50, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=(0, 0), pady=(0, 0))

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Search patents")
        self.entry.grid(row=0, column=1, padx=(150, 150), pady=(200, 20), sticky="ew")

        #USPTO API request
        url = 'https://developer.uspto.gov/ibd-api/v1/application/publications?searchText='

        def pressReturn(event):
            input = self.entry.get()
            input = input.replace(" ", "%20")
            print(input)
            r = requests.get(url + input + "&rows=2", verify=False)
            print(r.json()["results"][1]["inventorNameArrayText"][0])

        self.entry.bind('<Return>', pressReturn)
    

       # create scrollable frame left
       
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self)
      
        self.scrollable_frame.grid(row=1, rowspan=2, column=1, padx=(40, 40), pady=(20, 0), sticky="nsew")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        # Data Table
        table = ttk.Treeview(self.scrollable_frame, columns = ('title', 'name', 'date', 'abstract', 'number','pdf'), show = 'headings')
        table.heading('title', text='Patent Title')
        table.heading('name', text='Inventor')
        table.heading('date', text='Date')
        table.heading('abstract', text='Abstract')
        table.heading('number', text='Number')
        table.heading('pdf', text='Pdf')
        table.pack()

        #for i in data:
          #  table.insert(tk.END, f"{i['name']} - {i['value']}")


        # create scrollable frame right
        #self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="Recent Filings")
        #self.scrollable_frame.grid(row=1, rowspan=2, column=2, padx=(20, 20), pady=(20, 0), sticky="nsew")
        #self.scrollable_frame.grid_columnconfigure(0, weight=1)
        

        '''
        self.scrollable_frame_switches = []
        for i in range(100):
            switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
            switch.grid(row=i, column=0, padx=10, pady=(0, 20))
            self.scrollable_frame_switches.append(switch)
        '''
        
        # set default values

        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")
        
        """"
        self.slider_1.configure(command=self.progressbar_2.set)
        self.slider_2.configure(command=self.progressbar_3.set)
        self.progressbar_1.configure(mode="indeterminnate")
        self.progressbar_1.start()

        self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        self.seg_button_1.set("Value 2")
"""
    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)
    
    def usptoWebsite(self):
            webbrowser.open_new("https://www.uspto.gov/patents")

    def patentBasics(self):
            webbrowser.open_new("https://www.uspto.gov/patents/basics/essentials")

    def patentApplication(self):
            webbrowser.open_new("https://www.uspto.gov/patents/basics/apply")

    def patentNews(self):
            webbrowser.open_new("https://www.uspto.gov/about-us/news-updates")
        

if __name__ == "__main__":
    app = App()
    app.mainloop()
# Create a window
# window = tk.Tk()
# window.title('GUI')
# window.geometry('1470x900')

# Add a label widget
# titleLabel = ttk.Label(master = window, text='Hello', font = 'Calibri 24 bold')
# titleLabel.pack()

# entry = ttk.Entry(master=window)
# entry.pack()

# Start the main event loop
# window.mainloop()

# Stacked vertically tabs
'''
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='wn')

notebook = ttk.Notebook(root, style='lefttab.TNotebook')

f1 = tk.Frame(notebook, bg='red', width=200, height=200)
f2 = tk.Frame(notebook, bg='blue', width=200, height=200)

notebook.add(f1, text='Frame 1')
notebook.add(f2, text='Frame 2')

notebook.grid(row=0, column=0, sticky="nw")

root.mainloop()
'''