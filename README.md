# cocktails

Command line application to find possible cocktails from inputting a list of ingredients

## Usage

The application takes a single command 'ingredients' and expects a list of ingredients. 
```
python cocktails.py --ingredients "Ingredient1, Ingredient 2, ..."
```

### Example:
```
python cocktails.py --ingredients "Tequila, Tabasco sauce"
```
Should print in the terminal:
```Your possible cocktails are:
Tequila Surprise: Tequila, Tabasco sauce
Brave Bull Shooter: Tequila, Tabasco sauce
```
Where the first part is the name of the cocktail and the second part is a list of ingredients

## Testing

Tests are found in test_cocktails.py and can be run using the following command:
```
pytest test_cocktails.py
```


**_NOTE:_** This application only runs with Python3