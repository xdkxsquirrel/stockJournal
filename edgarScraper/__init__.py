import re
import pandas as pd
import requests
import unicodedata
from bs4 import BeautifulSoup

def getListOf10Ks( ticker ):
    url = r"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=" + ticker + r"&type=10-K&dateb=&owner=exclude&count=40"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html5lib')

    table = soup.find('div', attrs = {'id':'seriesDiv'})
    tenKs = []
    for row in table.findAll('td', attrs = {'nowrap':'nowrap'}):
        try:
            tenK = row.a['href']
            tenK = str(row)[str(row).find(r'<a href="/Archives')+9:str(row).find("index.htm")+9]
            if "Archives" in tenK:
                tenKs.append("https://www.sec.gov" + tenK)
        except:
            pass

    return tenKs

def get10KLink( url ):
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html5lib')
    table = soup.find('table', attrs = {'class':'tableFile'})
    for row in table.findAll('td', attrs = {'scope':'row'}):
        try:
            row.a['href']
            if str(row).find(r'/ix?doc='):
                return "https://www.sec.gov" + str(row)[str(row).find(r'<a href="ix?doc')+34:str(row).find(".htm")+4]
            else:
                return "https://www.sec.gov" + str(row)[str(row).find(r'<a href="/Archives')+9:str(row).find(".htm")+4]
        except: 
            pass

def parse10K( url ):
    data = requests.get(url.rsplit('/', 1)[0] + '/')
    soup = BeautifulSoup(data.content, 'html5lib')
    tableBody = soup.find_all('tbody')
    for row in tableBody:
        trs = row.find_all('tr')
        for thing in trs:
            print(thing)
            break
        
        

def getArchivesList( url ):
    archivesList = []
    data = requests.get(url.rsplit('/', 1)[0] + '/')
    soup = BeautifulSoup(data.content, 'html5lib')
    table = soup.find('table', attrs = {'summary':'Directory Listing for $full_dir'})
    for row in table.findAll('tr'):
        try:
            row.a['href']
            url = ''
            url = (str(row)[str(row).find(r'<a href="/Archives')+9:str(row).find(".htm")+4])
            if url is not '':
                archivesList.append("https://www.sec.gov" + url)
        except: 
            pass
    return archivesList

def getConstructedRList( url ):
    rList = []
    for i in range(19):
        rList.append(url.rsplit('/', 1)[0] + '/R' + str(i+1) + '.htm')
    return rList


def getRList( list ):
    rList = []
    for row in list:
        if row.rsplit('/', 1)[1][0] is 'R':
            rList.append(row)
    return rList

def getDocumentAndEntityInformation( url ):
    successful = False
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html5lib')
    table = soup.find('table', attrs = {'class':'report'})
    row = table.tr
    for value in row:
        if 'Document and Entity Information Document' in str(value):
            successful = True
    
    if not successful:
        return (False, None, None)

    for row in table.findAll('tr'):
        for value in row.findAll('td'):
            if "Entity Registrant Name" in str(value):
                next = value.find_next('td')
                location = str(next).find('<span></span>')
                entityRegistrantName = str(next)[17:location]
            if "Document Fiscal Year Focus" in str(value):
                next = value.find_next('td')
                fiscalYear = str(next)[17:21]
                break

    return (successful, entityRegistrantName, fiscalYear)

def getBalanceSheet( url ):
    successful = False
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html5lib')
    table = soup.find('table', attrs = {'class':'report'})
    row = table.tr
    for value in row:
        if 'Consolidated Balance Sheets' in str(value):
            successful = True
    
    if not successful:
        return (False, None, None)

    for row in table.findAll('tr'):
        for value in row.findAll('td'):
            print(value)
            if "TOTAL ASSETS" in str(value):
                next = value.find_next('td')
                location = str(next).find('<span></span>')
                totalAssets = str(next)[17:location]
                print(str(next)[17:location])
            if "Document Fiscal Year Focus" in str(value):
                next = value.find_next('td')
                location = str(next).find('<span></span>')
                totalLiabilities = str(next)[17:21]
                print(str(next)[17:location])
                break

    return (successful, totalAssets, totalLiabilities)
    
    
        
cnt = 0
TICKER = "INTC"
# tenKs = getListOf10Ks(TICKER)
# tenKUrl = get10KLink( tenKs[0] )
tenKUrl = r'https://www.sec.gov/Archives/edgar/data/50863/000005086320000011/a12282019q4-10kdocument.htm'
data = parse10K( tenKUrl )

