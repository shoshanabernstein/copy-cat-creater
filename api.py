import requests

API_URL = "https://api.nal.usda.gov/fdc/v1/foods/search"

API_KEY = "4gK8Ihd4ADtJiLSyjQ5yZWsGb7HceBIzLZPNfj24"

def api_food_nutrition(food):
    params = {
    "query": food,
    "api_key": API_KEY,
    "pageSize": 1
    }

    try:
        results = requests.get(API_URL, params=params)
        results.raise_for_status()
        return results.json()
    
    except Exception as ex:
        return None
    
def get_simplified_nutrition(data):
    # Check if the data is a dictionary and has the 'foods' key
    if not isinstance(data, dict) or not data.get("foods"):
        return None
    
    food = data["foods"][0]
    nutrients = food.get("foodNutrients", [])

    results = {"name": food.get("description").title(),
               "Calories": 0,
               "Protein": 0,
               "Fat": 0,
               "Carbs": 0
               }

    for n in nutrients:
        name = n.get("nutrientName", "").lower()
        value = round(n.get("value", 0), 1)

        if "energy" in name:
            results["Calories"] = value

        elif "protein" in name:
            results["Protein"] = value

        elif "total lipid (fat)" in name or "total fat" in name:
            results["Fat"] = value

        elif "fat" in name and results["Fat"] == 0:
            results["Fats"] = value
            
        elif "carbohydrate" in name:
            results["Carbs"] = value

    return results

def get_nutrition_data(food_name):
    # 1. Fetch the raw data from the search API
    data = api_food_nutrition(food_name)
    # 2. Pass that data to the simplification function
    return get_simplified_nutrition(data)
    