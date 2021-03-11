import re
import pandas as pd
import requests
import numpy as np
import unicodedata
from bs4 import BeautifulSoup

class Data:
    def __init__( self, symbol ):
        pass

    def getSheet( self, url, typeOfSheet, year ):
        successful = False
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'html5lib')
        table = soup.find('table', attrs = {'class':'report'})
        try:
            row = table.tr
            for value in row:
                if typeOfSheet in str(value):
                    successful = True
        except:
            return (False, None)
        
        if not successful:
            return (False, None)

        first = True
        count = 0
        balanceSheet = []
        label = ''
        number = ''

        for row in table.findAll('tr'):
            for value in row.findAll('td'):
                if first:
                    first = False
                else:
                    if "us-gaap" in value.text:
                        location = value.text.find("us-gaap")
                        number = value.text[0:location].strip('\n').strip('$').strip(',')
                    else:
                        if len(re.findall("[a-zA-Z]", value.text)) > 2:
                            label = value.text.strip('\n')
                        elif len(re.findall("[0-9]", value.text)) > 2 and label != '':
                            number = value.text.strip('\n').strip('$').strip(',')
                        
                    if label != '' and number != '':
                        balanceSheet.append([label, number])
                        number = ''
                        label = ''
                    
        return (successful, pd.DataFrame(balanceSheet, columns=['Name', year]))

    def getBalanceSheet( self, url, year ):
        return self.getSheet( url, 'Consolidated Balance Sheets', year )


    def getCashFlow( self, url, year ):
        return self.getSheet( url, 'Consolidated Statements of Cash', year )

    def getIncomeStatement( self, url, year ):
        return self.getSheet( url, 'Consolidated Statements of Income', year )