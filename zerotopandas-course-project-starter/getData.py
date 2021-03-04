from bs4 import  BeautifulSoup
import requests
import numpy as np

def tableDataText(table):    
    """Parses a html segment started with tag <table> followed 
    by multiple <tr> (table rows) and inner <td> (table data) tags. 
    It returns a list of rows with inner columns. 
    Accepts only one <th> (table header/data) in the first row.
    """
    def rowgetDataText(tr, coltag='td'): # td (data) or th (header)       
        return [td.get_text(strip=True) for td in tr.find_all(coltag)]  
    rows = []
    trs = table.find_all('tr')
    headerow = rowgetDataText(trs[0], 'th')
    if headerow: # if there is a header row include first
        rows.append(headerow)
        trs = trs[1:]
    for tr in trs: # for every table row
        rows.append(rowgetDataText(tr, 'td') ) # data row       
    return rows

html_text = requests.get('https://www.vedur.is/skjalftar-og-eldgos/jardskjalftar/reykjanesskagi/#view=table').content
soup = BeautifulSoup(html_text, 'lxml')
table = soup.find('tbody')
print(table)
#dataTable = tableDataText(table)

