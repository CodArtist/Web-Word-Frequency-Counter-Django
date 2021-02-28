from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import operator
import os
from word_counter.models import Urls
# Create your views here.

def home(request):    
    return render(request,'a.html')
def count(request):
   
    data=request.GET['fulltextArea']
    print("lalalalalllllllllllllllllllllllllllllllllllllllllllllllll")

    
    res=requests.get(data)

    linkexist=True
    if(Urls.objects.filter(link=data).values("link").count()==0):
        obj=Urls(link=data)
        obj.save()
        linkexist=False
    
    soup =BeautifulSoup(res.text,'lxml')
    text=""
    title=soup.select('p')
    for para in title:
        text+=para.text

    
    word_list=text.split()
    datalen=len(word_list)
    wordlist=[]
    with open(r"C:\Users\dell\Desktop\word_counter\word_counter\wordlist.txt") as f:
        for line in f:
            wordlist.append(line.strip())
    worddictionary={}
    for word in word_list:
        if word in worddictionary:
            worddictionary[word]+=1
        else:
            if word not in wordlist:
                worddictionary[word]=1
            
                


    
    sorteddictionary=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)
    i=1
    top10={}
    for word,value in sorteddictionary:
        top10[word]=value
        i+=1
        if i>10:
            break
   
    

    return render(request,'count.html',{'data':data,'length':datalen,'worddictionary':top10.items(),'Linkexist':linkexist})