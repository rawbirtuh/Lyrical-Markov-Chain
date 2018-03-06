import pronouncing
import numpy as np
import random

lyrics = open('Songs/chorus.txt').read()

corpus = lyrics.split()

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])

toRhyme = ''
for i in range(10):        
    pairs = make_pairs(corpus)

    word_dict = {}

    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(corpus)

    while first_word.islower():
        first_word = np.random.choice(corpus)

    chain = [first_word]

    n_words = 6

    for i in range(n_words):
        
        chosen = np.random.choice(word_dict[chain[-1]])
        chain.append(chosen)

    ' '.join(chain)

    newLine = ''
    wordCount = 0
    for words in chain:
        
        rand = random.randint(1,100)
        if wordCount == 7 and toRhyme == '':
            toRhyme = words
        elif wordCount == 7 and toRhyme != '':
            lastWord = pronouncing.rhymes(toRhyme)
            newLine = newLine + " " + lastWord[0]
            toRhyme = ''
            break
        newLine = newLine + " " + words
        wordCount += 1
    

    print (newLine)
