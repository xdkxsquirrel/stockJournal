from transactions import Transactions
from stocks import Stocks

import pandas as pd

#import PySimpleGUI as sg
#https://realpython.com/pysimplegui-python/

# roth = Transactions("transactionData\\roth.csv")
# growth = Transactions("transactionData\\growth.csv")


# print(growth.depositData)
# print(growth.data[(growth.data['Symbol'] == 'T') & (growth.data['Action'] == 'Buy')])

# totalDeposited = 0.0
# for idx in reversed(growth.data.index):
#     if growth.data.loc[idx]['Action'] is 'Journal':
#         growth.data.loc[idx]['Amount'] = growth.data.loc[idx]['Amount'].str.replace('$','')
#         growth.data.loc[idx]['Amount'] = growth.data.loc[idx]['Amount'].str.replace(',','')
#         totalDeposited = totalDeposited + float(growth.data.loc[idx]['Amount'])
# print(growth.getTransactionsOfStock('T'))

# print(growth.getTotalSum() + 12794.32)

INTC = Stocks( "intc" )
INTC.updateDatabase( ) 