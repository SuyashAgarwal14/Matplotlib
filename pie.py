from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices=[10,20,30,90]
labels=['Aap','Congress','BSP','BJP']
colors=['Grey','Green','Blue','#e85f10']
explode=[0.1,0,0,0]     #explode means how much it explodes out in this case it is 10% of radius of chart

#autopct='%1.1f%%' is used to add percentage to the chart,
plt.pie(slices,labels=labels,colors=colors,explode=explode,shadow=True,autopct='%1.1f%%',
        wedgeprops={'edgecolor':'black'})

plt.title('Pie Chart')
plt.tight_layout()
plt.show()