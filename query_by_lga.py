import requests
import json
from utils import get_queried_data, check_health, get_nextpage_data




def get_state_lga(lga_dict, google_api, action, api_key, entity,
                    state_data=None, state=''):
    """
    query per state and local government area
    :param lga_dict:      keys = states, values = list of lga's
    :param google_api:      google api https://maps.googleapis.com/maps/api/place/textsearch/json?
    :param action:          query
    :param api_key:         unique google api key
    :param entity:          entities eg Restaurants, Hotels
    :param state_data;      a set of unique data from previous processes
    :param state:           state eg 'Abia'
    :return:                state_data
    """

    for lga in lga_dict[state]:
        print(lga)

        search = f'{entity}+{state}+{lga}'

        link = google_api + action + search + api_key


        requested_obj = requests.get(link)

        json_data = json.loads(requested_obj.text)

        results = json_data.get('results')

        state_data = get_queried_data(results)

        state_data = get_nextpage_data(google_api, api_key,
                                       json_data, state_data)

    return state_data




def get_lga(lga_dict, google_api, action, api_key, entity,
               state_data=None, state=''):
    """
    query per local government area

    :param lga_dict:      keys = states, values = list of lga's
    :param google_api:      google api https://maps.googleapis.com/maps/api/place/textsearch/json?
    :param action:          query
    :param api_key:         unique google api key
    :param entity:          entities eg Restaurants, Hotels
    :param state_data;      a set of unique data from previous processes
    :param state:           state eg 'Abia'
    :return:                state_data
    """

    for lga in lga_dict[state]:
        print(lga)

        search = f'{entity}+{lga}'

        link = google_api + action + search + api_key

        requested_obj = requests.get(link)

        json_data = json.loads(requested_obj.text)

        results = json_data.get('results')

        state_data = get_queried_data(results, state_data)

        state_data = get_nextpage_data(google_api, api_key,
                                       json_data, state_data)


    return state_data





