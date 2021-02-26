import pandas as pd
import numpy as np
import dateutil

class Transactions:

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

