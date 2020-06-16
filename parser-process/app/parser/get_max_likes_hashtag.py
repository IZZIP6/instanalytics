import itertools
import nltk
from nltk.corpus import stopwords


common_hashtag = []

# get max number of likes obtained
def get_max_likes(postInfo, hashtag):
    maximum = 0
    index = 0
    global common_hashtag
    common_hashtag = []

    try:
        for item in postInfo:
            print(item)
            if(int(item[2]) > maximum):
                maximum = int(item[2])
        index = next(i for i,v in enumerate(postInfo) if maximum in v)
        common_hashtag += [hashtag[index]]
        return [maximum, hashtag[index], postInfo[index][1]]

    except Exception as e: 
        print(e)

# get max number of comments obtained
def get_max_comments(postInfo, hashtag):
    maximum = 0
    index = 0
    global common_hashtag
    for item in postInfo:
        if(int(item[3]) > maximum):
            maximum = int(item[3])
    index = next(i for i,v in enumerate(postInfo) if maximum in v)
    common_hashtag += [hashtag[index]]
    return [maximum, hashtag[index], postInfo[index][1]]


# return the number of likes and comment in the photos 
def get_likes_comments(postInfo):
    likes_list = []
    comments_list = []
    for item in postInfo:
        likes_list.append(item[2])
        comments_list.append(item[3])
    return [likes_list, comments_list]


# return what are the subject of the photos based on Instagram ML recognition algorithm 
def get_photo_description(accessibility_caption): 
    words = []
    it_stopwords = stopwords.words('italian')
    en_stopwords = stopwords.words('english')
    for item in accessibility_caption:
        if(item is not None):
            if("Image may contain:" in item):
                description = (item.split("Image may contain:",1)[1])
                insta_sw = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "and", "or", "one", "more", "text", "says"]
                description = description.replace(",", "")
                description = description.replace("'", "")
                description = description.replace("\"", "")
                token = description.split()

                for stopword in insta_sw:
                    if stopword in token:
                        token.remove(stopword)

                # uppercase of all stopwords
                en_up = list(map(str.upper,(en_stopwords)))
                it_up = list(map(str.upper,(it_stopwords)))

                # make one single big list
                all_sw = en_stopwords + it_stopwords + en_up + it_up
                
                token = [word for word in token if not word in all_sw]

                '''
                token = [word for word in token if not word in en_stopwords]
                token = [word for word in token if not word in it_stopwords]
                token = [word for word in token if not word in en_up]
                token = [word for word in token if not word in it_up]
                '''

                for word in token:
                    words.append(word)

    return words

