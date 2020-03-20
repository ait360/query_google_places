import requests
import json
from utils import get_queried_data, check_health, get_nextpage_data




def get_state(google_api, action, api_key, entity, state):
    """
    query entity per state

    :param google_api:  google api eg https://maps.googleapis.com/maps/api/place/textsearch/json?
    :param action:      query=
    :param api_key:     unique google api key
    :param entity:      entities eg Restaurants, Hotels
    :param state:       states eg Abia, Lagos
    :return:            unique data results
    """


    search = f'{entity}+{state}'

    link = google_api + action + search + api_key

    print(link)

    a = requests.get(link)

    json_data = json.loads(a.text)

    results = json_data.get('results')
    state_data = get_queried_data(results)

    health = check_health(json_data)

    state_data = get_nextpage_data(google_api, api_key,
                                   json_data, state_data)




    return state_data







