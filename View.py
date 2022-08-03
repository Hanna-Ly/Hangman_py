from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from datetime import datetime

class View(Tk):
    
    def __init__(self, controller):
        super().__init__() # Tk jaoks meetod, et saaks igalpool tk-d kasutada
        # Moned muutujad
        self.controller = controller
        self.userinput = StringVar()
        self.bigFontStyle = tkFont.Font(family='Courier', size=18, weight='bold') # suur tekst
        self.defaultFontStyle = tkFont.Font(family='Verdana', size=10) # Tavaline
        self.defaultFontStyleBold = tkFont.Font(family='Verdana', size=10, weight='bold')
        
        # Pohiaken
        self.geometry('450x200') # Akna suurus
        self.resizable(True, True) # Akna suurust saab muuta
        self.title('Hangman') # Tiitel rea tekst
        
        # Framede valja kutsumine
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()
        
        # Vidinad - Widget
        self.create_new_button() # Uus mang nupp 
        self.char_input, self.label_error, self.button = self.create_userinput() # Tahe kast ja Errori kast
        self.label = self.create_result_label() # Vastuse kast
        self.create_popup_button() # Edetabeli nupp
        
    def main(self):
        self.mainloop()
        
    # Framede tegemine
    def create_top_frame(self):
        frame = Frame(self, bg='blue', height=50)
        frame.pack(expand=True, fill='both')
        return frame
    
    def create_bottom_frame(self):
        frame = Frame(self, bg='yellow')
        frame.pack(expand=True, fill='both')
        return frame 
 
    # Tee Uus mang nupp
    def create_new_button(self):
        button = Button(self.top_frame, text='Uus mäng', font=self.defaultFontStyle, command=lambda:self.controller.btn_new_click())
        button.grid(row=0, column=0, padx=5, pady=5, sticky=EW)
        
                   
    # Label 2x, Entry, Button Saada         
    def create_userinput(self):
        label_info = Label(self.top_frame, text='Sisesta täht', font=self.defaultFontStyleBold, )
        label_info.grid(row=1, column=0, padx=5, pady=5)
        
        char_input = Entry(self.top_frame, textvariable=self.userinput, justify='center', font=self.defaultFontStyle)
        char_input.grid(row=1, column=1, padx=5, pady=5)
        char_input.focus() # Aktiivne teksti kursor
        
        button = Button(self.top_frame, text='Saada', font=self.defaultFontStyle, command=lambda:self.controller.btn_send_click(), state='disabled')
        button.grid(row=1, column=2, padx=5, pady=5)
    
        label_error = Label(self.top_frame, text='Valesti 0 täht(e).', anchor='w', font=self.defaultFontStyleBold)
        label_error.grid(row=2, column=0, columnspan=3, padx=5, pady=5, sticky=EW)
        
        return char_input, label_error, button
    
    def create_result_label(self):
        label = Label(self.bottom_frame, text='HAKKAME MÄNGIMA', font=self.bigFontStyle, bg='yellow')
        label.pack(padx=5, pady=5)
        return label
    
    # Popup osa
    def create_popup_button(self):
        button = Button(self.top_frame, text='Edetabel', font=self.defaultFontStyle, 
                        command=lambda:self.controller.btn_scoreboard_click())
        button.grid(row=0, column=1, padx=5, pady=5, sticky=EW)
    
    def create_popup_window(self):
        top = Toplevel(self)
        top.geometry('500x150')
        top.title('Edetabel')
        top.resizable(0,0) # Ei saa muuta akna suurust
        top.grab_set() # Modal, ehk ei saa alumise akna peal edasi mangida, kui edetabeli aken on lahti
        top.focus() # Et aen oleks aktiivne
        frame = Frame(top)
        frame.pack(expand=True, fill='both')
        return frame
        
    def generate_scoreboard(self, frame, data):
        my_table = ttk.Treeview(frame)
        
        # Vertikaalne kerimisrida
        vsb = ttk.Scrollbar(frame, orient='vertical', command=my_table.yview)
        vsb.pack(side='right', fill='y')
        my_table.configure(yscrollcommand=vsb.set)
        
        # Veeru n.ö id
        my_table['columns'] = ('date_time', 'player_name', 'word', 'misses')
        
        # Veeru omadused
        my_table.column('#0', width=0, stretch=NO)
        my_table.column('date_time', anchor=CENTER, width=80)
        my_table.column('player_name', anchor=CENTER, width=80)
        my_table.column('word', anchor=CENTER, width=80)
        my_table.column('misses', anchor=CENTER, width=80)
        
        # Veeru pealkirjad
        my_table.heading('#0', text='', anchor=CENTER)
        my_table.heading('date_time', anchor=CENTER, text='Kuupäev\Kellaaeg')
        my_table.heading('player_name', anchor=CENTER, text='Mängija')
        my_table.heading('word', anchor=CENTER, text='Arvatav sõna')
        my_table.heading('misses', anchor=CENTER, text='Vigased tähed')
        
        # Andmete lisamine
        i = 0
        for p in data:
            date_time = datetime.strptime(p.get_date(),'%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y %H:%M:%S')
            my_table.insert(parent='', index='end', iid=i, text='', values=(date_time, p.get_name(), p.get_word(), p.get_misses()))
            i+=1
        
        # Paiguta framele
        my_table.pack(expand=True, fill='both')