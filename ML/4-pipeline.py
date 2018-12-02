# a pipeline is just when you're chaining together different operations in the classification. 

#import a dataset
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
Y = iris.target

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = .5)

# # method 1
# from sklearn import tree
# my_classifier = tree.DecisionTreeClassifier()

#method 2
from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train, Y_train)

predictions = my_classifier.predict(X_test)
print(predictions)

# to Calculate the accuracy of your data
from sklearn.metrics import accuracy_score
print (accuracy_score(Y_test, predictions))
