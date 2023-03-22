from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


req=requests.get("https://en.wikipedia.org/wiki/List_of_largest_Internet_companies")
bsObj=BeautifulSoup(req.text, 'html.parser')

data=bsObj.find("table", {'class':'wikitable sortable mw-collapsible jquery-tablesorter mw-made-collapsible'})

table_data=[]
trs=bsObj.select('table tr')
for tr in trs[2:13]:
    row=[]
    for t in tr.select('td')[:3]:
        row.extend([t.text.strip()])
    table_data.append(row)

data=table_data

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html"
                            ,data=data
                            
                        )


if __name__ == "__main__":
    app.run(debug=True) 