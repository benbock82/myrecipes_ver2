import requests

url = 'https://api.spoonacular.com/food/search'
params = {
    'apiKey': '2f1d8ee965434c5e8a73402c8eda8466',
    'query': 'your_search_query'
}

response = requests.get(url, params=params)

if response.status_code == 200:
    # Request successful
    data = response.json()
    # Process the data as needed
else:
    # Request failed
    print('Error:', response.status_code)
