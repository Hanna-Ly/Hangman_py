import sqlite3
from datetime import datetime
from Score import *

class Model:
    
    def __init__(self): # Konstruktor
        self.database_name = 'words.db' # Andmebaasi nimi
        self.new_word = None # Sona mida ara arvatakse
        self.user_word = [] # Kasutaja leitud tahed
        self.all_user_chars = [] # Koik valesti sisestatud tahed
        self.counter = 0 # Vigade loendur
        self.answer = 'TEADMATA' # Mangija nimi kui pole sisestatud
        self.score_filename = 'score.txt' # Edetabeli fail
        self.score_data = [] # score.txt faili sisu
        
    def get_random_word(self):
        'Üks juhuslik sõna tabelist'
        connection = sqlite3.connect(self.database_name)
        cursor = connection.execute('SELECT * FROM words ORDER BY RANDOM() LIMIT 1') # Ainult uks kirje 
        self.new_word = cursor.fetchone()[1] # Veerg word on [1] id on [0]
        connection.close()
        
    def set_new_game(self):
        'Tee uus mäng'
        self.get_random_word() # Tee uus sona
        self.user_word = [] # Leitud tahed eemaldada
        self.all_user_chars = [] # Valesti sisestatud tahed eemaldada
        self.counter = 0 # Vigade loendur nulliks
        for i in range(len(self.new_word)):
            self.user_word.append('_')
        #print(self.new_word) # Test
        #print(self.user_word) # Test   
        
    def get_user_input(self, value):
        'Mida kasutaja sisestas'
        if value: # Kasutaja on midagi sisestanud ja see pole tyhi
            user_char = value[0:1] # Soltumata stringi pikkusest ainult esimen mark
            if user_char.lower() in self.new_word.lower(): # a in autojuht
                self.change_user_input(user_char) # Leiti
            else: # Ei leitud
                self.counter += 1 # Vigade loendur kasvab +1
                self.all_user_chars.append(user_char.upper())
                
    def change_user_input(self, user_char):
        current_word = self.chars_to_list(self.new_word)
        i = 0
        for c in current_word:
            if user_char.lower() == c.lower():
                self.user_word[i] = user_char.upper()
            i += 1
    
    def chars_to_list(self, string):
        chars = []
        chars[:0] = string
        return chars
    
    def get_user_word(self):
        'Tagastab kasutaja leitud tahed'
        return self.user_word
    
    def get_counter(self):
        'Tagasta loenduri vaartus'
        return self.counter
    
    def get_all_user_chars(self):
        'tagasta Listina koik valed sisestused'
        return ', '.join(self.all_user_chars)
    
    def reset_answer(self):
        self.answer = 'TEADMATA'
        
    def set_username(self,username):
        line= []
        now = datetime.now().strftime('%Y-%m-%d %T')
        if username:
            self.answer = username
            
        line.append(now)
        line.append(self.answer)
        line.append(self.new_word)
        line.append(self.get_all_user_chars())
        
        with open(self.score_filename, 'a+', encoding='utf-8') as f:
            f.write(';'.join(line) + '\n')
            
    def read_file_contents(self):
        self.score_data = []
        with open(self.score_filename, 'r', encoding='utf-8') as f:
            all_lines = f.readlines() # Loe fili sisu listi
            for line in all_lines:
                parts = line.strip().split(';')
                self.score_data.append(Score(parts[0], parts[1], parts[2], parts[3]))
            #print(self.score_data[0].get_name()) # Testiks!
        return self.score_data