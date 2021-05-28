import datetime
import requests

# sample
DAILY_LIMIT = 5
CURRENT_DONE = 3
HOURLY_LIMIT = 10


def call_api(username, api_user_id, to_crawl, id, account):
    # update database

    # get no of followers of the username
    if api_user_id != 'NA':
        # the api user id is already received
        pass
    else:
        status, resp = get_account_static_info(username)
        if status != 200:
            return status
        else:
            # now upload data
            account.image_url = resp['image_url']
            account.api_user_id = resp['api_user_id']
            account.name = resp['name']
            account.save()
            api_user_id = resp['api_user_id']

    # update the no of followers in database

    status, resp = get_user_info(api_user_id)

    if status == 200:
        followers = resp['followers']
        account.followers = followers
        account.save()

        if not to_crawl:
            # as it is already checked
            # make to_crawl 0 in database
            account.is_not_crawled = 1
            account.save()

        return status

    else:
        return status


def update_by_priority(accounts):
    # get all the data here

    # now sort them according to the date, past date first
    accounts_list = get_users(accounts)
    # [ID, INSTA_USERNAME, API_USER_ID, DATE, IS_NOT_CRAWLED]

    for i in range(len(accounts_list)):
        accounts_list[i] = accounts_list[i][::-1]

    # [IS_NOT_CRAWLED, DATE, API_USER_ID, INSTA_USERNAME, ID]
    accounts_list.sort()

    print('> ACCOUNTS', accounts_list)

    for i in range(min(HOURLY_LIMIT, len(accounts_list))):

        id = accounts_list[i][4]

        account = accounts.objects.all()[id]

        status = call_api(accounts_list[i][3], accounts_list[i][2], accounts_list[i][0],
                          accounts_list[i][4], account)
        if status == 200:
            account.date = datetime.date.today()
            account.save()
            print('SUCCESSFULLY UPDATED')

            continue
        else:
            break


def manage_update(Accounts, resource):
    print("> MANAGING UPDATES")
    # check if the daily limit is exceeded

    # get current limit by query

    current = get_current(resource)
    print("> CURRENT", current)

    if current <= DAILY_LIMIT:
        update_by_priority(Accounts)


"""
HELPING FUNCTIONS
"""


def get_account_static_info(username):
    """
    Takes the username and returns api_user_id, image_url, public_email
    :param username: (str) username of the user
    :return: dict(): {'api_user_id': username ID as in api (str), 'image_url': url (str), 'public_email' : email}
    """
    api_user_id = None
    image_url = None
    full_name = None
    email = None
    status = 200

    url = "https://instagram47.p.rapidapi.com/get_user_id"

    querystring = {"username": username}

    headers = {
        'x-rapidapi-key': "6689feb7aemsh38cfa9d303ff9fcp13c5b1jsn56d5b488c201",
        'x-rapidapi-host': "instagram47.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        response = response.json()

        if response['status_code'] != 100:

            api_user_id = response['user_id']

            print('API USER ID', api_user_id)

            url = "https://instagram47.p.rapidapi.com/email_and_details"

            querystring = {"userid": api_user_id}

            response = requests.request("GET", url, headers=headers, params=querystring)

            if response.status_code == 200:
                response = response.json()['body']
                image_url = response['profile_pic_url']
                full_name = response['full_name']
            else:
                print('REQUEST COULD NOT GO THROUGH')
                status = response.status_code

            # DUMMY DATA
            return status, {'api_user_id': api_user_id, 'image_url': image_url, 'name': full_name}
        else:
            return 100, None

    else:
        status = response.status_code
        return status, None


def get_user_info(api_user_id):
    """
    Return the data of user after getting the user id of the api

    :param api_user_id: The id given by the api
    :return: dict(): {'followers': no of followers (int), 'following': no of accounts the user is following (int)}
    """

    url = "https://instagram47.p.rapidapi.com/email_and_details"

    querystring = {"userid": api_user_id}

    headers = {
        'x-rapidapi-key': "6689feb7aemsh38cfa9d303ff9fcp13c5b1jsn56d5b488c201",
        'x-rapidapi-host': "instagram47.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    if response.status_code == 200:
        # DUMMY DATA
        response = response.json()
        return 200, {'followers': response['body']['follower_count'],
                                      'following': response['body']['following_count']}
    else:
        return response.status_code, None


def get_current(Resources):
    return Resources.objects.all()[0].done


def get_users(Accounts):
    """

    :return: [ID, INSTA_USERNAME, API_USER_ID, DATE, IS_NOT_CRAWLED]
    """
    accounts = []
    for i in range(len(Accounts.objects.all())):
        accounts.append([i, Accounts.objects.all()[i].insta_username, Accounts.objects.all()[i].api_user_id,
                         Accounts.objects.all()[i].date, Accounts.objects.all()[i].is_not_crawled])
    return accounts
