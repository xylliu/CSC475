import matplotlib.pyplot as plt
import pickle 
import numpy as np

data = np.load('/Users/llicht/Documents/csc475_asn3_data/data.npz')
a = data['arr_0']
a[a > 0] = 1
labels = np.load('/Users/llicht/Documents/csc475_asn3_data/labels.npz')
labels = labels['arr_0']
dictionary = pickle.load(open('/Users/llicht/Documents/csc475_asn3_data/dictionary.pck','rb'), encoding='latin1')
word_indices = [  41, 1465,  169,  217, 1036,  188,  260,  454,  173,  728,  163,
        151,  107,  142,   90,  141,  161,  131,   86,   73,  165,  133,
         84,  244,  153,  126,  137,  119,   80,  224]
words = [dictionary[r] for r in word_indices]

ra_rows = a[0:1000,:]
ro_rows = a[1000:2000,:]
co_rows = a[2000:3000,:] 

word_probs_ra = (ra_rows.sum(axis=0).astype(float) + 1.0) / (len(ra_rows)+1.0)
word_probs_ro = (ro_rows.sum(axis=0).astype(float) + 1.0) / (len(ro_rows)+1.0)
word_probs_co = (co_rows.sum(axis=0).astype(float) + 1.0) / (len(co_rows)+1.0)

print('rap')
for w in zip(word_probs_ra, words): 
    print(w)
print('rock')
for h in zip(word_probs_ro, words): 
    
    print(h)
print('country')
for y in zip(word_probs_co, words): 
    print(y)

def likelihood(test_song, word_probs_for_genre): 
    probability_product = 1.0 
    for (i,w) in enumerate(test_song): 
        if (w==1): 
            probability = word_probs_for_genre[i]
        else: 
            probability = 1.0 - word_probs_for_genre[i]
        probability_product *= probability 
    return probability_product

def predict(test_song): 
    scores = [likelihood(test_song, word_probs_ra), 
             likelihood(test_song, word_probs_ro),
             likelihood(test_song, word_probs_co)]
    labels = ['rap', 'rock', 'country']
    return labels[np.argmax(scores)]

track_id = np.random.randint(1000)
print("Random track id", track_id)
test_song = co_rows[track_id]
print(predict(test_song))

def predict_set(test_set, ground_truth_label): 
    score = 0 
    for r in test_set: 
        if predict(r) == ground_truth_label: 
            score += 1
    return score / 10.0 

print("Rap accuracy% = ", predict_set(ra_rows, 'rap'))
print("Rock accuracy% = ", predict_set(ro_rows, 'rock'))
print("Country accuracy% = ", predict_set(co_rows, 'country'))

