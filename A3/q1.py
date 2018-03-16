from sklearn.datasets import load_svmlight_file
from sklearn import metrics
from sklearn import tree
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import LogisticRegression

data, a = load_svmlight_file("q1.libsvm")

model1 = tree.DecisionTreeClassifier()
dtc = model1.fit(data, a)

print(dtc)

expected1 = a
predicted1 = dtc.predict(data)

print(metrics.classification_report(expected1, predicted1))
print("Confusion Matrix:")
print(metrics.confusion_matrix(expected1, predicted1))
print("----")

model2 = BernoulliNB()
gnb = model2.fit(data, a)

print(gnb)

expected2 = a
predicted2 = gnb.predict(data)

print(metrics.classification_report(expected2, predicted2))
print("Confusion Matrix:")
print(metrics.confusion_matrix(expected2, predicted2))
print("----")

model3 = LogisticRegression()
reg = model3.fit(data, a)

expected3 = a
predicted3 = reg.predict(data)

print(metrics.classification_report(expected2, predicted2))
print("Confusion Matrix:")
print(metrics.confusion_matrix(expected2, predicted2))
print("----")