
def getResumeInformation(resumeInCSV):
    resumeInCSV['cleaned_resume'] = ''
    resumeInCSV.head()
    print ("Displaying the distinct categories of resume -")
    print (resumeInCSV['Category'].unique())

    print ("Displaying the distinct categories of resume and the number of records belonging to each category -")
    print (resumeInCSV['Category'].value_counts())
    return resumeInCSV
