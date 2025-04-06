import numpy as np
import random
stock_prices=  np.random.randint(100, 500, (30,5))
print(stock_prices)
li_avg_stocks=np.mean(stock_prices,axis=0)
li_avg_stocks_arr=np.array(li_avg_stocks)
print(li_avg_stocks)
max_day=np.max(stock_prices)
min_price=np.min(stock_prices)
print((stock_prices-min_price)/(max_day-min_price))
date_li=np.unravel_index(np.argmax(stock_prices),stock_prices.shape)
print("Highest price recorded : ",max_day,"at Day",date_li[0]+1,"company",date_li[1]+1)
col_difference=np.diff(stock_prices,axis=0)
print(col_difference)
arr=col_difference<-200
print(col_difference[arr])