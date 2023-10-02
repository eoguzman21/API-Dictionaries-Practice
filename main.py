#rest apis
#application programming interface
import requests #requests something from the internet
import json #json stands for javascript object notation 

response = requests.get("https://randomuser.me/api/")
# print(response.json())
gender = response.json()["results"][0]["gender"]
print(gender)
title = response.json()["results"][0]["name"]["title"]
# get the first name
# get that last name
# get the email
# get the phone number
# get the city
# get the postal code
# get the street address
# get date of birth
# get the login user id
# get the registered age
first_name = response.json()["results"][0]["name"]["first"]
print(first_name)
last_name = response.json()["results"][0]["name"]["last"]
print(last_name)
email = response.json()["results"][0]["email"]
print(email)
phone_num = response.json()["results"][0]["phone"]
print(phone_num)
city = response.json()["results"][0]["location"]["city"]
print(city)
postal_code = response.json()["results"][0]["location"]["postcode"]
print(postal_code)
address = response.json()["results"][0]["location"]["street"]
print(address)
dob = response.json()["results"][0]["dob"]["date"]
print(dob)
login_id = response.json()["results"][0]["login"]["uuid"]
print(login_id)
age = response.json()["results"][0]["dob"]["age"]
print(age)