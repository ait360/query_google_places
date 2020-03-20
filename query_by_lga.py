import requests
import json
from utils import get_queried_data, check_health, get_nextpage_data




def get_state_lga(local_dict, google_api, action, api_key,
                    state_data=None, state=''):
    """
    query state and local government area
    :param local_dict: keys = states, values = list of lga's
    :param google_api: google api
    :param action: query
    :param api_key: unique google api key
    :param state: state eg 'Abia'
    :return: state_data
    """

    for lga in local_dict[state]:
        print(lga)
        search = 'pharmacy+' + state + '+' + lga
        link = google_api + action + search + api_key


        requested_obj = requests.get(link)

        json_data = json.loads(requested_obj.text)

        results = json_data.get('results')

        state_data = get_queried_data(results)

        state_data = get_nextpage_data(google_api, api_key,
                                       json_data, state_data)

    return state_data




def get_lga(local_dict, google_api, action, api_key,
               state_data=None, state=''):


    for lga in local_dict[state]:
        print(lga)
        search = 'pharmacy+' + '+' + lga
        link = google_api + action + search + api_key

        requested_obj = requests.get(link)

        json_data = json.loads(requested_obj.text)

        results = json_data.get('results')

        state_data = get_queried_data(results, state_data)

        state_data = get_nextpage_data(google_api, api_key,
                                       json_data, state_data)


    return state_data





