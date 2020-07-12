import mysql.connector

with open('html_data/test.txt', 'r') as var:
    for line in var:
        li = line

# Making some cleaning in the text file
li1 = li.replace('\\n','')
li2 = li1.replace('\\r','')
li3 = li2.replace('\r','')
li4 = li3.replace('\n','')
li5 = li4.replace('\\','')
li6 = li5.replace(')','')
li7 = li6.replace('(','')
li8 = li7.replace(']','')
li9 = li8.replace('[','')
li10 = li9.replace(',','')
li11 = li10.replace('.','')
li12 = li11.replace(':','')

li_final = list(li12.split(' '))

new_list = []
for i in li_final:
    new_list.append((i,))

mydb = mysql.connector.connect(
  host="localhost",
  user="gabi",
  password="1234",
  database="db_word"
)

cursor = mydb.cursor()

# Use execute many to insert many lines
stmt = "INSERT INTO exe3 (Word) VALUES (%s)"
cursor.executemany(stmt, new_list)

mydb.commit()
mydb.close()
