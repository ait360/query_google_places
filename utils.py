import requests
import json


def get_queried_data(results, state_data=[]):
    """
    get required attributes and see if data is unique

    :param results: a list of queried data
    :param state_data: cleaned data per state,
                       empty if called the first time
    :return: state_data
    """

    for result in results:
        name =      result.get('name')
        address =   result.get('formatted_address')
        latitude =  str(result.get('geometry').get('location').get('lat'))
        longitude = str(result.get('geometry').get('location').get('lng'))
        place_id =  result.get("place_id")
        entry = (name, address, latitude, longitude, place_id)
        if entry not in state_data:
            state_data.append(entry)
    return state_data


def check_health(json_data=None):

    if json_data is not None:
        if str(json_data.get('status')) == 'REQUEST_DENIED':
            print('invalid key parameter')

            return True

        elif str(json_data.get('status')) == 'OVER_QUERY_LIMIT':
            print("you've exceeded you quota")

            return True

def get_nextpage_data(google_api, api_key, json_data=None, state_data=None):

    while json_data.get('next_page_token') is not None:

        page_token = 'pagetoken=' + json_data.get('next_page_token')
        link = google_api + page_token + api_key
        print(link)

        a = requests.get(link)

        json_data = json.loads(a.text)

        health = check_health(json_data)

        if health:
            break

        while str(json_data.get('status')) == 'INVALID_REQUEST':
            print('Retrying')
            a = requests.get(link)
            json_data = json.loads(a.text)

        results = json_data.get('results')

        state_data = get_queried_data(results, state_data)

    return state_data


def is_running(func):

    if func.__name__ == 'get_state':

        print('querying state only')

    elif func.__name__ == 'get_state_locality':

        print('querying state and locality')

    elif func.__name__ == 'get_state_lga':

        print('querying state and LGA')

    elif func.__name__ == 'get_lga':

        print('querying lga only')



