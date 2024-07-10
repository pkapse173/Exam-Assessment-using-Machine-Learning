
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

documentA = 'My name is Pranav Kapse'
documentB = 'My name is Rahul Nagpal'

bagOfWordsA = documentA.split(' ')
bagOfWordsB = documentB.split(' ')

uniqueWords = set(bagOfWordsA).union(set(bagOfWordsB))

numOfWordsA =dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsA:
    numOfWordsA[word] +=1
numOfWordsB = dict.fromkeys(uniqueWords, 0)
for word in bagOfWordsB:
    numOfWordsB[word] += 1

from nltk.corpus import stopwords
stopwords.words('english')

def computeTF(wordDict, bagOfWords):
    tfDict = {}
    bagOfWordsCount = len(bagOfWords)
    for word, count in wordDict.items( ):
        tfDict[word] = count / float(bagOfWordsCount)
    return tfDict

tfA = computeTF(numOfWordsA, bagOfWordsA)
tfB = computeTF (numOfWordsB, bagOfWordsB)

print(tfA)
print(tfB)

def computeIDF(documents):
    import math
    N = len(documents)

    idfDict = dict.fromkeys(documents[0].keys( ), 0)
    for document in documents:
        for word, val in document.items( ):
            if val > 0:
                idfDict[word] += 1
    for word, val in idfDict.items( ):
        idfDict[word] = math. log(N / float (Val))
    return idfDict

idfs = computeIDF([numOfWordsA, numOfWordsB])

print (idfs)
def computeIDF(tfBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items( ):
        tfidf[word] = val * idfs[word]
    return tfidf

tfidf = computeTFIDF(tfA, idfs)

print (tfA)
print (tfB)

def computeIDF(documents):
    import math
    N = len (documents)

    idfDict = dict.fromkeys(documents[0].keys( ), 0)
    for document in documents:
        for word, val in document.items( ):
            if val > 0:
                idfDict [word] += 1

    for word, val in idfDict.items( ):
        idfDict[word] = math.log(N / float (Val))
    return idfDict

idfs = computeIDF([numOfWordsA, numOfWordsB])

print (idfs)
def computeTFIDF(ffBagOfWords, idfs):
    tfidf = {}
    for word, val in tfBagOfWords.items( ):
        tfidf[word] = val * idfs[word]
    return tfidf

tfidfA = computeTFIDF(tfA, idfs)
tfidfB = computeTFIDF(tfB, idfs)
df = pd.DataFrame([tfidfA, tfidfB])
print (tfidfA)
print (tfidfB)
print (df)

vectorizer = TfidfVectorizer( )
vectors = vectorizer.fit_transform([documentA, documentB])
feature_names = vectorizer.get_feature_names( )
dense = vectors.todense()
denselist = dense.tolist( )
df = pd.DataFrame (denselist, columns=feature_names)

print (df)


