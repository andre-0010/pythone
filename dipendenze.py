import bs4
import urllib.request 

def naviga(tag) :
    if tag.name.upper()=="A" :
        print(tag.get("href"))
    for stag in tag.contents :
        if type(stag) == bs4.element.Tag :
            naviga(stag)
        


root = "https://it.wikipedia.org/wiki/Marche"
text = urllib.request.urlopen(root)
risultato = text.read().decode()
doc = bs4.BeautifulSoup(risultato, features="html.parser")
#print(doc.prettify())

naviga(doc)
