from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import json
import collections
import emoji
import re
import nltk


def sanitize(comment_list):
    it_stopwords = stopwords.words('italian')
    en_stopwords = stopwords.words('english')
    tokens = []
    final_token = []
    for comment in comment_list:
        comment = comment.lower() # all comment to lower case
        comment = (emoji.get_emoji_regexp().sub(u'', comment)) # remove emoji
        comment = re.sub(r'([?!,.://({@})\\*]+)','', comment) # remove some punctuation
        comment_tokens = word_tokenize(comment)
        tokens_without_sw = [word for word in comment_tokens if not word in it_stopwords]
        tokens_without_sw = [word for word in tokens_without_sw if not word in en_stopwords]
        tokens.append(tokens_without_sw)
    
    for token in tokens:
        final_token += token
    return final_token


# Instantiate a dictionary, and for every word in the file, 
# Add to the dictionary if it doesn't exist. If it does, increase the count.
def count_occurrences(text):
    global wordcount
    wordcount = {}
    for comment in text:
        for word in comment.split():
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    

# print most common n_print tag
def get_comment(comment_list):
    final_list = sanitize(comment_list)
    count_occurrences(final_list)
    n_print = 10
    tmp_lista = []
    word_list = []
    count_list = []
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(n_print):
        word_list.append(word)
        count_list.append(count)

    tmp_lista.append(word_list)
    tmp_lista.append(count_list)
    return tmp_lista
