from matplotlib import pyplot as plt
import seaborn as sns

#Loading Dataset
tips = sns.load_dataset('tips')

#sns.set_style('darkgrid')
#sns.despine(left=False, bottom=True, top=False)
'''
1. Options for set_style are : darkgrid, whitegrid, dark, white, ticks
2. Despine removes the upper and the right margins of the plot 
3. Documentation for pallete can be found at : https://matplotlib.org/tutorials/colors/colormaps.html
'''

sns.countplot(x='sex', data=tips, hue='sex', palette='viridis')

plt.show()