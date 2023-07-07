import csv
import pandas as pd
import re
import inflect


def extract_matching_ingredients(text):
    matching_ingredients = []
    df = pd.read_csv('myrecipes/openfoodfact_ingredient_list.csv', header=None)
    ingredients = df.iloc[:, 0].str.lower().unique()
    p = inflect.engine()
    for ingredient in ingredients:
        pattern = r'\b{}\b'.format(re.escape(ingredient))
        if re.search(pattern, text, re.IGNORECASE):
            if ingredient not in matching_ingredients:
                matching_ingredients.append(ingredient.lower())

        singular = p.singular_noun(ingredient)
        plural = p.plural_noun(ingredient)

        if singular and re.search(r'\b{}\b'.format(re.escape(singular)), text, re.IGNORECASE):
            if singular not in matching_ingredients:
                matching_ingredients.append(singular.lower())

        if plural and re.search(r'\b{}\b'.format(re.escape(plural)), text, re.IGNORECASE):
            singular_plural = p.singular_noun(plural)
            if singular_plural and singular_plural not in matching_ingredients:
                matching_ingredients.append(singular_plural.lower())

    return matching_ingredients


def add_ingredient(new_ingredients):
    with open('myrecipes/openfoodfact_ingredient_list.csv', 'r') as file:
        reader = csv.reader(file)
        existing_ingredients = [row[0] for row in reader]
    with open('myrecipes/openfoodfact_ingredient_list.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        for item in new_ingredients:
            if item not in existing_ingredients:
                writer.writerow([item])


if __name__ == '__main__':
    text = """Carrots peeled and cut into 1cm chunks 200 g
Potato peeled & cut into rough chunks 650 g
Milk 60 ml
Butter 20 g
"""

    text2 = """Precooked Pizza Base or 8 slices of English bread 2
Basilico Sauce 1 jar
Mozzarella shredded 100 g 
Basil Leaves 8
Olive Oil 20 ml
Salt
Pepper
"""
    print(extract_matching_ingredients(text2))
