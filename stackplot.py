from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

minutes=[1,2,3,4,5,6,7,8,9]
player1=[1,1,1,1,2,2,2,3,4]
player2=[1,2,2,3,3,4,4,4,5]
player3=[1,1,1,2,2,2,3,3,3]

#can add colors also
labels=['player1','player2','player3']

plt.stackplot(minutes,player1,player2,player3,labels=labels)

plt.title("Stack plot")
plt.tight_layout()
plt.legend(loc='upper left')            #can also pass co-ordinates as tuple
#plt.legend(loc=(0.07,0.01))
plt.show()