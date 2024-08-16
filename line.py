from matplotlib import pyplot as plt
plt.style.use("ggplot")                         #use different plot styles can see all available styles by plt.style.available attribute
#plt.xkcd() change style of boundary

ages_x=[25,26,27,28,29,30,31,32,33,34,35]
dev_y=[38000,40000,42000,44000,48000,53000,55000,56000,60000,62000,65000]

plt.plot(ages_x,dev_y,color="b",linestyle="--",marker=".",linewidth=3,label="All Devs") #to plot line graph
#for color hex numbers can also be used to have broader range of colors

py_dev_y=[45000,48000,51000,54000,60000,63000,66000,70000,73000,78000,80000]
plt.plot(ages_x,py_dev_y,label="Python")

plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Salary (Rupees) by Age")

plt.legend()                                    #to apply labels
plt.grid(True)
plt.tight_layout()                              #to remove any kind of gap(padding)
#plt.savefig("plot.png")                        #to save plot as an image
plt.show()