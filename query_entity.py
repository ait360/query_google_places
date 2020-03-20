from pprint import pprint
from create_excel import create_worksheet, create_workbook
from lga_dict import local_govt_area
from utils import is_running
from query_by_state import get_state
from query_by_lga import get_lga, get_state_lga



def help_search(google_api, action, api_key, lga_dict, entity, state=''):


    state_data = []

    is_running(get_state)

    state_data += get_state(google_api, action, api_key, entity, state)

    is_running(get_state_lga)

    state_data = get_state_lga(lga_dict, google_api, action,
                               api_key, entity, state_data, state)

    is_running(get_lga)

    state_data = get_lga(lga_dict, google_api, action,
                         api_key, entity, state_data, state)
    print(f'We found {len(state_data)} results for {state}')

    return state_data


def search(google_api, action, api_key, lga_dict, entity, state=''):



    if state:

        workbook = create_workbook(entity, state)

        state_data = help_search(google_api, action, api_key,
                                 lga_dict, entity, state)

        create_worksheet(workbook, state_data, state)

    else:

        workbook = create_workbook(entity)

        for state in lga_dict.keys():

            state_data = help_search(google_api, action, api_key, lga_dict, entity, state)

            create_worksheet(workbook, state_data, state)


    workbook.close()
    print("Done, Closing the book")


lga_dict = local_govt_area


if __name__ == '__main__':


    google_api = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'


    action = 'query='


    ask_key = """input your api key,
it is of the form
&key=AIzaSyArrc8-wt9ombcwu62LwbcWeb67k_u6oAg  :  """

    api_key = input(ask_key)

    ask_entity = """

input the entity you which
to query eg: Restaurant  :  """

    entity = input(ask_entity)

    querybystate = input('\n\nDo you want to query a single state? y/n: ')


    if querybystate == 'n':
        message = """You are querying all the states, this will take sometime\npress Ctrl+C to cancel"""

        print(message)

        search(google_api, action, api_key, lga_dict, entity)


    elif querybystate == 'y':


        message = "\n\npick a state from the list below just as you can\nsee it in the list. Please do not add the quotes\n\n\n"

        print(message)

        states = ['Abia', 'Abuja', 'Adamawa', 'Akwa+Ibom', 'Anambra',
                  'Bauchi', 'Bayelsa', 'Benue', 'Bornu', 'Cross+river',
                  'Delta', 'Ebonyi', 'Edo', 'Ekiti', 'Enugu', 'Gombe',
                  'Imo', 'Jigawa', 'Kaduna', 'Kano', 'Katsina', 'Kebbi',
                  'Kogi', 'Kwara', 'Lagos', 'Nasarawa', 'Niger', 'Ogun',
                  'Ondo', 'Osun', 'Oyo', 'Plateau', 'Rivers', 'Sokoto',
                  'Taraba', 'Yobe', 'Zamfara']

        pprint(f'{states}')

        state = input('\nMay We have your state of interest: ')

        if state not in states:
            print('Please run the Script again following the instructions')
        else:
            search(google_api, action, api_key, lga_dict, entity, state)
