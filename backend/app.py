from flask import Flask
import pandas as pd
import numpy as np
from serpapi import GoogleSearch
import requests, lxml, os, json
import os, json
app = Flask(__name__)

@app.route('/')
def get_data():
    test_list = ['everlane','girlfriendcollective','reformation']
    ethical_brands = ['everlane', 'girlfriendcollective','nudiejeans',
    'organicbasics','reformation','mudjeans','patagonia','naadam','eileen fisher','nisolo','allbirds','cariuma','rothys',
    'larelaxed','wearwell','veneka','freespiritbrand',
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



    # params = {
    #  "q": "Striped cropped shirt",
    #  "tbm" : "shop",
    #  "location": "Austin, Texas, United States",
    #  "hl": "en",
    #  "gl": "us",
    #  "api_key": "de13e5e6e842d938c52ef7697f1d26055cd17112dbb83081e9e4d619f34eca5e",
    # }

    # search = GoogleSearch(params)
    # results = search.get_dict()

    # google_shopping_data = results["shopping_results"]

    thumbnails = []
    product_links = []
    #FIXME: It is inefficient (takes too long) and requires too many API calls, however we could argue that we 
    # can pay for an opitimized option with serapapi for more API calls. 
    for j in test_list:
        current_brand = j + ' Clothing Brand'
        params = {
     "q": current_brand + " Striped cropped shirt",
     "tbm" : "shop",
     "location": "Austin, Texas, United States",
     "hl": "en",
     "gl": "us",
     "api_key": "de13e5e6e842d938c52ef7697f1d26055cd17112dbb83081e9e4d619f34eca5e",
    }
        search = GoogleSearch(params)
        results = search.get_dict()

        google_shopping_data = results["shopping_results"]
        for i in google_shopping_data:
            current_thumbnail = i['thumbnail']
            current_link = i['link']
            source = i['source'].lower().strip()
            if source in ethical_brands:
                thumbnails.append(current_thumbnail)
                product_links.append(current_link)

    print(json.dumps(product_links, indent=2, ensure_ascii=False)) 
    
    return (json.dumps(product_links, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
    # get_data()