import requests

# # empty list
# lst = [1,'2','',5]
# print(lst)
# print(len(lst))
# if lst[2] == "":
#     print(f"{lst[2]} is empty")
#
# lst1 = ['a','a','']
# print(lst1)
# print(len(lst1))
# if lst1.count("") > 0:
#     print("Invalid Input")

api_url = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY  = open('api_key','r').read().rstrip()

def func_api(api_url,lat,lon):
    api_url = f"{api_url}lat={lat}&lon={lon}&appid={API_KEY}"
    print(api_url)


func_api(api_url,41.25,-95.93)
