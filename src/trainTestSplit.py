from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import hstack



def getTrainTestSplit(resumeInCSV):
    requiredText = resumeInCSV['cleaned_resume'].values
    requiredTarget = resumeInCSV['Category'].values

    WordFeatures = getWordFeatures(requiredText);


    X_train,X_test,y_train,y_test = train_test_split(WordFeatures,requiredTarget,random_state=0, test_size=0.2)
    return X_train,X_test,y_train,y_test;

def getWordFeatures(requiredText):
    word_vectorizer = TfidfVectorizer(
    sublinear_tf=True,
    stop_words='english',
    max_features=1500)
    word_vectorizer.fit(requiredText)
    WordFeatures = word_vectorizer.transform(requiredText)
    
    print ("Feature completed .....")
    return WordFeatures
