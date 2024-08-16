from matplotlib import pyplot as plt
import seaborn as sns

dataset=sns.load_dataset('tips')

sns.pairplot(dataset,hue='sex')

plt.show()