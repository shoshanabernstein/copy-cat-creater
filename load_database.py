"""Script to load the database with restaurant nutrition data."""
from database import (create_database, load_database, 
                      scrape_restaurant, delete_by_id)

if __name__=="__main__":
    create_database()
    # mcdonalds = scrape_restaurant("https://fastfoodnutrition.org/mcdonalds")
    kfc = scrape_restaurant("https://fastfoodnutrition.org/kfc")
    # starbucks = scrape_restaurant("https://fastfoodnutrition.org/starbucks")
    # baskin_robbins = scrape_restaurant("https://fastfoodnutrition.org/baskin-robbins")
    olive_garden = scrape_restaurant("https://fastfoodnutrition.org/olive-garden")
    waffle_house = scrape_restaurant("https://fastfoodnutrition.org/waffle-house")
    chipotle = scrape_restaurant("https://fastfoodnutrition.org/chipotle")
    pizza_hut = scrape_restaurant("https://fastfoodnutrition.org/pizza-hut")
    dunkin_donuts = scrape_restaurant("https://fastfoodnutrition.org/dunkin-donuts")
    # load_database(mcdonalds)
    load_database(kfc)
    # load_database(starbucks)
    # load_database(baskin_robbins)
    load_database(waffle_house)
    load_database(dunkin_donuts)
    load_database(pizza_hut)
    load_database(olive_garden)
    load_database(chipotle)
