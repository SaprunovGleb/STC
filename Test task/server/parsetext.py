# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 13:36:26 2021

@author: Flyin
"""
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize 


def parsetext(data):
    stop_words = set(stopwords.words('english') + list(punctuation)+['«','»','’']) 
    data = data.lower()
    list_sentenses = sent_tokenize(data)
    list_tokens = []
    for sent in list_sentenses:
        list_words = word_tokenize(sent)
        list_words = [w for w in list_words if not w in stop_words]
        list_tokens.append(list_words)
    return list_tokens


