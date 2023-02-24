import requests

text = 'My email address is spy@ninja.com and my number is +1 (650) 123-4567 so call me maybe?'

response = requests.post('http://localhost:8000/parse', {'locale': 'en_US', 'text': text})

entities = response.json()

for entity in entities:
    print( entity['dim'] +": "+ entity['body'])


# credit card info
text = 'Last Christmas I gave you my card 4111-1111-1111-1111 But the very next day you gave it away'

response = requests.post('http://localhost:8000/parse', {'locale': 'en_US', 'text': text, 'dims': ["credit-card-number"]})

entities = response.json()

for entity in entities:
    print( entity['dim'] +": "+ entity['body'])
