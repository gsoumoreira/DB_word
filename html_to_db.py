import mysql.connector


country_list = ['Brazil', 'Spain', 'Italy']

word_list = open("html_data/" + country_list[0] + ".txt").read().split()

mydb = mysql.connector.connect(
  host="localhost",
  user="gabi",
  password="1234",
  database="db_word"
)

# TABLES = {}
# TABLES['collect_word'] = (
#     "CREATE TABLE `word3` ("
#     "  `ID` int(11) NOT NULL AUTO_INCREMENT,"
#     "  `word` varchar(50) NOT NULL,"
#     "  PRIMARY KEY (`ID`)"
#     ") ENGINE=InnoDB")

# cursor.execute(TABLES['collect_word'])

cursor = mydb.cursor()

for word in word_list:

    ID_word = cursor.lastrowid
    print(ID_word)
    insert = ("INSERT INTO word3 (ID, word) VALUES (%s, %s)")
    data = (word)
    cursor.execute(insert, data)
    mydb.commit()
# cursor.execute("INSERT INTO word (word) VALUES (%s)", ('test'))

# for word in words:
#     ID_word = cursor.lastrowid
#     cursor.execute("INSERT INTO word VALUES (ID_word, word)")

# mydb.commit()

cursor.close()
