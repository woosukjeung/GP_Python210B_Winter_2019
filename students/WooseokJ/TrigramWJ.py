
# coding: utf-8

# In[3]:


import sys 
import random

#takes the words from the given file and returns it in a list
def words_from_file(filename):
    with open(filename, 'r') as textfile: 
        return [word.strip('\n') for l in textfile.readlines() 
                for word in l.split(' ')] 
#from the list makes a dictiondary to mix it in the next process
def build_trigrams_dict(words):
    trigrams = {}
    for i, w in enumerate(words): 
        if i + 2 < len(words): 
            first = w.strip() 
            second = words[i + 1].strip() 
            third = words[i + 2].strip() 
            mix = '{} {}'.format(first, second) 
            if mix not in trigrams.keys(): 
                trigrams[mix] = [] 
            trigrams[mix].append(third) 
    return trigrams 
#this mixes the words to create the trigram 
def build_text(trigrams, num, new_words=[]):
    if len(new_words) >= int(num) or int(num) < 3: 
        return ' '.join(new_words) 
    if not new_words: 
        second_start = random.choice(list(trigrams.keys())) 
        new_words.extend(second_start.split(' ')) 
    if len(new_words) > 1: 
        mix = '{} {}'.format(new_words[-2], new_words[-1])
        if mix not in trigrams.keys(): 
            mix = random.choice(list(trigrams.keys()))
        third = random.choice(trigrams[mix]) 
        new_words.append(third) 
#this is a promot that asks for the file that we want to scramble make sure to add .txt at the end of the file
        return build_text(trigrams, num, new_words)
if __name__ == '__main__':
    filename = input('Please enter a filename:\n--->')
    length = 178
    words = words_from_file(filename)
    trigrams = build_trigrams_dict(words)
    new_text = build_text(trigrams,length)
    print (new_text) 

