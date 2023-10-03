import requests
from threading import Timer


def Update_All_URL():
    Alldata = requests.get("http://127.0.0.1:8000/database").json()
    for data in Alldata:
        url = data[0]
        url = url.replace("/", "'", 255)
        request = "http://127.0.0.1:8000/check-status/" + url

        response = requests.post(request)
        print("updated: " + url)

    Timer(60, Update_All_URL).start()
Update_All_URL()
