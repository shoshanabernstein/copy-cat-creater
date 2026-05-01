from scraper import scrape_food_image, scrape_restaurant
from unittest.mock import Mock

def test_scrape_food_image():
    test_html = "https://fastfoodnutrition.org/mcdonalds/bacon-buffalo-ranch-deluxe-mccrispy"

    test_image_url = scrape_food_image(test_html)

    assert test_image_url == "https://fastfoodnutrition.org/item-photos/400x320/176219431863748.png"
    assert scrape_food_image(test_empty_html) == None 

def test_scrape_restaurant():
    fake_data = ""