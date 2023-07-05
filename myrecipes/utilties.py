import re
import pandas as pd
import nltk
from nltk.stem import SnowballStemmer
nltk.download('punkt')
nltk.download('stopwords')


def extract_matching_ingredients(text):
    stemmer = SnowballStemmer('english')
    matching_ingredients = []
    df = pd.read_csv('myrecipes/updated_ingredients.csv', header=None)
    ingredients = df.iloc[:, 0]
    for ingredient in ingredients:
        stemmed_ingredient = stemmer.stem(ingredient)
        pattern = r'\b{}\b'.format(re.escape(stemmed_ingredient))
        if re.search(pattern, text, re.IGNORECASE):
            if ingredient not in matching_ingredients:
                matching_ingredients.append(ingredient.lower())
    return matching_ingredients


if __name__ == '__main__':
    text = """Carrot peeled and cut into 1cm chunks 200 g
Potato peeled & cut into rough chunks 650 g
Milk 60 ml
Butter 20 g
"""
    print(extract_matching_ingredients(text))
