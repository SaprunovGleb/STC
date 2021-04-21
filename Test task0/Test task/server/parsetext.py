# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:36:26 2021

@author: Flyin
"""
from string import punctuation
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize 

#print (nltk.__version__)
def parsetext(data):
    stop_words = set(stopwords.words('english') + list(punctuation)+['«','»','’']) 
    #stop_symvols = [',','.','!','@','\n']
    data = data.lower()
    list_sentenses = sent_tokenize(data)
    list_tokens = []
    for sent in list_sentenses:
        wordsList = nltk.word_tokenize(sent)
        wordsList = [w for w in wordsList if not w in stop_words]
        #wordsList = [w for w in wordsList if not w in stop_symvols]
        list_tokens.append(wordsList)
    return list_tokens


if __name__=='__main__':
    data = "I am here. I'm like to eat."
    #print(str(parsetext(data)))