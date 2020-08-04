import pandas as pd
import quandl
import math
mydata=quandl.get("BSE/BOM539678", authtoken="byvBgHFEdsTmquvd5bnn")
mydata=mydata[['Open','High','Low','Close','WAP','No. of Shares','No. of Trades','Total Turnover']]
mydata['Profit/Share']=(mydata['Total Turnover']/mydata['No. of Shares'])
mydata['Difference']=(mydata['High']-mydata['Low'])
mydata['Close/Open Percentage']=(mydata['Close']-mydata['Open'])/mydata['Close']*100
mydata=mydata[['Profit/Share','Difference','Close/Open Percentage']]

print(mydata.head())
