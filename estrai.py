import urllib.request
url = "https://www.comuni-italiani.it/province.html"
response = urllib.request.urlopen(url)
theBytes = response.read()
text = theBytes.decode(encoding="iso-8859-1")
import bs4
doc = bs4.BeautifulSoup(text, features="html.parser")
elems = doc.find_all("table")
table = elems[3]
for tr in table.contents[2:-2]:
    if type(tr) == bs4.element.Tag :
        tds = tr.contents
        kmq = int(tds[4].get_text().replace(".",""))
        prov = tds[1].get_text()
        resi = int(tds[2].get_text().replace(".",""))
        sigl = tds[7].get_text()
        densita = round(float((tds[5].get_text().replace(".","")).replace(",",".")), 1)
        densitaCalcolata = round(resi/kmq, 1)
        print("-"*81)
        print(f"| {sigl:3s} | {prov:25s} |{resi:9d} |{kmq:6d} |{densitaCalcolata:7.1f} |{densita:7.1f} | {str(False if densitaCalcolata != densita else True):6} |")
        
