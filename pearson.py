import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

df = pd.read_csv('iris.csv',
                 header=0,
                 encoding='iso-8859-15',
                 names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])

sns.jointplot(df['sepal length'], df['petal length']).annotate(stats.pearsonr) # pearson correlation coefficient 1 or 0

plt.show()
