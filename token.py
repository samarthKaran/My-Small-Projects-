# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:11:17 2017

@author: samarth
"""
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords 
nltk.download('stopwords')
UNI = "Hey! This is my university. Awesome"
#print(word_tokenize(HMR))
#print(sent_tokenize(HMR))

stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(UNI)

filter_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
       if not w in stop_words:
           filtered_sentence.append(w)
print(word_tokens)
print(filtered_sentence)
           
