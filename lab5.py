from re import S, X


def describe_city(city, country):
    """Function to tell what country a city is in"""
    print(f"{city} is in {country}")

describe_city ('Belfast', 'Northern Ireland')

def prod_num(numbers):
   s=0
   for x in numbers:
    s+=x 
   return s

s = prod_num([10,4,1])
print(s)

def describe_country(place, country):
    print(f"{place} is in {country}")

describe_country('Liverpool', 'England')
