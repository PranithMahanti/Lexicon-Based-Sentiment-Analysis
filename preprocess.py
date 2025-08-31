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


def clean(text):
    '''
    Remove all numericals, special characters and punctuation marks

    Args:
        text (str): Regular unprocessed news headlines
    Returns:
        str: Processed and clean text

    '''
    text = re.sub('[^A-Za-z]+', ' ', text) 
    return text

def expand_contractions(text):
    '''
    Replace all the contractions with their expanded equivalents

    Args:
        text (str): Processed data 
                    (preferrably output from clean func.)
    Returns:
        str: Text with expanded equivalents of contractions.
        
    '''
    tkn = text.split(" ")
    expanded = []

    for word in tkn:
        expanded.append(contractions.fix(word))
    
    return " ".join(expanded)

def POS_tags(text):
    '''
    Remove the stopwords and tokenize the text along with POS(Parts of speech) tags.

    Args:
        text (str): Processed data with expanded contractions 
                    (preferrably output from expand_contractions func.)
    Returns:
        list: A list of tuples that occur in pairs of words abd the respective pos.
              Note, the only pos that will be reported are [Adjectives, Verbs, Nouns, Adverbs] 
              since they are the only ones to be lemmatized.
        
    '''
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
    '''
    Replace all the contractions with their expanded equivalents

    Args:
        pos_data (list): A list of tuples of form (word, pos)
                         (preferrably output of POS_tags func.)
    Returns:
        str: A string with only lemmatized words. Can be seperated easily using split() function.
        
    '''
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

def preprocess(series):
    '''
    Replace all the contractions with their expanded equivalents

    Args:
        series (pd.Series): 
            A pandas Series which should contain a column titled <text>
    Returns:
        pd.Series: 
            A pandas Series with added columns 
                <Cleaned>   : Cleaned data with expanded contractions and with numericals, special char and punctuations removed.
                <POS tagged>: List of tuples of form (word, pos)
                <Lemmatized>: Strings of lemmatized text (Final Output)
        
    '''
    text = series['text']
    series["Cleaned"] = text.apply(expand_contractions).apply(clean)
    series["POS tagged"] = series["Cleaned"].apply(POS_tags)
    series["Lemmatized"] = series["POS tagged"].apply(lemmatize)

    return series


# For the purpose of testing
# test_phrases.csv: Has all sample headlines.
# final_output.csv: Well, the name explains it, pretty much.
if __name__ == "__main__":
    data = pd.read_csv('test_phrases.csv')
    preprocess(data).to_csv('final_output.txt')

