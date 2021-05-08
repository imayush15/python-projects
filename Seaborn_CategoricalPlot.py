from matplotlib import pyplot as plt
import seaborn as sns

#Loading Dataset
tips = sns.load_dataset('tips')
#print(tips.head())

#sns.barplot(x='smoker', y='total_bill', data=tips)

#sns.countplot(x='smoker', data=tips) #Counts the number of occurences

#sns.boxplot(x='day',y='total_bill',data=tips, hue='sex')

#sns.violinplot(x='day', y='total_bill', data=tips, hue='smoker',palette='coolwarm', split=True,)

#sns.stripplot(x='smoker', y='tip', data=tips, hue='sex', palette='coolwarm',jitter=True, split=True)
#A Scatter plot is plotted

#sns.swarmplot(x='day', y='total_bill', data=tips)
#Scatter plot in shape of voilin plot

#sns.catplot(x='day', y='total_bill', data=tips)
#http://seaborn.pydata.org/generated/seaborn.catplot.html?highlight=catplot#seaborn.catplot
#for help refer the above link


plt.show()