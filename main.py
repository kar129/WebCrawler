from __future__ import print_function
import mechanize
import bs4 as bs
import urllib2
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
URL = "http://sahibinden.com"
search1=["deniz manzarali","konut","villa","daire","mustakil","bekara"]
search2=["kiralik","satilik"]
b= mechanize.Browser()
b.set_handle_refresh(False)
b.addheaders=[('User-agent', "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36")]
for i in range(len(search1)):
    for j in range(len(search2)):

        b.open(URL)

        b.select_form(nr=0)
        b.form["query_text"]=str(search1[i])+" "+str(search2[j])
        b.method="GET"
        b.submit()
        soup=bs.BeautifulSoup(b.open(b.geturl()).read(),"lxml")
        for a in soup.find_all("a",class_="classifiedTitle"):
            with open ("save.txt", 'a') as f:
                f.write(a.string)


