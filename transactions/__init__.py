import pandas as pd
import numpy as np

class Transactions:

    def __init__( self, odoFileName ):
        self.dataAggrigate = {'Market':'first','Type':'first','Price':'mean','Amount':'sum','Total':'sum','Fee':'sum','Acc':'first'}
        self.data = pd.read_csv(odoFileName, header=1)

    def getAggregateTransactionsOfStock( self, symbol ):
        dataFrame = self.data[roth.data['Symbol'] == symbol]
        self.data

