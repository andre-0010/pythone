import bs4
import urllib3

def naviga(tag):
    print(tag.name.upper())
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag :
            naviga(stag)



def naviga2(tag, indent="") :
    print(indent + tag.name.upper())
    for stag in tag.contents:
        if type(stag) == bs4.element.Tag :
            naviga2(stag, indent + " ")




root = "https://it.wikipedia.org/wiki/Marche"
text = urllib3.request("GET", root)
risultato = text.data.decode()
doc = bs4.BeautifulSoup(risultato)
#print(doc.prettify())

naviga2(doc)
