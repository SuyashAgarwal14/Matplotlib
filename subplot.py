from matplotlib import pyplot as plt
import pandas as pd


plt.style.use("seaborn") 

data=pd.read_csv("E:\Programs\Python\matplotlib\line_filling_data.csv")
ages=data['Age']
dev_salary=data['All_Devs']
py_salary=data['Python']
jsv_salary=data['JavaScript']

"""Uptil now we have used pyplot object that has been imported,this is called stateful 
This object holds the current state of the plot like figure and axes we are working with
Figure is container holding our plot whole window that appears showing our plot 
Axes is our actual plot so a figure can have multiple plot
Like we have seen earlier the use of gcf and gca we can switch between different one so thats the stateful way
but object oriented approach is way better when working with multiple figure and axis thus subplots() is used
To implement this we instantiate figure and axes
"""

#subplots create a figure then specify certain number of rows and columns of axes
#by default it is 1x1(1 row 1 column) which is simply one axes
#basicalyy subplots is used to to split our plots
#subplots(nrows=2,ncols=2)      implies 4 axes
#(ax1,ax2) is unpacking of axes in order to instantiate different axes to different variable

fig,(ax1,ax2)=plt.subplots(nrows=2,ncols=1,sharex=True,sharey=True)
#sharex- labels x axis of bottom axes only, for two rows
#sharey- labels y axis of left axes only, for two columns
#one figure with two different plots


#if we want to plot our axes on different figures
fig1,ax1=plt.subplots()
fig2,ax2=plt.subplots()


ax1.plot(ages,dev_salary,linestyle='--',label='All Devs')
ax2.plot(ages,py_salary,label='Python')
ax2.plot(ages,jsv_salary,label='JavaScript')

ax1.legend()
ax1.set_ylabel("Salary")
ax1.set_title("Salary (Rupees) by Age")

ax2.legend()
ax2.set_xlabel("Age")
ax2.set_ylabel("Salary")

plt.tight_layout()
plt.show()