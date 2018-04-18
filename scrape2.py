import csv
import requests
from bs4 import BeautifulSoup

url ='http://www.skysports.com/premier-league-table'
response=requests.get(url)
html=response.content


soup=BeautifulSoup(html)
#print(soup.prettify())
tableBody=soup.find_all('tbody')

list_of_rows=[]
trs=tableBody[0].find_all('tr')


for row in trs:
    list_of_cells=[]
    for cell in row.find_all('td'):
        text=cell.text.replace('\n','')
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

print(list_of_rows)    
 

outfile = open('./epltable6.csv','w', newline='')

with outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Rank','Team','GP', 'Wins','Draws','Losses', 'GF','GA','GD','Pts'])
    writer.writerows(list_of_rows)
outfile.close()



  
    

#print(list_of_rows)
    
        

