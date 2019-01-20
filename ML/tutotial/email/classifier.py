#import pandas as pd
import nltk
from nltk.corpus import stopwords
import pandas
import numpy as np
import codecs
import unicodedata
import glob
import os

class MailClassifier:
    def __init__(self):
        self.TRAIN_DIR = "train-mails/*.txt"
        self.TEST_DIR =  "test-mails/*.txt"
        self.stopwords = set(stopwords.words('english'))
    
    def getWordFreqDist(self):
        """
            get the frequency distribution of the training emails.
        """
        text_all = []
        for eachFile in glob.glob(self.TRAIN_DIR):
            with codecs.open(eachFile,"r",encoding='utf-8', errors='ignore') as file:
                    print("opening...", eachFile)
                    """
                        add addtional trimming to increase the quality of the FreqDist
                    """
                    text = file.read()
                    text = unicodedata.normalize('NFKD', text).encode('ascii','ignore') # convert unicode to string
                    token = nltk.word_tokenize(text)
                    text_trimmed = [t for t in token if t not in self.stopwords]
                    text_all += text_trimmed
                    #text = text + file.read()
        freqDist = nltk.FreqDist(text_all).most_common(3000)
        return freqDist
        #print(freqDist)

    def extract_features(self, mail_dir, dictionary):
        """
            create numpy array of features.
            the size of the array is [test_size, 3000]. 
            each array will have the word frequency of 3000 most_common words
        """
        files = [os.path.join(mail_dir,fi) for fi in os.listdir(mail_dir)]
        features_matrix = np.zeros((len(files),3000))
        train_labels = np.zeros(len(files))
        count = 0;
        docID = 0;
        print(features_matrix)
        print(train_labels)
        print(features_matrix.shape)
        print(train_labels.shape)
        
        for fil in files:
            with open(fil) as fi:
                for i,line in enumerate(fi):
                    if i == 2:
                        words = line.split()
                        for word in words:
                            wordID = 0
                            for i,d in enumerate(dictionary):
                                if d[0] == word:
                                    wordID = i
                                    features_matrix[docID,wordID] = words.count(word)
                        train_labels[docID] = 0;
                        filepathTokens = fil.split('/')
                        lastToken = filepathTokens[len(filepathTokens) - 1]
                        if lastToken.startswith("spmsg"):
                            train_labels[docID] = 1;
                            count = count + 1
                        docID = docID + 1
        print(features_matrix)
        print(train_labels)
        print(features_matrix.shape)
        print(train_labels.shape)
        return features_matrix, train_labels

if __name__ == "__main__":
    mail_dir = "train-mails"

    m = MailClassifier()
    dictonary = m.getWordFreqDist()
    m.extract_features(mail_dir, dictonary)



