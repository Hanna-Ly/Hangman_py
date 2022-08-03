from tkinter import messagebox
from datetime import datetime
from Model import *
from View import *
from tkinter import simpledialog

class Controller:
    
    def __init__(self):
        self.model = Model() # Laseb kasutada Model klassi Controller klassis
        self.view = View(self)
        
    def main(self):
        self.view.main() # View.py failis olev main meetod
        
        
    def btn_new_click(self):
        'Uus mäng nupu vajutamine'
        #print('Klikiti nuppu Uus mäng') # Kas nupp tootab
        self.model.set_new_game() # Tee uus mang
        self.view.label.configure(text=self.model.user_word) # Muutuja
        self.view.label_error.configure(text=f'Valesti 0 täht(e)') # f on vormindatud string
        self.view.button['state'] = NORMAL
        self.view.label_error.configure(fg='black')
        self.model.reset_answer()
        
    def btn_send_click(self):
        self.model.get_user_input(self.view.userinput.get().strip())
        #print(self.model.user_word) # Testiks
        self.view.label.configure(text=self.model.get_user_word()) # Sama mis rida 17
        self.view.label_error.configure(text=f'Valesti {self.model.get_counter()} täht(e). {self.model.get_all_user_chars()}')
        self.view.char_input.delete(0, 'end') # Tuhjendab kursori valja
        if self.model.get_counter() >=1:
            self.view.label_error.configure(fg='red')
        self.is_game_over()
        
        
    def is_game_over(self):
        if self.model.get_counter() >= 8 or '_' not in self.model.get_user_word():
            # messagebox.showinfo('Teade', 'Mäng on läbi!\nKuidas on mängija nimi?')
            self.view.button['state'] = DISABLED
            
            answer = simpledialog.askstring('Input', 'Mäng on läbi!\nMis on sinu eesnimi?', parent=self.view)
            if answer is not None:
                print('Sinu nimi on', answer)
            else:
                print('TEADMATA')
            self.model.set_username(answer) # Saadame info mudelile
            
    def btn_scoreboard_click(self):
        popup_frame = self.view.create_popup_window() # Frame
        data = self.model.read_file_contents() # Loe faili sisu Listi (Objekt)    
        self.view.generate_scoreboard(popup_frame, data)       
            
      
