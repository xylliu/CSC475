import numpy as np
import pickle
from sklearn.naive_bayes import BernoulliNB
from sklearn import metrics

data = np.load('/Users/llicht/Documents/csc475_asn3_data/data.npz')
a = data['arr_0']
a[a > 0] = 1
labels = np.load('/Users/llicht/Documents/csc475_asn3_data/labels.npz')
labels = labels['arr_0']
dictionary = pickle.load(open('/Users/llicht/Documents/csc475_asn3_data/dictionary.pck', 'rb'), encoding = 'latin1')
word_indices = [41, 1465, 169, 217, 1036, 188, 260, 454, 173, 728, 163, 151, 107, 142, 90, 141, 161, 131, 86, 73, 165, 133, 84, 244, 153, 126, 137, 119, 80, 224]
words = [dictionary[r] for r in word_indices]
rap_rows = a[0:1000,:]
rock_rows = a[1000:2000,:]
country_rows = a[2000:3000,:]

word_probs_rap = (rap_rows.sum(axis=0).astype(float) + 1.0) / (len(rap_rows)+1.0)
word_probs_rock = (rock_rows.sum(axis=0).astype(float) + 1.0) / (len(rock_rows)+1.0)
word_probs_country = (country_rows.sum(axis=0).astype(float) + 1.0) / (len(country_rows)+1.0)

word_probs_for_genre = [word_probs_rap, word_probs_rock, word_probs_country]

def likelihood(test_song, word_probs_for_genre):
    probability_product = 1.0
    for (i,w) in enumerate(test_song):
        if (w==1):
            probability = word_probs_for_genre[i]
        else:
            probability = 1.0 - word_probs_for_genre[i]
        probability_product *= probability
    return probability_product

def predict(test_song, probs):
    probs = [likelihood(test_song, probs[0]),
             likelihood(test_song, probs[1]),
             likelihood(test_song, probs[2])]
    return np.argmax(probs)

def get_word_probs(occur):
  return (occur.sum(axis=0).astype(float) + 1.0) / (len(occur)+1.0)

def classify(X, y, probs):
        matrix = np.zeros((3,3))
        accCount = 0
        for (i,song) in enumerate(X):
            prediction = predict(song,probs)
            matrix[y[i]][prediction] += 1
            if(y[i] == prediction):
                accCount += 1

        accuracy = float(accCount) / float(len(y))
        return matrix, accuracy
rap_indices = np.random.permutation(len(rap_rows))
rock_indices = np.random.permutation(len(rock_rows))
country_indices = np.random.permutation(len(country_rows))
r_rap = rap_rows[rap_indices]
r_rock = rock_rows[rock_indices]
r_country = country_rows[country_indices]
totalMatrix = np.zeros((3,3))
for i in range(0,10):
  t_rap_probs = get_word_probs(np.concatenate((r_rap[0:(i*100)], r_rap[(i+1)*100:999])))
  t_rock_probs = get_word_probs(np.concatenate((r_rock[0:(i*100)], r_rock[(i+1)*100:999])))
  t_country_probs = get_word_probs(np.concatenate((r_country[0:(i*100)], r_country[(i+1)*100:999])))
  probs = (t_rap_probs,t_rock_probs,t_country_probs)

  testX = np.concatenate((r_rap[i*100:(i+1)*100], r_rock[i*100:(i+1)*100], r_country[i*100:(i+1)*100]))

  rapY = np.full(100,0,dtype=np.int)
  rockY = np.full(100,1,dtype=np.int)
  countryY = np.full(100,2,dtype=np.int)
  testY = np.concatenate((rapY, rockY, countryY))

  matrix, acc = classify(testX, testY, probs)
  totalMatrix += matrix
acc = (totalMatrix[0,0] + totalMatrix[1,1] + totalMatrix[2,2]) / 3000
print (acc)
print (totalMatrix)




