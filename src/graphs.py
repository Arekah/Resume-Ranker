import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import numpy as np;

def showCountPlot(resumeInCSV):
    plt.figure(figsize=(15,15))
    plt.xticks(rotation=90)
    sns.countplot(y="Category", data=resumeInCSV)


def showGridSpec(resumeInCSV):
    targetCounts = resumeInCSV['Category'].value_counts()
    targetLabels  = resumeInCSV['Category'].unique()
    # Make square figures and axes
    plt.figure(1, figsize=(25,25))
    the_grid = GridSpec(2, 2)


    cmap = plt.get_cmap('coolwarm')
    colors = [cmap(i) for i in np.linspace(0, 1, 6)]
    plt.subplot(the_grid[0, 1], aspect=1, title='CATEGORY DISTRIBUTION')

    source_pie = plt.pie(targetCounts, labels=targetLabels, autopct='%1.1f%%', shadow=True, colors=colors)
    plt.show()