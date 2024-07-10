
import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

#nltk.download('punkt') # if necessary...

stemmer = nltk.stem.porter.PorterStemmer( )
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]
	
'''remove punctuation, lowercase, stem'''
def normalize (text):
    return stem_tokens(nltk.word_tokenize(text.lower( ).translate(remove_punctuation_map)))

vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

def cosine_sim(text1,text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[O,1]

ans="BE student should attend regular college"
ans1="regular college should be attended by rahul"
#ans3="Vaseline is a trademark of unilever"

ans2="everyone from BE should enjoy attending regular college"

print str (cosine_sim(ans,ans1)*100)+" % Similar"
print str (cosine_sim(ans,ans2)*100)+" % Similar"
