# Dictionaries in Python
# A dictionary is a collection of key-value pairs. 
# It is mutable, meaning it can be changed after it's created.
# It is unordered, meaning the order of the key-value pairs is not guaranteed. 

from typing import Dict, Union, Optional
import pprint

key = Union[int, str] # Create Custom type
value = Union[int, str, dict, set, tuple]

data : Dict[key,value] = {
    "name" : "Muhammad Afzal",
    "age" : "27",
    "city" : "Nankana Sahib",
    "country" : "Pakistan",
    "hobbies" : {"reading", "writing", "coding"},
    "education" : "Masters in Computer Science"
}
pprint.pprint(data)

car : Dict[key,value] = {
    "brand" : "Toyota",
    "model" : "Corolla",
    "year" : 2015,
    "color" : "Black",
    "mileage" : 50000,
    "features" : {"air_conditioner", "power_steering", "anti_lock_brakes"}
}
pprint.pprint(car["brand"])
