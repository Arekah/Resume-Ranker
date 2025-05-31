import re

def cleanData(resumeInCSV):
    resumeText = re.sub('http\S+\s*', ' ', resumeInCSV)  # remove URLs
    resumeText = re.sub('RT|cc', ' ', resumeInCSV)  # remove RT and cc
    resumeText = re.sub('#\S+', '', resumeInCSV)  # remove hashtags
    resumeText = re.sub('@\S+', '  ', resumeInCSV)  # remove mentions
    resumeText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', resumeInCSV)  # remove punctuations
    resumeText = re.sub(r'[^\x00-\x7f]',r' ', resumeInCSV) 
    resumeText = re.sub('\s+', ' ', resumeInCSV)  # remove extra whitespace
    return resumeText