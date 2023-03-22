from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


req=requests.get("https://www.worldometers.info/coronavirus/")
bsObj=BeautifulSoup(req.text, 'html.parser')

data=bsObj.findAll("div", class_='maincounter-number')

totalcases=int(data[0].text.strip().replace(',',''))
recovered=int(data[2].text.strip().replace(',',''))

percentageRecovered=round((recovered/totalcases*100),2)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html"
                            ,data=data
                            ,totalcases=totalcases
                            ,percentageRecovered=percentageRecovered
                        )


if __name__ == "__main__":
    app.run(debug=True) 