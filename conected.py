#from typing import ItemView
import requests
from bs4 import BeautifulSoup

"""
https://j2logo.com/flask/tutorial-como-crear-api-rest-python-con-flask/

"""

def baseUrl():
    return "https://dsp-wiki.com"



def conected():
    response= requests.get("https://dsp-wiki.com/Main_Page")

    soup = BeautifulSoup(response.text,"lxml")

    return soup


def findItems(soup):

    footer= soup.find_all(title="Items")

    response= requests.get(baseUrl()+footer[0].get("href"))

    soup = BeautifulSoup(response.text,"lxml")

    footer= soup.find("tbody")

    
    listMaterials=[]
    
    for row in footer.find_all("tr"):
        for cell in row.find_all("td"):
            test= cell.find("a")
            listMaterials.append((test.get("title"),test.get("href")))


    dictMaterials= dict(map(lambda x: (x[0],x[1]), (x for x in listMaterials) ))

    return dictMaterials

def viewItem(dictMaterials):
    #print("dictMaterials: ",dictMaterials)

    class Item():
        nameItem= None
        cantPerCraft= None
        durationPerCraft= None
        dictNecessaryMaterias= {}


    
    response= requests.get(baseUrl() + dictMaterials.get("Circuit Board"))

    soup= BeautifulSoup(response.text,"lxml")

    footer= soup.find("div", {"class":"tt_recipe"})
    itemView= Item()
    for cell in footer.children:
        if (cell["class"][0]=="tt_output_item"):
            itemView.nameItem=cell.a.get("title")
            itemView.cantPerCraft=cell.text
        elif (cell["class"][0]=="tt_rec_arrow"):
            itemView.durationPerCraft= cell.text
        elif (cell["class"][0]=="tt_recipe_item"):
            itemView.dictNecessaryMaterias[cell.a.get("title")]= cell.text
    
    
            

    pass

#findItems(conected())

viewItem(findItems(conected()))