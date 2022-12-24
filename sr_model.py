import pandas as pd
import speech_recognition as sr
import nltk
import pyttsx3
import time

from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')

stop_words = set(stopwords.words('english'))

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
	print('Listening')
	audio = r.listen(source)
	print('Recognizing')
	text = r.recognize_google(audio)

print(text)

new_words = ["fig", "figure", "image", "sample", "using",
             "show", "result", "large",
             "also", "one", "two", "three",
             "four", "five", "seven", "eight", "nine"]

stop_words = list(stop_words.union(new_words))

text = text.lower()
text = text.split()
text = [word for word in text if word not in stop_words]
text = [word for word in text if len(word) >= 3]
lmtzr = WordNetLemmatizer()
text = [lmtzr.lemmatize(word) for word in text]

print(text)
print(type(text))

data = pd.read_excel('btp_dataset.xlsx')
Word_list = data['Word'].tolist()

for word in text:
	if word in Word_list:
		print('Task Success - Finding out what class it belongs to')
		time.sleep(2)
		print('The word is happy ')
		time.sleep(5)
		print('Class 1')
		break
	else:
		print('Iterate to other word')

print('Task Over')