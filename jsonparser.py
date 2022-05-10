import json
import sqlite3

with open("kanji.json", "r", encoding="utf-8") as f:
    data = json.load(f)

conn = sqlite3.connect('kanjidb.sqlite')
cur = conn.cursor()

list_attributes = []

count = 0

for k, v in data.items():
    if count == 1:
        break
    for keys, values in v.items():
        list_attributes.append(keys)
    count += 1

print(list_attributes)
first_3 = list_attributes[:6]

cur.execute('DROP TABLE IF EXISTS Kanji')
cur.execute('''
            CREATE TABLE Kanji (id INTEGER PRIMARY KEY AUTOINCREMENT,
            kanji TEXT UNIQUE, strokes INTEGER, grade INTEGER,
            jlpt_old INTEGER, jlpt_new INTEGER, meanings_id INTEGER 
            onyomi_id INTEGER, kunyomi_id INTEGER, wk_level INTEGER, 
            wk_meanings_id INTEGER, wk_onyomi_id INTEGER, 
            wk_kunyomi_id INTEGER, wk_radicals_id INTEGER)''')   

count = 0
for k, v in data.items():
    kanji = k
    print(k)
    cur.execute('INSERT INTO Kanji (kanji) VALUES (?)',(kanji, ))
    
    if count == 10:
        break
    
    # for keys, values in v.items():
    #     if(keys in first_3):
    #         cur.execute('UPDATE Kanji SET ? = ? WHERE kanji = ?', (keys, v[keys], kanji))
    
    count += 1
