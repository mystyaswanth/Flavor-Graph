from collections import defaultdict

# ------------------ Sample dataset ------------------
RECIPES = {
    "Spaghetti Aglio e Olio": ["spaghetti", "garlic", "olive oil", "red pepper flakes", "parsley", "salt"],
    "Tomato Basil Pasta": ["pasta", "tomato", "basil", "garlic", "olive oil", "salt", "pepper"],
    "Veggie Stir Fry": ["rice", "soy sauce", "garlic", "ginger", "broccoli", "carrot", "bell pepper", "sesame oil"],
    "Chicken Curry": ["chicken", "onion", "garlic", "ginger", "curry powder", "tomato", "coconut milk"],
    "Omelette": ["eggs", "milk", "butter", "salt", "pepper", "cheese"],
    "Pancakes": ["flour", "milk", "egg", "baking powder", "sugar", "butter"],
    "Guacamole": ["avocado", "lime", "salt", "onion", "cilantro", "tomato"],
    "Tuna Salad": ["tuna", "mayonnaise", "onion", "celery", "lemon", "salt", "pepper"],
    "Grilled Cheese": ["bread", "butter", "cheese"],
    "Greek Salad": ["tomato", "cucumber", "olive oil", "feta", "olives", "onion", "oregano"],
}

SUBSTITUTIONS = {
    "milk": ["plant milk", "water+milk powder"],
    "butter": ["olive oil", "margarine"],
    "egg": ["flax egg (1 tbsp flax + 3 tbsp water)", "banana (for pancakes)"],
    "cheese": ["nutritional yeast (for flavor)", "vegan cheese"],
    "soy sauce": ["tamari", "coconut aminos"],
    "coconut milk": ["heavy cream", "yogurt+water"],
    "tuna": ["chickpeas", "salmon"],
    "chicken": ["tofu", "chickpeas"],
}

def build_bipartite(recipes):
    r2i = {r: set(ings) for r, ings in recipes.items()}
    i2r = defaultdict(set)
    for r, ings in r2i.items():
        for ing in ings:
            i2r[ing].add(r)
    return r2i, dict(i2r)

R2I, I2R = build_bipartite(RECIPES)
