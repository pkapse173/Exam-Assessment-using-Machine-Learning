
from rake_nltk import Rake
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv
import sys
from pymongo import MongoClient
m_client = MongoClient('localhost', 27017)
db = m_client.QandA
collection = db. preprocessed
collection.delete_many({})

reload (sys)
sys.setdefaultencoding('utf8')
r = Rake()
stop_words = set(stopwords.words('english'))
with open('../data/shivam. csv') as csvfile:
        reader = csv.reader(csvfile,delimiter=',')
        for row in reader:
                if (row[1]!="" and row[1]!="Question"):
                          ques=row[1].decode('ascii','ignore')
                          text=row[2].decode('ascii','ignore')
                          ans=row[2].decode('ascii','ignore')
                          r.extract_keywords_from_text(text)
                          word_tokens= word_tokenize(text)
                          stopwords=[]
                          keywords=r.get_ranked_phrases( ) # To get keyword phrases ranked highest to lowest.
                          for w in word tokens:
                                  if w in stop_words:
                                         if w not in stopwords:
                                                 stopwords.append(w)
                          collection.insert_one({"Status":0,"Question":ques,"Answer":text,"Keywords":keywords,"Stopwords":stopwords,"Difficulty":row[7]})

