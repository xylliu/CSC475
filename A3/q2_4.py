import numpy as np
import pickle
from sklearn.naive_bayes import BernoulliNB
from sklearn import metrics
def generateRandomLyrics(word_probs, words):

  indices = np.random.permutation(len(words))
  r_probs = word_probs[indices]
  r_words = np.array(words)[indices]

  s = ""
  r = np.random.rand(30)
  for (i,word) in enumerate(r_words):
    if r[i] < r_probs[i]:
      s += word + " "
  return s
urn (occur.sum(axis=0).astype(float) + 1.0) / (len(occur)+1.0)

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

for i in range(0,5):
  print ("rap: " + generateRandomLyrics(word_probs_rap, words))
  print ("rock: " + generateRandomLyrics(word_probs_rock, words))
  print ("country: " + generateRandomLyrics(word_probs_country, words))



