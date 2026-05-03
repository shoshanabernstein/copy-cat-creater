"""Script to load the database with restaurant nutrition data."""
from database import (create_database, load_database, 
                      scrape_restaurant, delete_by_id, delete_duplicates)

if __name__=="__main__":
    create_database()
    mcdonalds = scrape_restaurant("https://fastfoodnutrition.org/mcdonalds")
    starbucks = scrape_restaurant("https://fastfoodnutrition.org/starbucks")
    baskin_robbins = scrape_restaurant("https://fastfoodnutrition.org/baskin-robbins")

    load_database(mcdonalds)
    load_database(starbucks)
    load_database(baskin_robbins)

    panera = scrape_restaurant("https://fastfoodnutrition.org/panera-bread")
    taco_bell = scrape_restaurant("https://fastfoodnutrition.org/taco-bell")
    dairy_queen = scrape_restaurant("https://fastfoodnutrition.org/dairy-queen")
    chick_fil_a = scrape_restaurant("https://fastfoodnutrition.org/chick-fil-a")
    taco_bell = scrape_restaurant("https://fastfoodnutrition.org/burger-king")
    subway = scrape_restaurant("https://fastfoodnutrition.org/subway")

    load_database(panera)
    load_database(taco_bell)
    load_database(dairy_queen)
    load_database(chick_fil_a)
    load_database(subway)
    load_database(taco_bell)

    # delete_duplicates()

