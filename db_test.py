import sqlite3

connection = sqlite3.connect('words.db')
cursor = connection.execute('SELECT * FROM words ORDER BY word')
data = cursor.fetchall()


#print(data)
for row in data:
    print(row[0], row[1], row[2])
    
# ilma data reata

#for row in cursor:
#    print(row[0], row[1], row[2])

connection.close()