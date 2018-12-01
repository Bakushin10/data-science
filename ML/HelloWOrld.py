from sklearn import tree

##
## 1. Collect Training Data
## 2. Train Classfier
## 3. Make Predictions
##

features = [[140, 1], [130, 1], [150, 0], [130, 0]]
labels = [0,0,1,1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[150,0]]))
