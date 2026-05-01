from scraper import scrape_food_image, scrape_restaurant
from unittest.mock import Mock

def test_scrape_food_image():
    test_html = "https://fastfoodnutrition.org/mcdonalds/bacon-buffalo-ranch-deluxe-mccrispy"

    test_image_url = scrape_food_image(test_html)

    assert test_image_url == "https://fastfoodnutrition.org/item-photos/400x320/176219431863748.png"

def test_scrape_restaurant():
    test_html = "https://fastfoodnutrition.org/mcdonalds"
    test_data = scrape_restaurant(test_html)
    assert len(test_data) > 0
    assert test_data[0]['food_logo'] == "https://fastfoodnutrition.org/logos/mcdonalds.jpg"