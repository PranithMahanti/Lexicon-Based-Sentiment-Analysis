import re

import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk import pos_tag
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.corpus import stopwords
nltk.download('wordnet')
from nltk.corpus import wordnet

from nltk.stem import WordNetLemmatizer

import contractions
import pandas as pd

# Remove all numericals, special characters and punctuation marks
def clean(text):
    text = re.sub('[^A-Za-z]+', ' ', text) 
    return text

def expand_contractions(text):
    tkn = text.split(" ")
    expanded = []

    for word in tkn:
        expanded.append(contractions.fix(word))
    
    return " ".join(expanded)

def POS_tags(text):
    # Remove Stop words
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())

    filtered_tokens = [word for word in tokens if word not in stop_words]

    pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'M':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
    pos_tagged = []

    tags = pos_tag(filtered_tokens)
    for word, tag in tags:
            pos_tagged.append(tuple([word, pos_dict.get(tag[0])]))
    return pos_tagged

def lemmatize(pos_data):
    lemma_final = ""

    wordnet_lemmatizer = WordNetLemmatizer()

    for word, pos in pos_data:
        if not pos:
            lemma = word
            lemma_final = lemma_final + " " + lemma
        else:
            lemma = wordnet_lemmatizer.lemmatize(word, pos=pos)
            lemma_final = lemma_final + " " + lemma

    return lemma_final.strip()

def preprocess(data):
    text = data['text']
    data["Cleaned"] = text.apply(expand_contractions).apply(clean)
    data["POS tagged"] = data["Cleaned"].apply(POS_tags)
    data["Lemmatized"] = data["POS tagged"].apply(lemmatize)

    return data


if __name__ == "__main__":
    data = pd.read_csv('test_phrases.csv')
    print(preprocess(data))

