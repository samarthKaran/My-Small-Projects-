# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 10:47:43 2017

@author: samarth
"""
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize
nltk.download('punkt')

ps = PorterStemmer()
new_text = "Hi! I am an Engineer. Bye."
words = word_tokenize(new_text)

for word in words:
    print(ps.stem(word))