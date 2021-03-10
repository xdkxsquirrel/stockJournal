import pandas as pd
import numpy as np
import dateutil
from edgarScraper import Data
from datetime import date
from os import path


class Stocks:
    def __init__( self, symbol ):
        self.symbol = symbol
        if path.exists( "stockData\\" + symbol + ".csv" ): 
            self.edgarParser = Data( self.symbol )
            #self.data = pd.read_csv( "stockData\\" + self.symbol + ".csv", header=1 )
            # self.data = pd.DataFrame( empty )
            todaysDate = date.today( )
            year = todaysDate.year - 1
            self.EdgarLinks = pd.read_csv("stockData\\" + self.symbol + "Links.csv")
        else:
            pass


    def updateDatabase( self ):
        if path.exists("stockData\\" + self.symbol + "Links.csv"): 
            self.EdgarLinks = pd.read_csv( "stockData\\" + self.symbol + "Links.csv", header=0 )
            financialsDF = []
            todaysDate = date.today()
            year = 2019
            urlDF = self.EdgarLinks.loc[self.EdgarLinks['Year'] == year]
            url = urlDF['Base Link'] + urlDF['Income Statement']
            incomeStatement = self.edgarParser.getIncomeStatement( url.values[0], year )
            url = urlDF['Base Link'] + urlDF['Balance Sheet']
            balanceSheet = self.edgarParser.getBalanceSheet( url.values[0], year )
            url = urlDF['Base Link'] + urlDF['Cashflow Statement']
            cashflowStatement = self.edgarParser.getCashFlow( url.values[0], year )
            if cashflowStatement[0]:
                
            
            financialsDF = pd.DataFrame(financials, columns=['Name', year])

            for i in range(8):
                # year = todaysDate.year - 1 - i
                financials = []
                year = 2018 - i
                urlDF = self.EdgarLinks.loc[self.EdgarLinks['Year'] == year]
                url = urlDF['Base Link'] + urlDF['Income Statement']
                incomeStatement = self.edgarParser.getIncomeStatement( url.values[0], year )
                if incomeStatement[0]:
                    for row in incomeStatement[1]:
                        financials.append([row[0], row[1]])
                url = urlDF['Base Link'] + urlDF['Balance Sheet']
                balanceSheet = self.edgarParser.getBalanceSheet( url.values[0], year )
                if balanceSheet[0]:
                    for row in balanceSheet[1]:
                        financials.append([row[0], row[1]])
                url = urlDF['Base Link'] + urlDF['Cashflow Statement']
                cashflowStatement = self.edgarParser.getCashFlow( url.values[0], year )
                if cashflowStatement[0]:
                    for row in cashflowStatement[1]:
                        financials.append([row[0], row[1]])
                financialsDF = financialsDF.merge(pd.DataFrame(financials, columns=['Name', year]), how='left', on='Name')


            financialsDF.to_csv("stockData\\" + self.symbol + ".csv", index=False)
        else:
            print("File of Edgar links does not exists: stockData\\" + symbol + "Links.csv")