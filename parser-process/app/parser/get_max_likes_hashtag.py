import itertools

common_hashtag = []

def get_max_likes(postInfo, hashtag):
    maximum = 0
    index = 0
    global common_hashtag
    common_hashtag = []
    for item in postInfo:
        if(int(item[2]) > int(maximum)):
            maximum = item[2]
    index = next(i for i,v in enumerate(postInfo) if maximum in v)
    common_hashtag += [hashtag[index]]
    print("*"*25)
    print(common_hashtag)
    return [maximum, hashtag[index], postInfo[index][1]]


def get_max_comments(postInfo, hashtag):
    maximum = 0
    index = 0
    global common_hashtag
    for item in postInfo:
        if(int(item[3]) > int(maximum)):
            maximum = item[3]
    index = next(i for i,v in enumerate(postInfo) if maximum in v)
    common_hashtag += [hashtag[index]]
    return [maximum, hashtag[index], postInfo[index][1]]


# return a list of hashtag from the most likes and most commented posts
def get_common_hashtag(postInfo, hashtag):
    global common_hashtag
    common_hashtag = list(itertools.chain.from_iterable(common_hashtag)) # put list of list together 
    #common_hashtag = list(set(common_hashtag)) # remove possible duplicates
    return common_hashtag

def get_likes_comments(postInfo):
    likes_list = []
    comments_list = []
    for item in postInfo:
        likes_list.append(item[2])
        comments_list.append(item[3])
    return [likes_list, comments_list]





