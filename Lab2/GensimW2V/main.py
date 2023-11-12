# import modules & set up logging
import gensim, logging, numpy as np
import help_functions as hf
import nltk

#@author: The first version of this code is the courtesy of Vadim Selyanik


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
lemmatizer = nltk.WordNetLemmatizer() # create a lemmatizer

sentences = []
file = open("lemmatized.text", "r")

for line in file: # read the file and create list which contains all sentences found in the text
    sentences.append(line.split())
# train word2vec on the two sentences

dimension = 50 # parameter for Word2vec size of vectors for word embedding

threshold = 0.00055 # parameter for Word2vec


sum = 0.0

# 
model = gensim.models.Word2Vec(sentences, min_count=1, sample=threshold, sg=1,size=dimension) # create model using Word2Ve with the given parameters
#
print(len(model.vocab)) # check the length of the vocabulary which was formed by Word2Vec

#The rest implements passing TOEFL tests
i = 0 #counter for TOEFL tests
number_of_tests = 80
text_file = open('new_toefl.txt', 'r')
right_answers = 0 # variable for correct answers
number_skipped_tests = 0 # some tests could be skipped if there are no corresponding words in the vocabulary extracted from the training corpus
while i < number_of_tests:
            line = text_file.readline() #read line in the file
            words = line.split() # extract words from the line
            try:
                words = [lemmatizer.lemmatize(lemmatizer.lemmatize(lemmatizer.lemmatize(word, 'v'), 'n'), 'a') for word in
                         words] # lemmatize words in the current test
                vectors = []
                if words[0] in model: # check if there embedding for the query word
                    k = 1 #counter for loop iterating over 5 words in the test
                    vectors.append(model[words[0]])
                    while k < 5:
                        if words[k] in model: # if alternative has the embedding
                            vectors.append(model[words[k]]) #assing the learned vector
                        else: 
                            vectors.append(np.random.randn(dimension)) #assing random vector
                        k += 1
                    right_answers += hf.get_answer_mod(vectors) #find the closest vector and check if it is the correct answer

            except KeyError: # if there is no representation for the query vector than skip
                number_skipped_tests += 1
                print("skipped test: " + str(i) + "; Line: " + str(words))
            except IndexError:
                print(i)
                print(line)
                print(words)
                break
            i += 1
text_file.close()
sum += 100 * float(right_answers) / float(number_of_tests) #get the percentage
print("Threshold ferq = "+ str(threshold)+" Percentage of correct answers: " + str(sum) + "%")