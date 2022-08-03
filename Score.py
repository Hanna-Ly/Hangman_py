class Score: # Et naitaks edetabeli popupil infot
    
    def __init__(self, date, name, word, misses):
        self.date = date
        self.name = name
        self.word = word
        self.misses = misses
        
    def get_date(self):
        return self.date
    
    def get_name(self):
        return self.name
    
    def get_word(self):
        return self.word
    
    def get_misses(self):
        return self.misses
    
    