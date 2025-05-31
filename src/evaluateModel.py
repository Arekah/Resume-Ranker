from sklearn import metrics

def EvaluateModel(clf , X_train , y_train , X_test , y_test):
    prediction = clf.predict(X_test)


    return prediction;
    