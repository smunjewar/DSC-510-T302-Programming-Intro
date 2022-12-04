# import requests
#
# res = requests.get('https://ipinfo.io/')
# data = res.json()
#
# city = data['city']
#
# location = data['loc'].split(',')
# latitude = location[0]
# longitude = location[1]
#
# print("Latitude : ", latitude)
# print("Longitude : ", longitude)
# print("City : ", city)

# li = ()
# # mystring = "Omaha,NE,USA"
# # mystring = "Omaha,NE,"
# mystring = "Omaha,NE"
# li = list(mystring.split(','))
# print(type(li))
# for num in [0,1,2]:
#     print(li[num])
#     if li[num].strip() == "":
#         print(num)

print(f"Welcome to common weather app : ")
print(f"Weather can be pulled based on City Name or Zip code ")
print(f"City Name Example : Omaha or Omaha,NE or Omaha,NE,US")
print(f"Zip Code Example : 68130 or 68130,NE")

while True:

    usr_input = input("\n Enter y to cont and q to quit() : ")
    # print(len(usr_input))
    # print(usr_input.lower())
    if usr_input.lower() == 'q':
        print("Thanks for visiting !")
        break
    elif len(usr_input) == 0 or usr_input.strip().lower() != 'y' :
        print ("Invalid Input : {}, Please try again".format(usr_input))
    else:
            usr_list = []
            url = "http://api.openweathermap.org/geo/1.0/"
            api_key="fe5cc61799dd4704e63e6fc3feb3f713"
            # ?zip=68130,US&appid=fe5cc61799dd4704e63e6fc3feb3f713"
            usr_list = input("Enter city name or zip code: ").split(",")
            # usr_list = list(usr_city.split(","))
            print(usr_list)
            print(type(usr_list))
            if usr_list.count(" ") > 0:
                print("Invalid Input !!")
            else:
                if len(usr_list) == 2 and usr_list[0].isnumeric():
                    print("Zip Code")
                    # print(f"{url}?zip={usr_list[0]},{usr_list[1]}&appid={api_key}")
                    #-- Zip Code with Country code.
                    url = f"{url}zip?zip={usr_list[0]},{usr_list[1]}&appid" \
                          f"={api_key}"
                    print(f"url={url}")

                elif len(usr_list) == 3:
                    print("City")
                    # http://api.openweathermap.org/geo/1.0/direct?q=Omaha&limit=5&appid=fe5cc61799dd4704e63e6fc3feb3f713
                    if usr_list[2].lower() == 'us':
                        url = f"{url}direct?q={usr_list[0]},{usr_list[1]}," \
                              f"{usr_list[2]}&limit=5&appid" \
                              f"={api_key}"
                    else:
                        url = f"{url}direct?q={usr_list[0]}," \
                              f"{usr_list[2]}&limit=5&appid" \
                              f"={api_key}"

                    print(f"url={url}")

                elif len(usr_list) == 1 and usr_list[0].isnumeric():
                    print ("Zip Code Only")
                    # http://api.openweathermap.org/geo/1.0/zip?zip=68130&appid=fe5cc61799dd4704e63e6fc3feb3f713
                    url = f"{url}zip?zip={usr_list[0]}&appid={api_key}"
                    print(f"url={url}")

                elif len(usr_list) == 2 and not usr_list[0].isnumeric():
                    # http://api.openweathermap.org/geo/1.0/direct?q=Pune,IND&limit=1&appid=fe5cc61799dd4704e63e6fc3feb3f713
                    #-City name, state code (only for the US) and country code divided by comma. Please use ISO 3166 country codes.
                    url = f"{url}direct?q={usr_list[0]},{usr_list[1]}" \
                          f"&limit=5&appid={api_key}"
                    print(f"url={url}")
                    print("Hello")
                else:
                    print("Invalid Input, Please insert comma seperated values "
                          "and city name with state.")
            # try:
            #     r = requests.get(
            #         'https://api.chucknorris.io/jokes/random?category=animal')
            #     r.raise_for_status()
            # except requests.exceptions.HTTPError as err_http:
            #     print(f"Error code {r.status_code} - "
            #           f"requests.exceptions.HTTPError")
            # except requests.exceptions.ConnectionError as err_conn:
            #     print(f"Error code {r.status_code} - "
            #           f"requests.exceptions.ConnectionError")
            # except requests.exceptions.RequestException as err_exp:
            #     print(f"Error code {r.status_code} - "
            #           f"requests.exceptions.RequestException")
            #
            # if r.status_code == 200 :
            #     data = r.json()
            #     #-- Calling func_pprint() for formatted output.
            #     func_pprint(data)
