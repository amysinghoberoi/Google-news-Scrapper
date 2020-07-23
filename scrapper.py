"""


@author: amysi
"""

import requests
from bs4 import BeautifulSoup

#print(response)
def india():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"India"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]) 

##############################################################

def Your_local_news():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Your local news"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]) 

#################################################################

def World():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"World"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]) 
#########################################################################
def Technology():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Technology"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]) 
############################################################################

def Entertainment():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Entertainment"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]) 

##########################################################################
def Sports():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Sports"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]) 
#########################################################################
def Science():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Science"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]) 
#########################################################################
def Health():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Health"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]) 

#########################################################################
def Business():
    a=[]
    url="https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN%3Aen"
    response=requests.get(url)
    soup=BeautifulSoup(response.content,"lxml")
    r1=soup.find("div",{"jsname":"V2bVMb"})
    r2=r1.find("div",{"aria-label":"Business"})
    h=r2.find("a",class_="SFllF")["href"]
    link="https://news.google.com"+h
    new=requests.get(link)
    soup=BeautifulSoup(new.content,"lxml")
    for s1 in soup.findAll("div",{"jscontroller":"d0DtYd"}):
        s2=s1.find("div",class_="xrnccd F6Welf R7GTQ keNKEd j7vNaf")
        s3=s2.find("h3",class_="ipQwMb ekueJc gEATFF RD0gLb")
        a.append(s3.text)
    
    return print(a[:5]) 

