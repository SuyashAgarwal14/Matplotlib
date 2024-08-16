from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')

data=pd.read_csv(r'E:\Programs\Python\matplotlib\hist_data.csv')
ids=data['Responder_id']
ages=data['Age']

bins=[10,20,30,40,50,60,70,80,90,100]

plt.hist(ages,bins=bins,edgecolor='black',
         log=True                                           #to plot values in logarithm
         )

median=55
plt.axvline(median,label="Avg Age",color='red',linewidth=2) #add a vertical line on a plot

plt.legend()
plt.title('Histogram')
plt.xlabel('Ages')
plt.ylabel("Total Respondance")
plt.tight_layout()
plt.show()