import requests
from django.core.exceptions import ValidationError

def not_valid_breed(value):

    print(value)

    response = requests.get("https://api.thecatapi.com/v1/breeds")

    if response.status_code != 200:
        raise ValidationError("Something went wrong")
    
    breeds = {item['name'] for item in response.json()}

    if value not in breeds:
        return True
    
    return False


