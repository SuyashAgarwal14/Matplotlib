#scatterplot is used to show relation between two sets of values
from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('fivethirtyeight')


x=[5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
y=[7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]
colors=[7,5,9,7,5,7,2,5,3,7,1,2,8,1,9,2,5,6,7,5]
sizes=[10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]

plt.scatter(x,y,s=sizes,c=colors,cmap='Greens',edgecolor='Black',linewidth=1,alpha=0.5)
#s stands for size of dots can pass a value(like s=60) or a list of sizes representing points size
#c stands for color we can pass direct color(like c='green') or list of numbers 
#cmap defines what shades of color used for the points when we want different color points
#marker='X',     #gives marker for the points(shape of the points)
#edgecolor gives color to the edges of the point
#linewidth tells us width of the edge 
#alpha gives transparency percentage
            
cbar=plt.colorbar()                         #to add color bar 
cbar.set_label("Satisfaction")


data=pd.read_csv("E:\Programs\Python\matplotlib\scatter_data.csv")
view_count=data['view_count']
likes=data['likes']
ratio=data['ratio']

plt.scatter(view_count,likes,c=ratio,cmap='summer',edgecolor='Black',linewidth=1,alpha=0.5)

cbar=plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

plt.xscale('log')                           #change scale of axis 
plt.yscale('log')

plt.title('Trending')
plt.xlabel('View Count')
plt.ylabel("Total Likes")

plt.tight_layout()
plt.show()