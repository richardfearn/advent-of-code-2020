from utils import to_lines
from operator import itemgetter
from collections import namedtuple

Food = namedtuple("Food", ["ingredients", "allergens"])


def parse(lines):

    if isinstance(lines, str):
        lines = to_lines(lines)

    return [parse_food(line) for line in lines]


def parse_food(line):
    (ingredients, allergens) = line.split(" (contains ")
    ingredients = set(ingredients.split(" "))
    allergens = set(allergens[:-1].split(", "))
    return Food(ingredients, allergens)


def part_1(lines):
    foods = parse(lines)
    find_ingredients_and_allergens(foods)
    return sum([len(food.ingredients) for food in foods])


def part_2(lines):
    foods = parse(lines)
    ingredient_allergens = find_ingredients_and_allergens(foods)
    sorted_ingredients = [item[0] for item in sorted(ingredient_allergens.items(), key=itemgetter(1))]
    return ",".join(sorted_ingredients)


def find_ingredients_and_allergens(foods):

    all_ingredients = set(i for food in foods for i in food.ingredients)
    all_allergens = set(a for food in foods for a in food.allergens)

    ingredient_allergens = {}

    remaining_allergens = set(all_allergens)

    finished = False
    while not finished:

        # Find an allergen that is definitely associated with only one ingredient
        result = None

        for allergen in remaining_allergens:

            # Don't care about ingredients for which we already know the allergen
            ingredients = all_ingredients.difference(ingredient_allergens.keys())

            for food in foods:
                if allergen in food.allergens:
                    ingredients = ingredients.intersection(food.ingredients)

            if len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                result = (ingredient, allergen)

        if result is not None:

            (ingredient, allergen) = result
            ingredient_allergens[ingredient] = allergen
            remaining_allergens.remove(allergen)

            for food in foods:
                food.ingredients.discard(ingredient)
                food.allergens.discard(allergen)

        else:
            finished = True

    return ingredient_allergens
