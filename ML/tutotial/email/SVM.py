import nltk
from nltk.corpus import stopwords
import pandas as pd
import numpy as np
import codecs
import unicodedata
import glob
import os
from sklearn import svm
from sklearn.metrics import accuracy_score

class MailClassifier:

    SPAM = "spmsg"

    def __init__(self):
        self.stopwords = set(stopwords.words('english'))
    
    def getWordFreqDist(self, TRAIN_DIR):
        """
            get the frequency distribution of the training emails.
        """
        text_all = []
        numOfFiles = 0
        trimmed_text_list = [] # list of trimmed_text that is used when creating the feature
        file_name_list = [] # list of training files 
        
        for eachFile in glob.glob(TRAIN_DIR):
            with codecs.open(eachFile,"r",encoding='utf-8', errors='ignore') as file:
                text = file.read()
                trimmed_text = self.trimText(text)
                trimmed_text_list.append(trimmed_text)
                file_name_list.append(eachFile)
                text_all += trimmed_text
            numOfFiles += 1

        freqDist = nltk.FreqDist(text_all).most_common(3000)
        self.numOfFiles = numOfFiles
        self.trimmed_text_list = trimmed_text_list
        self.file_name_list = file_name_list
        return freqDist

    def extract_features(self, mail_dir, dictionary):
        """
            create numpy array of features.
            the size of the array is [test_size, 3000]. 
            each array will have the word frequency of 3000 most_common words
        """
        features_matrix = np.zeros((self.numOfFiles,3000))
        train_labels = np.zeros(self.numOfFiles)

        for i in range(len(self.trimmed_text_list)):
            text = self.trimmed_text_list[i]
            fdist = nltk.FreqDist(text)
            train_labels[i] = self.checkFile(self.file_name_list[i])
            for word, word_freq in fdist.items():
                for j, word_dic in enumerate(dictionary):
                    if word == word_dic[0]:
                        features_matrix[i,j] = word_dic[1]
            # print(features_matrix[i])

        return features_matrix, train_labels
    
    def trimText(self, text):
        text = unicodedata.normalize('NFKD', text).encode('ascii','ignore') # convert unicode to string
        token = nltk.word_tokenize(text)
        trimmed_text = [t for t in token if t not in self.stopwords]
        return trimmed_text
    
    def checkFile(self, file):
        if self.SPAM in file:
            return 1
        else:
            return 0

if __name__ == "__main__":
    TRAIN_DIR = "train-mails/*.txt"
    TEST_DIR =  "test-mails/*.txt"

    m = MailClassifier()
    dictionary = m.getWordFreqDist(TRAIN_DIR)
    features_matrix, labels = m.extract_features(TRAIN_DIR, dictionary)
    test_feature_matrix, test_labels = m.extract_features(TEST_DIR, dictionary)

    model = svm.SVC()
    model.fit(features_matrix, labels)
    predicted_labels = model.predict(test_feature_matrix)

    print("accuracy score : ")
    print(accuracy_score(test_labels, predicted_labels))
