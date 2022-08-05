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
    expected = {"Brave Bull Shooter": ["Tequila", "Tabasco sauce"],
                "Tequila Surprise": ["Tequila", "Tabasco sauce"]}
    actual = cocktails.get_all_cocktails(["Tequila", "Tabasco sauce"])

    assert expected == actual
