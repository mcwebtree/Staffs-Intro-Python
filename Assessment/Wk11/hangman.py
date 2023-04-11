

# params
api_ninjsas_key = "NZ7cUijXf6uoivDW6yl/EA==ufxyi04CTS0N25V6"

import requests
import json 

def get_word():
    api_url = 'https://api.api-ninjas.com/v1/randomword'
    response = requests.get(api_url, headers={'X-Api-Key': api_ninjsas_key})
    if response.status_code == requests.codes.ok:
        a_ret = json.loads(response.text)
        return a_ret['word']
    else:
        print("Error:", response.status_code, response.text)
        return ""
    
s_word = get_word()
if s_word != "":
    print ( f"The word is '{s_word}'" )