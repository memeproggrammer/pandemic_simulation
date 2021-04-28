import random
city_size = ['small, population 4000', 'medium, population 9000', 'large, population 100,000', 'giant, population 900,000']
print ("city size:")
city = random.choice(city_size)
print (city)
enter = input("press enter to continue")
small = ("small, population 4000")
medium = ("medium, population 9000")
large = ("large, population 100,000")
giant = ("giant, population 900,000")
if city == small:
    infection_possible = ['4000 people', '3000 people', '2000 people', '1000 people']
    infected = random.choice(infection_possible)
    precautions = ['masks', 'online meetings', 'wash hands', 'no driving with other people']
    precation = random.choice(precautions)
    a = ("masks")
    b = ("online meetings")
    c = ("wash hands")
    d = ("no driving with other people")
    if precation == a:
        money = ("9000$")
    elif precation == b:
        money = ("4000$")
    elif precation == c:
        money = ("3000$")
    elif precation == d:
        money = ("2000$")
elif city == medium:
    infection_possible = ['5000 people', '6000 people', '7000 people', '8000 people', '100,000 people']
    infected = random.choice(infection_possible)
    precautions = ['masks', 'online meetings', 'wash hands', 'no driving with other people']
    precation = random.choice(precautions)
    a = ("masks")
    b = ("online meetings")
    c = ("wash hands")
    d = ("no driving with other people")
    if precation == a:
        money = ("11,000$")
    elif precation == b:
        money = ("6000$")
    elif precation == c:
        money = ("5000$")
    elif precation == d:
        money = ("4000$")
elif city == large:
    infection_possible = ['6000 people', '7000 people', '8000 people', '9000 people', '9000 people']
    infected = random.choice(infection_possible)
    precautions = ['masks', 'online meetings', 'wash hands', 'no driving with other people']
    precation = random.choice(precautions)
    a = ("masks")
    b = ("online meetings")
    c = ("wash hands")
    d = ("no driving with other people")
    if precation == a:
        money = ("10,000$")
    elif precation == b:
        money = ("5000$")
    elif precation == c:
        money = ("4000$")
    elif precation == d:
        money = ("3000$")
elif city == giant:
    infection_possible = ['8000 people', '9000 people', '10,000 people', '20,000 people', '900,000 people']
    infected = random.choice(infection_possible)
    precautions = ['masks', 'online meetings', 'wash hands', 'no driving with other people']
    precation = random.choice(precautions)
    a = ("masks")
    b = ("online meetings")
    c = ("wash hands")
    d = ("no driving with other people")
    if precation == a:
        money = ("12,000$")
    elif precation == b:
        money = ("7000$")
    elif precation == c:
        money = ("6000$")
    elif precation == d:
        money = ("5000$")
enter = input("press enter to show results")
print ("infected:")
print (infected)
print ("precaution:")
print (precation)
print ("money spent:")
print (money)

































