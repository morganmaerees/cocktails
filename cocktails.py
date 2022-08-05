"""
Command lind script to find possible cocktails from inputting a list of ingredients
"""

import requests
import argparse


def get_all_cocktails(ingredients):
    """
    Gets all possible cocktails from list of ingredients
    :param ingredients: List of ingredients
    :return: dictionary mapping cocktails to the ingredients
    """
    # Get all possible cocktails for each ingredient

    possible_cocktails = set()
    missing_ingredient_cocktails = set()
    for item in ingredients:
        possible_cocktails = possible_cocktails.union(get_cocktails_by_ingredient(item))

    # Find all ingredients in each cocktail, if cocktail contains any
    # Additional ingredients, add it to missing_ingredients set
    detailed_cocktails = {}
    for cocktail in possible_cocktails:
        cocktail_ingredients = get_ingredients_in_cocktail(cocktail)
        i = 0
        while i < len(cocktail_ingredients):
            if cocktail_ingredients[i] not in ingredients:
                missing_ingredient_cocktails.add(cocktail)
                break
            i += 1
        detailed_cocktails[cocktail] = cocktail_ingredients

    # Remove Cocktail from dictionary of cocktails if any ingredient is missing from provided list
    possible_cocktails = list(possible_cocktails - missing_ingredient_cocktails)
    final_cocktails = {k:v for k, v in detailed_cocktails.items() if k in possible_cocktails}
    return final_cocktails


def get_ingredients_in_cocktail(cocktail):
    """
    Gets all ingredients within a cocktail
    :param cocktail: Name of the cocktail
    :return: List of ingredient names
    """
    cocktails_url = cocktail.replace(" ", "_")
    response = requests.get(f"https://thecocktaildb.com/api/json/v1/1/search.php?s={cocktails_url}")
    drinks = response.json()['drinks']
    ingredients = []
    for drink in drinks:
        if drink['strDrink'] == cocktail:
            # API returns list of up to 15 ingredients,
            # If not None, add to list of ingredients
            for i in range(1, 16):
                if drink[f'strIngredient{i}']:
                    ingredients.append(drink[f'strIngredient{i}'])
    return ingredients


def get_cocktails_by_ingredient(ingredient):
    """
    Gets all cocktails which contain a specific ingredient
    :param ingredient: Name of the ingredient
    :return: List of cocktail names
    """
    # Get all cocktails with specific ingredient
    ingredient_url = ingredient.replace(" ", "_")
    response = requests.get(f"https://thecocktaildb.com/api/json/v1/1/filter.php?i={ingredient_url}")
    cocktails = set()
    drinks = response.json()['drinks']
    for item in drinks:
        cocktails.add((item['strDrink']))
    return cocktails


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ingredients', action='store', type=str, required=True)
    args = vars(parser.parse_args())
    if "ingredients" in args.keys():
        args["ingredients"] = [s.strip() for s in args["ingredients"].split(",")]
    ingredients = args["ingredients"]
    cocktails = get_all_cocktails(ingredients)
    print(f"Your possible cocktails are:")
    for k, v in cocktails.items():
        val = ', '.join(str(ingredient) for ingredient in v)
        print(f"{k}: {val}")


