import numpy as np
from scipy import spatial
#import scipy


def get_random_word_vector(dimension, k):
    positions = np.random.permutation(dimension)[0:2 * k]
    minus_positions = positions[0:k]
    plus_positions = positions[k:2 * k]
    v = np.array(np.zeros(dimension),np.int8)
    v[minus_positions] = -1
    v[plus_positions] = 1
    return v

def get_random_word_vector_bin(dimension):
    k = (int)(dimension/2)
    positions = np.random.permutation(dimension)[0:2 * k]
    minus_positions = positions[0:k]
    plus_positions = positions[k:2 * k]
    v = np.array(np.zeros(dimension), np.int8)
    v[minus_positions] = -1
    v[plus_positions] = 1
    return v

def get_answer(letter, word,  values):
    answer_list = ['A', 'B', 'C', 'D']
    distance_function = cosine_norm
    min_value = max(distance_function(word, values[0]), distance_function(word, values[1]), distance_function(word, values[2]),
                    distance_function(word, values[3]))
    i = 0
    while min_value != distance_function(word,values[i]):
        i += 1
    if answer_list[i] == letter:
        return 1
    else:
        return 0

def get_answer_mod(words):
    distance_function = cosine_norm
    min_value = max(distance_function(words[0], words[1]), distance_function(words[0], words[2]), distance_function(words[0], words[3]),
                    distance_function(words[0], words[4]))
    i = 1
    # while i <=4 and min_value != distance_function(words[0],words[i]):
    #     i+=1
    if min_value == distance_function(words[0],words[1]):
        return 1
    else:
        return 0

def euclidian_norm(x,y):
    return np.linalg.norm(x-y)

def cosine_norm(x, y):
    return 1-spatial.distance.cosine(x,y)

def trunc_to_eight(words):
    i = 0
    for word in words:
        if len(word) > 8:
            words[i] = word[0:8]
        i += 1
    return words
