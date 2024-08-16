import csv
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter
import pandas as pd 

plt.style.use('fivethirtyeight')
#with open('E:\Programs\Python\matplotlib\horizontal_bar_data.csv') as csv_file:
    #csv_reader=csv.DictReader(csv_file)        OR
data=pd.read_csv("E:\Programs\Python\matplotlib\horizontal_bar_data.csv")

language_counter=Counter()
ids=data['Responder_id']
responses=data['LanguagesWorkedWith']

for each in responses:
    language_counter.update(each.split(";"))
    
language=[]
popularity=[]

for item in language_counter.most_common(15):
    language.append(item[0])
    popularity.append(item[1])

language.reverse()
popularity.reverse()
plt.barh(language,popularity)   #barh is used for horizontal bar graph(simple bar is vertical bar graph)
plt.xlabel("People use")
plt.title('Most popular language')


#stcked horizontal bar-  can be done for bar graph also
df= pd.DataFrame(np.random.uniform(size=(6,4)),index=["one","two","three","four","five","six"],columns=pd.Index(["A","B","C","D"],name="Genus"))
df.plot.barh(stacked=True, alpha=0.5)

plt.tight_layout()
plt.show()