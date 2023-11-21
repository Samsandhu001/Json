import pandas as pd
import requests
import json




def get_cat_facts(_ammont):
    
    #connection string
    #chech documentation
    conn_str = f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={_ammont}'

    #call the api

    response = requests.get(conn_str)

    #call the api

    #parse the results
    response = json.loads(response.content)
    l_cat_fact = []
    for _fact in response:
        l_cat_fact.append(_fact['text'])
    
    print(l_cat_fact)
    return l_cat_fact

str = get_cat_facts(3)
print(str)