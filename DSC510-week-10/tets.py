import requests
import pprint


'''Create a program which uses the Request library to make a GET request of the following API: Chuck Norris Jokes.
The program will receive a JSON response which includes various pieces of data. You should parse the JSON data to obtain the “value” key. The data associated with the value key should be displayed for the user (i.e., the joke).
Your program should allow the user to request a Chuck Norris joke as many times as they would like. You should make sure that your program does error checking at this point. If you ask the user to enter “Y” and they enter y, is that ok? Does it fail? If it fails, display a message for the user. There are other ways to handle this. Think about included string functions you might be able to call.
Your program must include a header as in previous weeks.
Your program must have a properly defined main method and a properly defined call to main.
Your program should adhere to PEP8 guidelines especially as it pertains to variable names.
Your program must include a welcome message for the user.
Your program must generate “pretty” output. Simply dumping a bunch of data to the screen with no context doesn’t represent “pretty.”
'''
print("Welcome to Chuck Norris Web Jokes ")
while True:
    usr_input = input("Enter Y/y to conitnue : ")
    print(len(usr_input))
    print(usr_input.lower())
    if len(usr_input) == 0 or usr_input.lower() != 'y' :
        print ("Invalid Input : {}, Please try again".format(usr_input))
    else:
        break


try:
    r = requests.get('https://api.chucknorris.io/jokes/random')
except TimeoutError as e:
    print(e)
except AttributeError as e:
    print(e)
except NameError as e:
    print("NameError : {}".format(e))
# import json
# r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
# r = requests.get('https://api.chucknorris.io/jokes/random')
# print(r.status_code)
# print(type(r))
# print(dir(r))
data = r.json()
# print(type(data))
# print(data)

print(data['value'])
print("Printing dictionary data using pprint : ")
pprint.pprint(data)
print("Printing dictionary data without using pprint : ")
print(data)
#
# for key_values in data:
#     print(data[key_values])
    # if key_values.lower() == 'value':
    #     print("Joke of the day : {}".format(data['value']))

