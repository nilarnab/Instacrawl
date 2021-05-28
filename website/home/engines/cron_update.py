# sample
DAILY_LIMIT = 5
CURRENT_DONE = 3
HOURLY_LIMIT = 5


def call_api(username, to_crawl):
    # update database

    # get no of followers of the username

    followers = 108

    # update the no of followers in database

    if to_crawl:
        # as it is already checked
        # make to_crawl 0 in database

        pass


def update_by_priority():
    # get all the data here

    # now sort them according to the date, past date first
    accounts = get_users()

    for i in range(len(accounts)):
        accounts[i] = accounts[i][::-1]

    accounts.sort()

    call_api()


def manage_update(data):
    global Accounts
    Accounts = data
    print("HELLO ACCOUNTS")

    for i in range(len(Accounts.objects.all())):
        print(Accounts.objects.all()[i].name)

    # check if the daily limit is exceeded

    # get current limit by query

    # current = get_current()
    # if current <= DAILY_LIMIT:
    #     update_by_priority()


"""
HELPING FUNCTIONS
"""


def get_current():
    return CURRENT_DONE


def get_users():
    return [
        ['NAME1', 'username1', '2020-05-01', 1],
        ['NAME2', 'username2', '2020-05-01', 1],
        ['NAME3', 'username3', '2020-05-02', 0],
        ['NAME4', 'username4', '2020-05-03', 0],
    ]



