from sklearn import metrics

def EvaluateModel(clf , X_train , y_train , X_test , y_test):
    prediction = clf.predict(X_test)

    print('Accuracy of KNeighbors Classifier on training set: {:.2f}'.format(clf.score(X_train, y_train)))
    print('Accuracy of KNeighbors Classifier on test set: {:.2f}'.format(clf.score(X_test, y_test)))

    print("\n Classification report for classifier %s:\n%s\n" % (clf, metrics.classification_report(y_test, prediction))) 

    return prediction;
    