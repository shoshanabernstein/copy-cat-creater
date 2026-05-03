"""This module contains the functions to scrape the menu from the provided URL and return the scraped data"""
import requests
from bs4 import BeautifulSoup
import re

@st.cache_data
# Function to scrape the menu from the provided URL and return the scraped data
def scrape_restaurant(html):
    """Scrapes the menu from the provided URL and returns the scraped data"""
    r = requests.get(f'{html}', auth=('user', 'pass'))
    soup = BeautifulSoup(r.text, 'html.parser')  
    restaurant_foods = []

    # Scrape the restaurant name and logo
    restaurant = soup.find('div', class_='rest_links_name').text.strip()
    restaurant_logo = soup.find('img', class_='logo_float').get('src')
  
     # Scrape the menu items, their categories, and their calorie information
    foods = soup.find_all('li', class_='filter_target')
    for food in foods:
        category_element = food.find_previous('h2')
        food_category = category_element.get_text(strip=True)
        food_link = "https://fastfoodnutrition.org" + food.find('a').get('href')

        food_image = scrape_food_image(food_link)
        if food:
            restaurant_foods.append({
                'food_name': food['title'],
                'food_calories': food['data-calories'],
                'food_restaurant': restaurant,
                'food_logo': "https://fastfoodnutrition.org" + restaurant_logo,
                'food_category': food_category,
                'food_link': food_link,
                'food_image': food_image
            })

    return restaurant_foods

@st.cache_data
# Function to scrape the food image from the provided URL and return the scraped image URL
def scrape_food_image(html):
    """Scrapes the food items picture"""
    r = requests.get(f'{html}', auth=('user', 'pass'))
    soup = BeautifulSoup(r.text, 'html.parser') 

    div = soup.find('div', class_='col-12')
    if div:
        img = div.find('img')
        if img and img.get('src'):
            food_image = "https://fastfoodnutrition.org" + img.get('src')
        else:
            food_image = None
    else:
        food_image = None

    return food_image


