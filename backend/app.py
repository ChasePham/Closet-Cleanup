from flask import Flask
import pandas as pd
import numpy as np
from serpapi import GoogleSearch
import requests, lxml, os, json
import os, json
app = Flask(__name__)

@app.route('/')
def get_data():
    params = {
     "q": "Striped cropped shirt",
     "tbm" : "shop",
     "location": "Austin, Texas, United States",
     "hl": "en",
     "gl": "us",
     "api_key": "de13e5e6e842d938c52ef7697f1d26055cd17112dbb83081e9e4d619f34eca5e",
    }

    ethical_brands = ['larelaxed','wearwell','veneka','freespiritbrand',
    'etica','knickey','eclipse','harvestandmill','thestandardstich',
    'nube','triarchy','melissajoymanning','duchxfashion',
    'mariclaro','fairindigo','vegasrabbit',
    'walkinthroughflowers','christydawn','yesfriends','teemill',
    'wheredoesitcomefrom','mantisworld','silk-genie','kohr',
    'peopletree','blufruit','cultthread','dedicated',
    'anneherimine','ironroots','mudjeans','bluesuit','thela',
    'orbasics','swedishstockings','armedangels','intoadesign',
    'nudiajeans','lilianvontrapp','silentwaveindigo','appleoakfibreworks',
    'jackfruit','etiko','flarestreet','citizenwolf','joyya','commongood',
    'rupahus','dorsu','nonasties', 'thunderpants','yesfriends',
    'monsoonblooms','mayamiko','larelaxed','bleed','etica',
    'unrobe','vatter','dedicated','teemill','bhumi','senseorganics','knickey',
    'wheredoesitcomefrom','eclipse','etiko',
    'ironroots','sealand','mudjeans','kalaurie',
    'milavert','rapanui','jackalo','dorsu','noctu',
    'mantisworld','thestandardstitch','dharmabums','nube',
    'thercollective','bonlabel','leftedit',
    'charleeswim','thetintycloset','nonasties',
    'flarestreet','silkgenie','passionline',
    'citizenwolf','joyya','tonle','thesocialstudio','dawndenim',
    'reflectstudio','kampos','peopletree','mightygoodbasics',
    'armedangels','papiidesign','hopaal','philandlui',
    'twodaysoff','kingsofindigo','rozenbroek',
    'livingcrafts','recreate','organicbasics','nisa',
    'carlieballard','zerowastedaniel','blufruit','nudiejeans',
    'aestethiclondon','phyne','littleyellowbird','culthread',
    'duchxfashion','seeker','panamunaproject','annehermine',
    'nightswim','thegoodtee','fairindigo']


    search = GoogleSearch(params)
    results = search.get_dict()

    google_shopping_data = results["shopping_results"]

    thumbnails = []
    product_links = []

    for i in google_shopping_data:
        current_thumbnail = i['thumbnail']
        current_link = i['link']
        source = i['source']
        if source.lower() in ethical_brands:
            thumbnails.append(current_thumbnail)
            product_links.append(current_link)

    print(json.dumps(product_links, indent=2, ensure_ascii=False)) 
    #FIXME Test this to fix if it works. To test, input the top two list above this one into the data frame return statement
    # print(json.dumps(google_shopping_data, indent=2, ensure_ascii=False)) 
        
    return (json.dumps(product_links, indent=2, ensure_ascii=False))

    # Will most likely need a large list containing the most sustainable clothing brands OR a list containing non-sustainable clothes. (2 ways to do this)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
    # get_data()