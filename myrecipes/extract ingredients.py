import csv
import sys
import requests
from bs4 import BeautifulSoup

url = "https://world.openfoodfacts.org/entry-date/2016-08/ingredients"
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")


# Find the HTML elements that contain the ingredient information
ingredients_list = soup.find_all("a", class_="tag known")

# Extract the ingredient names
ingredient_names = [ingredient.text for ingredient in ingredients_list]


with open('openfoodfact_ingredient_list.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for ingredient_name in ingredient_names:
        writer.writerow([ingredient_name.encode(sys.stdout.encoding, errors='replace').decode(sys.stdout.encoding)])
