from flask import Flask
import pandas as pd
import numpy as np
from serpapi import GoogleSearch
import os, json
app = Flask(__name__)

@app.route('/data')
def get_data():
    params = {
     "api_key": "de13e5e6e842d938c52ef7697f1d26055cd17112dbb83081e9e4d619f34eca5e",
     "engine": "google",
     "q": "brown shoes",
     "location": "Austin, Texas, United States",
     "google_domain": "google.com",
     "gl": "us",
     "hl": "en",
     "ijn": 0,
    "tbm": "isch"
    }

    search = GoogleSearch(params)

    # Get Pictures and website links dataframe"""

    # Convert to df
    # Saves the picture links
    image_results = []
    # Saves the source links
    image_source_links = []


    while True:
        results = search.get_dict()
        if "error" not in results:

        # Goes through 100 at a time I believe
            for i in range(len(results['images_results'])):

                current = results['images_results'][i]
                curr_original_pic = current['original']
                curr_link = current['link']
                if curr_original_pic not in image_results:
                    image_results.append(curr_original_pic)
                    image_source_links.append(curr_link)

            # Limit to how many similar clothing items we want
            if len(image_results) == 500:
             break
            params['ijn'] += 1
        else:
            break
    # Same as above
        if len(image_results) == 500:
            break


    # print(image_results)
    # print(image_source_links)
    # print(len(image_results))

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
    
    image_results_final = []
    image_source_links_final = []

    #FIXME Test this to fix if it works. To test, input the top two list above this one into the data frame return statement
    for i in range(len(image_source_links)):
        current = image_source_links[i].lower()
        for j in range(len(ethical_brands)):
            if ethical_brands[j] in current:
                image_results_final.append(image_results[i])
                image_source_links_final.append(image_source_links[i])
                break
        
    return pd.DataFrame({'img_pic': image_results_final, 'img_source_link': image_source_links_final}).to_json()

    # Will most likely need a large list containing the most sustainable clothing brands OR a list containing non-sustainable clothes. (2 ways to do this)

    """Extracting Sustainable Clothing"""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)