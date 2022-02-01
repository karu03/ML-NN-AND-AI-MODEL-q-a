import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())
    
def bag_of_words(tokeninzed_sentence,words):
    sentence_word = [stem(word)for word in tokeninzed_sentence]
    bag = np.zeros(len(words),dtype = np.float32)    

    for idx , w in enumerate(words):
        if w in sentence_word:
            bag[idx] = 1


    return bag