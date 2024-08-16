from matplotlib import pyplot as plt
import pandas as pd

data=pd.read_csv("E:\Programs\Python\matplotlib\line_filling_data.csv")
ages=data['Age']
dev_salary=data['All_Devs']
py_salary=data['Python']
jsv_salary=data['JavaScript']
median=57000

plt.plot(ages,dev_salary,linestyle='--',label='All Devs')
plt.plot(ages,py_salary,label='Python')

#fill_between is used to fill the area under the line
plt.fill_between(ages,py_salary,
            median,                            #to fill upto median only can use parameter of another line to fill between the lines
            where=py_salary>median,            #aplly conditions o fill
            interpolate=True,                  #to make sure certain x regions are not clipped and regions are filled correctly
            alpha=0.25,label='Above Avg')      #alpha is how much can we see through it

plt.fill_between(ages,py_salary,median,where=py_salary<=median,interpolate=True,
                 color='red',alpha=0.25,label='Below Avg')

plt.title('Salary by Age')
plt.xlabel("Age")
plt.ylabel("Salary")

plt.legend()
plt.tight_layout()
plt.show()