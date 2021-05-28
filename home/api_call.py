import requests


while True:
    url = "https://instagram47.p.rapidapi.com/get_user_id"

    querystring = {"username":"bangali_tintin"}

    headers = {
        'x-rapidapi-key': "6689feb7aemsh38cfa9d303ff9fcp13c5b1jsn56d5b488c201",
        'x-rapidapi-host': "instagram47.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.status_code)