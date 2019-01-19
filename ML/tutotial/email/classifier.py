#import pandas as pd
import nltk
from nltk.corpus import stopwords
import pandas
import numpy
import codecs
import unicodedata
import glob

class MailClassifier:
    def __init__(self):
        self.TRAIN_DIR = "train-mails/*.txt"
        self.TEST_DIR =  "test-mails/*.txt"
        self.stopwords = set(stopwords.words('english'))
        print(self.stopwords)
    
    def readFile(self):
        text_all = []
        for eachFile in glob.glob(self.TRAIN_DIR):
            with codecs.open(eachFile,"r",encoding='utf-8', errors='ignore') as file:
                    print("opening...", eachFile)
                    text = file.read()
                    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore') # convert unicode to sting
                    token = nltk.word_tokenize(text)
                    text_trimmed = [t for t in token if t not in self.stopwords]
                    text_all += text_trimmed
                    #text = text + file.read()
        freqDist = nltk.FreqDist(text_all).most_common(3000)
        print(freqDist)

if __name__ == "__main__":
    m = MailClassifier() 
    m.readFile()



