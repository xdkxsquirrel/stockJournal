import pandas as pd
import numpy as np
import dateutil


# columns = ['Year', 'Base Link', 'Balance Sheet', 'Income Statement', 'Cashflow Statement']
# data = []
# data.append(['2019', 'https://www.sec.gov/Archives/edgar/data/50863/000005086320000011/', 'R4.htm', 'R2.htm', 'R6.htm'])
# data.append(['2018', 'https://www.sec.gov/Archives/edgar/data/50863/000005086319000007/', 'R4.htm', 'R2.htm', 'R6.htm'])
# data.append(['2017', 'https://www.sec.gov/Archives/edgar/data/50863/000005086318000007/', 'R4.htm', 'R2.htm', 'R6.htm'])
# data.append(['2016', 'https://www.sec.gov/Archives/edgar/data/50863/000005086317000012/', 'R4.htm', 'R2.htm', 'R6.htm'])
# data.append(['2015', 'https://www.sec.gov/Archives/edgar/data/50863/000005086316000105/', 'R4.htm', 'R2.htm', 'R6.htm'])
# data.append(['2014', 'https://www.sec.gov/Archives/edgar/data/50863/000005086315000015/', 'R4.htm', 'R2.htm', 'R6.htm'])
# data.append(['2013', 'https://www.sec.gov/Archives/edgar/data/50863/000005086314000020/', 'R4.htm', 'R2.htm', 'R6.htm'])
# data.append(['2012', 'https://www.sec.gov/Archives/edgar/data/50863/000119312513065416/', 'R4.htm', 'R2.htm', 'R6.htm'])
# data.append(['2011', 'https://www.sec.gov/Archives/edgar/data/50863/000119312512075534/', 'R4.htm', 'R2.htm', 'R6.htm'])
# data.append(['2010', 'https://www.sec.gov/Archives/edgar/data/50863/000095012311015783/', 'R4.htm', 'R2.htm', 'R6.htm'])

# df = pd.DataFrame( data, columns=columns )
# df.to_csv( 'stockData/intcLinks.csv', index=False )


class Stocks:

    def __init__( self, odoFileName ):
        self.dataAggrigate = {'Market':'first','Type':'first','Price':'mean','Amount':'sum','Total':'sum','Fee':'sum','Acc':'first'}
        self.data = pd.read_csv(odoFileName, header=1)
        self.data = self.data[self.data['Action'] != 'Bank Interest']
        self.depositData = self.data[self.data['Action'] == 'Journal']
        self.data = self.data[self.data['Action'] != 'Journal']
        #self.data['Date'] = self.data['Date'].apply(dateutil.parser.parse, dayfirst=False)

    def getTransactionsOfStock( self, symbol ):
        return self.data[self.data['Symbol'] == symbol]

    def getTotalSum( self ):
        return np.sum(self.data['Amount'].replace('[\$,]', '', regex=True).astype(float).dropna().to_numpy())

