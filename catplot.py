import seaborn as sns
from matplotlib import pyplot as plt

tips=sns.load_dataset('tips')

tips["tip_pct"]=tips["tip"]/(tips["total_bill"]-tips["tip"])

sns.catplot(x="day",y="tip_pct",hue="time",col="smoker",kind="bar",data=tips[tips.tip_pct<1])

sns.catplot(x="day",y="tip_pct",row="time",col="smoker",kind="bar",data=tips[tips.tip_pct<1])

plt.show()