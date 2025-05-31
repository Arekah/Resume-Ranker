import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
import string
from wordcloud import WordCloud
from src.cleanCSV import cleanData
import matplotlib.pyplot as plt;

def wordCloudLogic(resumeInCSV):
    oneSetOfStopWords = set(stopwords.words('english')+['``',"''"])
    Sentences = resumeInCSV['Resume'].values
    totalWords , cleanedSentences = getTotalWords(Sentences , oneSetOfStopWords);
    showCommonWords(totalWords);
    showWordCloud(cleanedSentences);
        



def showWordCloud(cleanedSentences):
    wc = WordCloud().generate(cleanedSentences)
    plt.figure(figsize=(15,15))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    
def showCommonWords(totalWords):
    wordfreqdist = nltk.FreqDist(totalWords)
    mostcommon = wordfreqdist.most_common(50)
    print(mostcommon)

def getTotalWords(Sentences , oneSetOfStopWords):
    totalWords =[]
    cleanedSentences = ""
    for i in range(0,160):
        cleanedText = cleanData(Sentences[i])
        cleanedSentences += cleanedText
        requiredWords = nltk.word_tokenize(cleanedText)
        for word in requiredWords:
            if word not in oneSetOfStopWords and word not in string.punctuation:
                totalWords.append(word)
    return totalWords , cleanedSentences