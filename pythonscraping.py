from bs4 import BeautifulSoup
import csv
import requests
from itertools import zip_longest
##lists
all_AT=[]
all_BT=[]
score=[]
reslut=[]
###/lists
## st1
req=requests.get("https://www.yallakora.com/match-center")
src=req.content

soup=BeautifulSoup(src,"lxml")
## Team A 
all_Ateam=soup.find_all("div",{"class":"teams teamA"})
for at in range(len(all_Ateam)):
    all_AT.append(all_Ateam[at].text.strip())
print(all_AT)
####/Team 


##team B
all_Bteam=soup.find_all("div",{"class":"teams teamB"})
for bt in range(len(all_Bteam)):
    all_BT.append(all_Bteam[bt].text.strip())
print(all_BT)
#team/B

### csv file

file=[all_AT,all_BT]
match=zip_longest(*file)
with open("match2.csv","a",encoding="utf -8") as myfile:
    wr=csv.writer(myfile)
    wr.writerows(match)

### find score


score_match=soup.find_all("div",{"class":"MResult"})
for m in range(len(score_match)):
    score.append(score_match[m].text.strip())
for re in range(len(score)):
    
        new=score[re].replace("\n-\n","-")
        reslut.append(new)
### csv file
file2=[all_AT,all_BT,reslut]
zi=zip_longest(*file2)
with open("reslut.csv","a") as myscond:
     wr=csv.writer(myscond)
     wr.writerow("First team")
     wr.writerows(zi)

print(reslut)