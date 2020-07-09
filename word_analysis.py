import mysql.connector
import numpy as np
import seaborn as sns
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt


word_list = open("html_data/Brazil.txt").read().split()

mydb = mysql.connector.connect(
  host="localhost",
  user="gabi",
  password="1234",
  database="db_word"
)

cursor = mydb.cursor()

cursor.execute("SELECT * FROM word3")

# It gives a python list with the DB words and index
word_list = cursor.fetchall()
print(word_list)

# Using the tensorflow example
imdb, info = tfds.load("imdb_reviews", with_info=True, as_supervised=True)

train_data, test_data = imdb['train'], imdb['test']

training_sentences = []

# str(s.tonumpy()) is needed in Python3 instead of just s.numpy()
for s,l in train_data:
  training_sentences.append(s.numpy().decode('utf8'))

vocab_size = 10000
embedding_dim = 16
max_length = 120
trunc_type='post'
oov_tok = "<OOV>"

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

tokenizer = Tokenizer(num_words = vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)
word_index = tokenizer.word_index
sequences = tokenizer.texts_to_sequences(training_sentences)
padded = pad_sequences(sequences,maxlen=max_length, truncating=trunc_type)

f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(training_sentences[0], annot=True, fmt="d", linewidths=.5, ax=ax)
