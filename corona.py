import requests
import os
from bs4 import BeautifulSoup
from tabulate import tabulate
import numpy as np 
import matplotlib.pyplot as plt
extarct=lambda row:[x.text.replace('\n',"")for x in row]
URL='https://covidindia.org/'
SHORT_HEADERS=['State','Confirmed Cases','Cured','Deaths']
response=requests.get(URL).content
soup=BeautifulSoup(response,'html.parser')
header=extarct(soup.tr.find_all('th'))
stats=[]
states=[]
all_rows=soup.find_all('tr')
for row in all_rows:
    stat=extarct(row.find_all('td'))
    if stat:
        if len(stat)==0:
            stat=['',*stat]
            stats.append(stat)
        else:
            stats.append(stat)
objects=[]
for row in stats:
    objects.append(row[1])
y_pos=np.arange(len(objects))
Alive=[]
Deaths=[]
Recovered=[]
for row in stats:
    Alive.append(int(row[1]))
    Deaths.append(int(row[2]))
    Recovered.append(int(row[3]))
    states.append(row[0])
total=['TOTAL',sum(Alive),sum(Deaths),sum(Recovered)]
stats.append(total)
table = tabulate(stats, headers=SHORT_HEADERS) 
print(table)
plt.barh(y_pos, Alive, align='center', alpha=0.5, 
                 color=(234/256.0, 128/256.0, 252/256.0), 
                 edgecolor=(106/256.0, 27/256.0, 154/256.0)) 

plt.yticks(y_pos,states) 
plt.xlim(1,1500) 
plt.xlabel('Number of Cases') 
plt.title('Corona Virus Cases') 
plt.show()