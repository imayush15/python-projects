from matplotlib import pyplot as plt
import seaborn as sns

tips = sns.load_dataset('tips')
#print(tips.head())
#sns.distplot(tips['tip'])
#sns.jointplot(x='total_bill', y='tip', data=tips, kind='kde')
sns.pairplot(tips, hue='sex')
#sns.rugplot(tips['total_bill'])
#sns.kdeplot(tips['total_bill'])

plt.show()
