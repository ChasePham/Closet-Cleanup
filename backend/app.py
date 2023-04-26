from flask import Flask
import pandas as pd
import numpy as np
from serpapi import GoogleSearch
import requests, os, json
import os, json
app = Flask(__name__)

@app.route('/')
def get_data():
    test_list = ['everlane','reformation']
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
    source_name = []
    price_nums = []
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
            "api_key": "8c06d8fadc2c651a8e3d8c0d5a0baf12dea102e98538fce593f4e777f3265347",
    }
        search = GoogleSearch(params)
        results = search.get_dict()

        google_shopping_data = results["shopping_results"]
        count = 0
        for i in google_shopping_data:
            if 'source' not in i:
                continue
            current_thumbnail = i['thumbnail']
            current_link = i['link']
            print(i)
            source = i['source'].lower().strip()
            price = i['price']
            if source in ethical_brands:
                thumbnails.append(current_thumbnail)
                product_links.append(current_link)
                source_name.append(source)
                price_nums.append(price)
                count += 1
                if count == 3:
                    break


    #second hand option
    query = "sustainable fashion striped cropped shirt"
    params = {
        "q": "site:depop.com " + query,
        "gl": "us",
        
        #"google_domain": "google.com",
        "api_key": "8c06d8fadc2c651a8e3d8c0d5a0baf12dea102e98538fce593f4e777f3265347",
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    thumbnails_two = []
    product_links_two = []
    depop_data = results["organic_results"]
    count = 0
    for i in depop_data:
        if 'thumbnail' not in i or 'link' not in i:
            continue
        current_thumbnail_two = i['thumbnail']
        current_link_two = i['link']
        thumbnails_two.append(current_thumbnail_two)
        product_links_two.append(current_link_two)  
        count += 1
        if count == 3:
            break
    
    # Return list format: First index are the thumbnails while the second index are the product links
    result_dict = {}
    result = [thumbnails,product_links,source_name,price_nums]
    result_two = [thumbnails_two,product_links_two]

    # To Organize, we put the lists into dictionary
    result_dict['result'] = result
    result_dict['result_two'] = result_two

    # print(json.dumps(result, indent=2, ensure_ascii=False)) 
    # print ("Second hand options")
    # print(json.dumps(result_two, indent=2, ensure_ascii=False)) 
    return (json.dumps(result_dict, indent=2, ensure_ascii=False))



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
    # get_data()