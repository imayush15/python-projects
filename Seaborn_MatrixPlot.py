from matplotlib import pyplot as plt
import seaborn as sns

#Loading Dataset
tips = sns.load_dataset('tips')
flights = sns.load_dataset('flights')

tc = tips.corr()
fc = flights.pivot_table(values='passengers', index='month', columns='year')

#print(fc)
#corr() gives us the matrix form for the plotting of heatmap

#sns.heatmap(fc)
sns.clustermap(fc)

plt.show()