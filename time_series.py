from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import pandas as pd
from datetime import datetime,timedelta

plt.style.use('fivethirtyeight')


dates=[
    datetime(2023,6,24),
    datetime(2023,6,25),
    datetime(2023,6,26),
    datetime(2023,6,27),
    datetime(2023,6,28),
    datetime(2023,6,29),
    datetime(2023,6,30)
]

y=[0,1,3,4,6,5,7]

plt.plot_date(dates,y,linestyle='solid')
#linestyle to give line joining markers some style

plt.gcf().autofmt_xdate()                    #used to rotate dates so enhance presentation applied on figure
#gcf-get current figure used to get figure of our plot
#fmt-format

date_format=mpl_dates.DateFormatter('%b, %d %Y')
plt.gca().xaxis.set_major_formatter(date_format)


data=pd.read_csv("E:\Programs\Python\matplotlib\\time_series_data.csv")
#when we read file it read dates as string to convert it into date
data['Date']=pd.to_datetime(data['Date'])       
data.sort_values('Date',inplace=True)      #inplace is used instead of reinialization after modification
price_data=data['Date']
price_close=data['Close']

plt.plot_date(price_data,price_close,linestyle='solid')
plt.gcf().autofmt_xdate()

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()
plt.show()