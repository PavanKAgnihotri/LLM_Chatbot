#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 17:15:12 2024

@author: pavan
"""

import numpy as np

def read_data(file_name):
	file = open(file_name, "r")
	content = file.read()
	file.close()
	return content

def is_alphabet(ch):
	if ch >= 'a' and ch <= 'z':
		return True
	return ch >= 'A' and ch <= 'Z'

def clean_content(content):
	for idx in range(len(content)):
		if not is_alphabet(content[idx]):
			content[idx] = '_'
	return content

def get_words(content):
	words = []
	i = 0
	while i < len(content):
		if content[i] == '_':
			i += 1
			continue
		word = ''
		j = i
		while j < len(content):
			if content[j] != '_':
				word += content[j]
				j += 1
			else:
				break
		i += len(word)
		words.append(word.lower())
	return words

content = list(read_data("Romeo_and_Juliet.txt"))
content = clean_content(content)
words = get_words(content)
vocab = list(set(words))
vocab.sort()

# print('Vocabulary:', vocab)
print('Size of vocabulary:', len(vocab))

N = len(vocab)

# This is a matrix capturing the conditional probability p(word | context).
# We apply the 1-Markov assumption so that the context is only a single word.
prob = np.zeros((N, N))

for i in range(len(words) - 1):
	idx_1 = vocab.index(words[i])
	idx_2 = vocab.index(words[i + 1])
	prob[idx_1, idx_2] += 1
    
for i in range(N):
    if np.sum(prob[i, :]) > 0:
        prob[i, :] /= np.sum(prob[i, :])
        
# Note: The ChatGPT works in the same manner - Autoregressive.
# Generate a new sentence with a starting word.
L = 100
for start in ["romeo", "juliet", "love"]:
    current = start
    sentence = current + ' '
    for i in range(L - 1):
        idx = vocab.index(current)
        #next word is selected based on the probability distribution not highsest probability
        next_idx = np.random.choice(N, p=prob[idx, :])
        next_word = vocab[next_idx]
        sentence += next_word + ' '
        current = next_word
    print(f"\nGenerated sentence starting with '{start}':")
    print(sentence)

print('Done')