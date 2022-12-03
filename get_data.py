import pandas as pd
import json
import requests

def get_accident_data(year: str):
    file_name = 'Data/FARS' + year + '/accident.csv'
    df = pd.read_csv(file_name, encoding='windows-1252', low_memory=False)
    return df

def get_realtime_accident_data(response_limit: str):
    url = 'https://realtime-road-accidents-in-usa.p.rapidapi.com/states/Texas'
    querystring = {'responseLimit': response_limit}
    headers = {
        'X-RapidAPI-Key': '30b8dcc7bcmsh269aa8b26f20a9cp18b81fjsnf414ff1c2be6',
        'X-RapidAPI-Host': 'realtime-road-accidents-in-usa.p.rapidapi.com'
    }
    response = requests.get(url, headers=headers, params=querystring)
    #response = json.dumps(response.json(), indent=4)
    #response = json.loads(response)
    return response

def count_accident_by_state(year: str):
    df = get_accident_data(year)
    state_name = df.loc[:,'STATENAME'].tolist()
    accident_in_each_state = dict()
    for states in state_name:
        if states in accident_in_each_state:
            accident_in_each_state[states] += 1
        else:
            accident_in_each_state[states] = 1
    return accident_in_each_state