import requests
import json

API_URL = "https://api.nal.usda.gov/fdc/v1/foods/list"

API_KEY = "4gK8Ihd4ADtJiLSyjQ5yZWsGb7HceBIzLZPNfj24"

def api_food_nutrition(food):
    try:
        params = {
        "query": food,
        "api_key": API_KEY
        }

        results = requests.get(API_URL, params=params)

        results.raise_for_status()
        data = results.json()
        
        if "foods" in data and len(data["foods"]) > 0:
            food_item = data["foods"][0]

            # return {
            #     "name": food_item.get("description"),
            #     "calories": next((n['value'] for n in food_item.get('foodNutrients', []) if n.get('nutrientName') == 'Energy'), 0),
            #     "protein": next((n['value'] for n in food_item.get('foodNutrients', []) if n.get('nutrientName') == 'Protein'), 0)
            # }
        return data
    except Exception as ex:
        return None
    
food_data = api_food_nutrition("burger")
print(json.dumps(food_data, indent=4))