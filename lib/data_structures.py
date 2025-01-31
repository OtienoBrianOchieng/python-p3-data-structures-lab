spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]
 

def get_names(spicy_foods):

    names = [food["name"] for food in spicy_foods ]
    return names


def get_spiciest_foods(spicy_foods):

    foods_dict = [food for food in spicy_foods if food["heat_level"] > 5]
    return foods_dict




def print_spicy_foods(spicy_foods):
        for food in spicy_foods:
            name = food["name"]
            cuisine = food["cuisine"]
            heat_level = "🌶" * food["heat_level"]
            print(f"{name} ({cuisine}) | Heat Level: {heat_level}")
    


def get_spicy_food_by_cuisine(spicy_foods, cuisine):

    for food in spicy_foods:
         if food ["cuisine"] == cuisine:
              return food
  

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
         if food["heat_level"] > 5:
              name = food['name']
              cuisine = food['cuisine']
              heat_level = '🌶' * food["heat_level"]
              print (f"{name} ({cuisine}) | Heat Level: {heat_level}")




def get_average_heat_level(spicy_foods):
    sum_spicy_foods = sum(food["heat_level"] for food in spicy_foods)
    subscript = len(spicy_foods)
    average_heat_level = sum_spicy_foods/subscript
    return average_heat_level


def create_spicy_food(spicy_foods, spicy_food):
    pass
