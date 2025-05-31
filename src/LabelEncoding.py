from sklearn.preprocessing import LabelEncoder

def getLabelEncodedData(resumeInCSV):
    var_mod = ['Category']
    le = LabelEncoder()
    for i in var_mod:
        resumeInCSV[i] = le.fit_transform(resumeInCSV[i])
    return resumeInCSV;