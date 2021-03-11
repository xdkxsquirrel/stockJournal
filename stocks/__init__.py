import pandas as pd
import numpy as np
import dateutil
from edgarScraper import Data
from datetime import date
from os import path


class Stocks:
    def __init__( self, symbol ):
        self.symbol = symbol
        self.edgarParser = Data( self.symbol )
        if path.exists( "stockData\\" + symbol + "Links.csv" ): 
            self.EdgarLinks = pd.read_csv("stockData\\" + self.symbol + "Links.csv")
        else:
            print("Edgar links do not exist")
            self.EdgarLinks = []


    def updateDatabase( self ):
        if path.exists("stockData\\" + self.symbol + "Links.csv"): 
            self.EdgarLinks = pd.read_csv( "stockData\\" + self.symbol + "Links.csv", header=0 )
            financialsDF = pd.DataFrame([])
            todaysDate = date.today()


            # frames = []
            # year = 2014
            # urlDF = self.EdgarLinks.loc[self.EdgarLinks['Year'] == year]
            # url = urlDF['Base Link'] + urlDF['Income Statement']
            # incomeStatement = self.edgarParser.getIncomeStatement( url.values[0], year ) 
            # if incomeStatement[0]:
            #     frames.append(incomeStatement[1])              
            # url = urlDF['Base Link'] + urlDF['Balance Sheet']
            # balanceSheet = self.edgarParser.getBalanceSheet( url.values[0], year )
            # if balanceSheet[0]:
            #     frames.append(balanceSheet[1])
            # url = urlDF['Base Link'] + urlDF['Cashflow Statement']
            # cashflowStatement = self.edgarParser.getCashFlow( url.values[0], year )
            # if cashflowStatement[0]:
            #     frames.append(cashflowStatement[1])
            # if financialsDF.empty:
            #     financialsDF = pd.concat(frames, join='outer').drop_duplicates(subset=['Name'])
            # else:
            #     tempDF = pd.concat(frames, join='outer', sort='True').drop_duplicates(subset=['Name'])
            #     financialsDF = financialsDF.merge(tempDF, how='left', on='Name')
            # print(financialsDF)
            # return


            for i in range(9):
                # year = todaysDate.year - 1 - i
                frames = []
                year = 2019 - i
                urlDF = self.EdgarLinks.loc[self.EdgarLinks['Year'] == year]
                url = urlDF['Base Link'] + urlDF['Income Statement']
                incomeStatement = self.edgarParser.getIncomeStatement( url.values[0], year ) 
                if incomeStatement[0]:
                    frames.append(incomeStatement[1])              
                url = urlDF['Base Link'] + urlDF['Balance Sheet']
                balanceSheet = self.edgarParser.getBalanceSheet( url.values[0], year )
                if balanceSheet[0]:
                    frames.append(balanceSheet[1])
                url = urlDF['Base Link'] + urlDF['Cashflow Statement']
                cashflowStatement = self.edgarParser.getCashFlow( url.values[0], year )
                if cashflowStatement[0]:
                    frames.append(cashflowStatement[1])
                if financialsDF.empty:
                    financialsDF = pd.concat(frames, join='outer').drop_duplicates(subset=['Name'])
                else:
                    tempDF = pd.concat(frames, join='outer', sort='True').drop_duplicates(subset=['Name'])
                    financialsDF = financialsDF.merge(tempDF, how='left', on='Name')

            financialsDF.to_csv("stockData\\" + self.symbol + ".csv", index=False)
        else:
            print("File of Edgar links does not exists: stockData\\" + self.symbol + "Links.csv")