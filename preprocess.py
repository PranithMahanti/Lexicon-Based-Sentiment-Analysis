import re

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.corpus import wordnet

import contractions
import pandas as pd

data = pd.read_csv('test_phrases.csv')

# Remove all numericals, special characters and punctuation marks
def clean(text):
    text = re.sub('[^A-Za-z]+', ' ', text) 
    return text

text = '''I'll be there within 5 min. Shouldn't you be there too? 
          I'd love to see u there my dear. It's awesome to meet new friends.
          We've been waiting for this day for so long.'''

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())

    filtered_tokens = [word for word in tokens if word not in stop_words]

    print("Original:", tokens)
    print("Filtered:", filtered_tokens)

def expand_contractions(text):
    tkn = text.split(" ")
    expanded = []

    for word in tkn:
        expanded.append(contractions.fix(word))
    
    return " ".join(expanded)

t = clean(expand_contractions(text=text))
print(t)
remove_stopwords(t)

