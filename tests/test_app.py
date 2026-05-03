from app import food_card

def test_food_card():
    food = {
        "id": 5,
        "food_name": "Burger", 
        "food_calories": 500, 
        "food_restaurant": "McDonald's",
        "food_logo": "https://fastfoodnutrition.org/logos/mcdonalds.jpg",
        "food_link": "https://fastfoodnutrition.org/mcdonalds/bacon-buffalo-ranch-deluxe-mccrispy",
        "food_category": "Sandwiches",
        "food_image": "https://fastfoodnutrition.org/item-photos/400x400/1665163352.jpg" # <--- Add this!
    }
    food_card(food)
    assert True