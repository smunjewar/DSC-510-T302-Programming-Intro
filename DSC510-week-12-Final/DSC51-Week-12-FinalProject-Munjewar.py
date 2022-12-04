import os
import string
import datetime as dt
import requests
# import pprint
# ------------------------------------------------------------------------#
# Title          : Week-12-Final Project.
# Author         : Sheetal Munjewar
# University     : College of Science and Technology, Bellevue University
# Course         : DSC 510 T302 Introduction to Data Science (2227-1)
# Professor      : Michael Eller
# Initial Draft  : 11/06/2022
# Change History : 11/12/2022 - defined function for kelvin to C/F conversion.
# Change History : 11/14/2022 - Rewrite code execution logic without internet.
# Change History : 11/15/2022 - Removed function - func_kelvin_conversion,
#                               API itself will have options to get o/p in C/F.
# Change History : 11/16/2022 - Defined cloud coverage using if block in
#                               print function.
#
#-------------------------------------------------------------------------#
# Note : Program must expect API in seperate file called : api_key
#-------------------------------------------------------------------------#

#--Pretty Print function wiht one input parmater, no return value.
def func_print_forecast(response):
    # CITY = "Omaha"
    CITY = response['name']
    temp_fahrenheit = response['main']['temp']
    temp_max = response['main']['temp_max']
    temp_min = response['main']['temp_min']
    pressure = response['main']['pressure']
    feels_like_kelvin = response['main']['feels_like']
    temp_humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']
    cloud = response['clouds']['all']
    #-- Declare conditions
    #-- Under 30 -Clear Sky
    #-- Between 30 and 60 - Partial Cloud Cover
    #-- Above 60 - Full Cloud Cover
    if cloud == "" or cloud is None or cloud <= 30:
        cloud_desc = "Clear Sky."
    elif cloud == "" or cloud is None or cloud <= 60:
        cloud_desc = "Partial Cloud Cover"
    else:
        cloud_desc = "Full Cloud Cover."
    temp_description = response['weather'][0]['description']
    sunrise = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] +
                                           response['timezone'])
    sunset = dt.datetime.utcfromtimestamp(response['sys']['sunset'] +
                                           response['timezone'])

    print(f'\n{f"":-<70}')
    print(f'{f"{CITY} temperature forecast :":<50}')
    print(f'{f"":-<70}')
    print(f'{f"Current temperature ":>30}:'
          f' {((temp_fahrenheit - 32)*5/9):.2f}°C'
          f' or {temp_fahrenheit:.2f}°F')
    print(f'{f"Max temperature ":>30}: {((temp_max - 32)*5/9):.2f}°C'
          f' or {temp_max:.2f}°F')
    print(f'{f"Min temperature ":>30}: {((temp_min - 32)*5/9):.2f}°C'
          f' or {temp_min:.2f}°F')
    print(f'{f"Humidity ":>30}: {temp_humidity:.2f}%')
    print(f'{f"Wind Speed ":>30}: {wind_speed:.2f}m/s')
    print(f'{f"Pressure ":>30}: {pressure}hPa')
    print(f'{f"Cloud Coverage ":>30}: {cloud_desc}')
    print(f'{f"Sun Rises at ":>30}: {sunrise} local time.')
    print(f'{f"Sun Set at ":>30}: {sunset} local time.')
    print(f'{f"General Weather ":>30}: {temp_description}')
    print(f'{f"":-<70}')

# def func_kelvin_conversion(kelvin):
#     celsius = kelvin - 273.15
#     fahrenheit = celsius * (9/5) + 32
#     return celsius, fahrenheit

def func_welcome():
    print(f'\n{"":-<70}')
    print(f'{"OpenWeatherApp UI (Search scope limited to US only.)": ^70}')
    print(f'{"":-<70}')
    print(f'{"Expected inputs - City,State or Zip Code ":<70}')
    print(f'{"Example : City,State - Omaha,NE":<70}')
    print(f'{"Example : Zip Code - 68130":<70}')
    # print(f'{"Invalid inputs will lead to unexpected results":<50}')
    print(f'{"":-<70}')

#-- func_get_api() will accept one input parameter - url.
#-- Function will call api url using requests to get dict or list in return.
def func_get_api(url):
    try:
        # print(f'url:{url}')
        r = requests.get(url)
        # r.raise_for_status()
    except requests.exceptions.HTTPError as err_http:
        print(f"HTTPError error encountered, Please try again !")
        print(f"Error Message : {err_http}")
        return 400
    except requests.exceptions.ConnectionError as err_conn:
        print(f"ConnectionError error encountered, Please try again !")
        print(f"Error Message : {err_conn}")
        return 400
    except requests.exceptions.RequestException as err_exp:
        print(f"Exception encountered, Please try again !")
        print(f"Error Message : {err_conn}")
        return 400

    if r.status_code == 200 :
        data = r.json()
        # print("Hey")
        return data

#-- func_api_call() will accept three input parameters.
#-- function will concat base URL with lat and lon values and return URL.
def func_api_call(BASE_URL,lat,lon):
    # api_url = f"{BASE_URL}lat={lat}&lon={lon}&appid={API_KEY}"
    # For temperature in Fahrenheit use units = imperial
    # For temperature in Celsius use units = metric
    api_url = f"{BASE_URL}lat={lat}&lon={lon}&appid={API_KEY}&units=imperial"
    # print(api_url)
    return api_url

#-- func_usr_input() will accept user input and return GEO URL
#-- based on inputs.
def func_usr_input():
    #-- Define empty list:
    usr_list = []
    #--Making to function func_welcome(), to display options.
    func_welcome()
    u_list = input("Enter City Name,State or Zip Code: ").split(",")
    #-- parse list elements to strip blank spaces.
    usr_list = [ele for ele in u_list if ele.strip()]

    if len(usr_list) == 1 and usr_list[0].isnumeric():
        # print ("Zip Code Only")
        # http://api.openweathermap.org/geo/1.0/zip?zip=68130&appid=fe5cc61799dd4704e63e6fc3feb3f713
        url = f"{GEO_URL}zip?zip={usr_list[0]}&appid={API_KEY}"
        return url
        # print(f"url={url}")

    elif len(usr_list) == 2 and not usr_list[0].isnumeric():
        # print("Omaha,NE - May not work !")
        # http://api.openweathermap.org/geo/1.0/direct?q=Pune,IND&limit=1&appid=fe5cc61799dd4704e63e6fc3feb3f713
        #-City name, state code (only for the US) and country code divided by comma. Please use ISO 3166 country codes.
        # print(f'GEO_URL : {GEO_URL}')
        url = f"{GEO_URL}direct?q={usr_list[0]},{usr_list[1]},US" \
              f"&appid={API_KEY}"
        # print(f"url={url}")
        return url

    else:
        print(f"Invalid Input- {usr_list}, Please try again.")
        # print(usr_list)
        return None

def main():

    """Create a header for your program just as you have in the past.
    Create a Python Application which asks the user for their zip code or city (Your program must perform both a city and a zip lookup). You must ask the user which they want to perform with each iteration of the program.
    Use the zip code or city name in order to obtain weather forecast data from OpenWeatherMap.
    Display the weather forecast in a readable format to the user. Do not display the weather data in Kelvin, since this is not readable to the average person.  You should allow the user to choose between Celsius and Fahrenheit and ideally also Kelvin.
    Use comments within the application where appropriate in order to document what the program is doing. Comments should add value to the program and describe important elements of the program.
    Use functions including a main function and a properly defined call to main. You should have multiple functions.
    Allow the user to run the program multiple times to allow them to look up weather conditions for multiple locations.
    Validate whether the user entered valid data. If valid data isn’t presented notify the user. Your program should never crash with bad user input.
    Use the Requests library in order to request data from the webservice.
    Use Try blocks to ensure that your request was successful. If the connection was not successful display a message to the user.
    Use Python 3
    Use try blocks when establishing connections to the webservice. You must print a message to the user indicating whether or not the connection was successful.
    You must have proper coding convention including proper variable names (See PEP8)."""

    """Start early.  Ask lots of questions when you don’t understand something.  It’s far better to get clarity then to not meet requirements.
    Be creative.  This assignment is a real-world program.  Use it as an opportunity to improve your knowledge and showcase what you’ve learned.
    Sign up for API Key http://openweathermap.org/appid
    The API key will look something similar to this: d5751b1a9e2e4b2b8c7983646072da8b
    Make a connection to the API using the Requests library.
    You MUST do a GEO Lookup first then do a weather lookup using the latitude and longitude.  This will require you to do 2 API calls.  One call will be to obtain the LAT and LON and the other will be to get the weather using the LAT and LON.
    READ all of the OpenWeather GEOCode and Weather Lookup API documentation.  Most of the questions you have can be answered by the API documentation. 
    Make sure that your try blocks are solid.  Don’t include huge blocks of code in the try blocks.  Don’t use generic exceptions.  Take a look at the request documentation on the various exceptions you can catch for HTTP connections.  You should have specific exceptions with meaningful messages for the end user to make adjustments.
    Make sure you have request specific exceptions.  Your code should not throw any unhandled exceptions.
    Make sure that your program allows a user to do a zip code weather lookup and a city/state lookup.  You must give them the option and I will test both.  For city you should ask the user to enter a state, otherwise there’s no way to distinguish between Omaha TX, Omaha AR, and Omaha NE.
    I will put gibberish in your prompts.  This is an example of non happy path testing and is a real-world testing scenario.  Make sure you have lots of validation to test those scenarios.  If you ask the user to enter a number for a menu how will your program respond if the user enters characters for instance.
    Make sure that your program has really good comments.  Comments should be meaningful and provide value for other developers looking at your code.
    Make sure you follow PEP8 guidelines.  Don’t use single variable names etc…
    Make sure to review the requests library
    Level of effort counts.  Make sure you’re putting your all into this final program. 
    Make sure to keep in mind function structure.  Your program should have functions that serve value by encapsulating specific pieces of functionality.
    Make sure you have a proper call to main."""

    '''Current Weather Conditions For Omaha
    Current Temp: 30.87 degrees
    High Temp: 33.24 degrees
    Low Temp: 29.05 degrees
    Pressure: 1022hPa
    Humidity: 74%
    Cloud Cover: Full Cloud Cover
    Description: overcast clouds'''

#-- Variable declarations
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
GEO_URL = "http://api.openweathermap.org/geo/1.0/"
#-- API key will get fetched from file called : api_key.
API_KEY  = open('api_key','r').read().rstrip()

while True:
    usr_input = input("OpenWeather UI, Press y to continue and q to quit(): ")
    # print(len(usr_input))
    # print(usr_input.lower())
    if usr_input.lower() == 'q':
        print("Thanks for visiting !")
        break
    elif len(usr_input) == 0 or usr_input.strip().lower() != 'y' :
        print(f"Invalid Input : {usr_input}, Please try again.")
    else:
        get_url = func_usr_input()
        if get_url is None:
            print(f'Return Code - {get_url}')
        else:
            # print(get_url)
            lat = 0.0
            lon = 0.0
            #-- Will Return dict to fetch lat and log.
            # print(f'get_url:{get_url}')
            #-- Call function func_get_api()
            ret_code = func_get_api(get_url)
            #-- to check return value must be dict and non-empty.
            # print(ret_code)
            # print(bool(ret_code))

            if type(ret_code) is list and not ret_code:
                print(f"No result found, try again.")
                # print(f"No result found, Empty list : {ret_code}!")

            elif type(ret_code) is dict and not bool(ret_code):
                print(f"No result found, try again.")
                # print(f"No result found, Empty Dictionary : {ret_code}!")

            elif type(ret_code) is dict or type(ret_code) is list:
                if type(ret_code) is dict and bool(ret_code):
                    # print("Dictionary")
                    lat = ret_code['lat']
                    lon = ret_code['lon']
                #-- Check for non-empyt list.
                elif type(ret_code) is list and ret_code:
                     # print("List")
                     lat = ret_code[0]['lat']
                     lon = ret_code[0]['lon']

                #-- Once you derivied lon and lat
                base_api_url = func_api_call(BASE_URL,lat,lon)
                # print(base_api_url)
                base_api_dict = func_get_api(base_api_url)
                func_print_forecast(base_api_dict)

            elif ret_code is None or ret_code > 200:
                print(f'Result not found or Invalid Input,'
                      f'please try again.')

            else:
                print(f"Empty List or Dictionary - Please try again.")

if __name__ == "__main__": main()
