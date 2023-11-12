from scipy import spatial

def creating_text_word8(file1, file2):
    file = open(file1, 'r')
    new_file = open(file2, "w")
    for line in file:
        if line != "\n":
            words = line.split()
            words = trunc_to_eight(words)
            for word in words:
                new_file.write(word + " ")
            new_file.write("\n")

    file.close()
    new_file.close()

def new_tasa(file1, file2):
    maximum = 15000

    dictionary = {}
    text_file = open(file1, "r")
    for line in text_file:
        if line != "\n":
            words = line.split()
            words = trunc_to_eight(words)
            for word in words:
                if dictionary.get(word) is None:
                    dictionary[word] = 1
                else:
                    dictionary[word] += 1

    text_file.close()

    file = open(file1, 'r')
    new_file = open(file2, "w")
    for line in file:
        if line != "\n":
            words = line.split()
            words = trunc_to_eight(words)
            for word in words:
                if dictionary[word] < maximum:
                    new_file.write(word + " ")
                    # new_file.write("\n")

    file.close()
    new_file.close()


def trunc_to_eight(words):
    i = 0
    for word in words:
        if len(word) > 8:
            words[i] = word[0:8]
        i += 1
    return words

def get_answer_mod(words):
    distance_function = cosine_norm
    min_value = max(distance_function(words[0], words[1]), distance_function(words[0], words[2]), distance_function(words[0], words[3]),
                    distance_function(words[0], words[4]))
    i = 1
    while min_value != distance_function(words[0],words[i]):
        i += 1
    if i == 1:
        return 1
    else:
        return 0

def cosine_norm(x, y):
    return 1-spatial.distance.cosine(x,y)