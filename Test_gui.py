import requests
from threading import Timer

#print(requests.get("http://127.0.0.1:8000/database").json())

#url = "https://www.google.com"
#url = url.replace("/","'",255)
#request = "http://127.0.0.1:8000/database/Add-url/" + url
#print(url)
#print(request)
#print(requests.post(request).json())
#request = "http://127.0.0.1:8000/check-status/" + url
#request = "http://127.0.0.1:8000/database/None-status/"

request = "http://127.0.0.1:8000/database/All-test/"
#print(requests.get(request).json())



#not updating the database for some reson
def Update_All_URL():
    Alldata = requests.get("http://127.0.0.1:8000/database").json()
    for data in Alldata:
        url = data[0]
        url = url.replace("/", "'", 255)
        request = "http://127.0.0.1:8000/check-status/" + url
        #print(requests.post(request).json())
        print("updated: " + url)

    Timer(60,Update_All_URL).start()

#bonos

Update_All_URL()

#does update the database but it's not realy a separate function
def Update_All_URL_API():
    request = "http://127.0.0.1:8000/check-status/All"
    print(requests.post(request).json())
    Timer(60,Update_All_URL_API).start()


#Update_All_URL_API()










#url = "https://www.google.com"
#url = url.replace("/","'",255)
#request = "http://127.0.0.1:8000/check-status/" + url
#print(requests.put(request).json())
