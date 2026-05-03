from app import food_card

def test_food_card():
    food = {"name": "Burger", "Calories": 500}

    result = food_card(food)

    assert "Burger" in result