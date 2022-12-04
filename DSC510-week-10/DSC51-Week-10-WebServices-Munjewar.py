# import os
# import string
import requests
import pprint
# ------------------------------------------------------------------------#
# Title         : Week-10-WebServices.
# Author        : Sheetal Munjewar
# University    : College of Science and Technology, Bellevue University
# Course        : DSC 510 T302 Introduction to Data Science (2227-1)
# Professor     : Michael Eller
# Initial Draft : 11/06/2022
#-------------------------------------------------------------------------#
#-- Reference link :
#-- https://www.youtube.com/watch?v=ULv9x0GQFbw ( How to handle exception in
# requests )

#--Pretty Print function wiht one input parmater, no return value.
def func_pprint(data):
    # print(data)
    #-- Formatting using ppprint
    pprint.pprint(data,depth=2, indent=4, width=180, sort_dicts=False)
    #-- Formatting using print
    print("\n")
    print(" {:->80} ".format(""))
    print(" {:>20} {} ".format("Character :","Chuck Norris"))
    print(" {:>20} {} ".format("Request Timestamp :",data['created_at']))
    print(" {:>20} {} ".format("categories :",data['categories'][0]))
    print(" {:>20} {} ".format("Joke :",data['value']))
    print(" {:->80} ".format(""))

def main():
    '''Create a program which uses the Request library to make a GET request of
    the following API: Chuck Norris Jokes. The program will receive a JSON
    response which includes various pieces of data. You should parse the JSON
    data to obtain the “value” key. The data associated with the value key
    should be displayed for the user (i.e., the joke).
    Your program should allow the user to request a Chuck Norris joke as many
    times as they would like. You should make sure that your program does error
    checking at this point. If you ask the user to enter “Y” and they enter y,
    is that ok? Does it fail? If it fails, display a message for the user.
    There are other ways to handle this. Think about included string functions
    you might be able to call.
    Your program must include a header as in previous weeks.
    Your program must have a properly defined main method and a properly
    defined call to main.
    Your program should adhere to PEP8 guidelines especially as it pertains
    to variable names.
    Your program must include a welcome message for the user.
    Your program must generate “pretty” output. Simply dumping a bunch of data
    to the screen with no context doesn’t represent “pretty.”
    '''

print("Welcome to Chuck Norris Jokes webpage :")
while True:
    usr_input = input("\nTo fetch the joke, press 'y' to cont. or 'q' to "
                      "quit: ")
    # print(len(usr_input))
    # print(usr_input.lower())
    if usr_input.lower() == 'q':
        print("Thanks for visiting !")
        break
    elif len(usr_input) == 0 or usr_input.strip().lower() != 'y' :
        print ("Invalid Input : {}, Please try again".format(usr_input))
    else:
            try:
                r = requests.get(
                    'https://api.chucknorris.io/jokes/random?category=animal')
                r.raise_for_status()
            except requests.exceptions.HTTPError as err_http:
                print(f"Error code {r.status_code} - "
                      f"requests.exceptions.HTTPError")
            except requests.exceptions.ConnectionError as err_conn:
                print(f"Error code {r.status_code} - "
                      f"requests.exceptions.ConnectionError")
            except requests.exceptions.RequestException as err_exp:
                print(f"Error code {r.status_code} - "
                      f"requests.exceptions.RequestException")

            if r.status_code == 200 :
                data = r.json()
                #-- Calling func_pprint() for formatted output.
                func_pprint(data)

if __name__ == "__main__": main()
