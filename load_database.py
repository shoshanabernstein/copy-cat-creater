"""Script to load the database with restaurant nutrition data."""
from database import (create_database, load_database, 
                      scrape_restaurant, delete_by_id)

if __name__=="__main__":
    create_database()
    #mcdonalds = scrape_restaurant("https://fastfoodnutrition.org/mcdonalds")
    #wendys = scrape_restaurant("https://fastfoodnutrition.org/wendys")
    # starbucks = scrape_restaurant("https://fastfoodnutrition.org/starbucks")
    # dairy_queen = scrape_restaurant("https://fastfoodnutrition.org/dairy-queen")
    #load_database(mcdonalds)
    #load_database(wendys)
    # load_database(starbucks)
    # load_database(dairy_queen)
    delete_by_id(829)