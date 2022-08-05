import cocktails


def test_returns_correct_cocktails_by_ingredient():
    expected = set(["Brave Bull Shooter", "Tequila Surprise", "Fahrenheit 5000"])
    actual = cocktails.get_cocktails_by_ingredient("Tabasco sauce")

    assert expected == actual


def test_returns_correct_ingredients_in_cocktails():
    expected = ["Tequila", "Triple sec", "Lime juice", "Salt"]
    actual = cocktails.get_ingredients_in_cocktail("Margarita")

    assert expected == actual


def test_returns_correct_cocktails():
    ingredients = ["Lime", "Light rum", "Mint", "Sugar",
                   "Tequila", "Lime juice", "Triple sec",
                   "Tabasco sauce", "Salt", "Soda water"]
    expected = {"Mojito": ["Light rum", "Lime", "Sugar", "Mint", "Soda water"],
                "Frozen Mint Daiquiri": ["Light rum", "Lime juice", "Mint", "Sugar"],
                "Margarita": ["Tequila", "Triple sec", "Lime juice", "Salt"],
                "Brave Bull Shooter": ["Tequila", "Tabasco sauce"],
                "Tequila Surprise": ["Tequila", "Tabasco sauce"]}
    actual = cocktails.get_all_cocktails(ingredients)

    assert expected == actual


def test_incorrect_ingredient_returns_empty():
    ingredients = "dafasfa"
    expected = {}
    actual = cocktails.get_all_cocktails(ingredients)

    assert expected == actual
