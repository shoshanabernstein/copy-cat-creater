from database import create_database, load_databse, scrape_restaurant

if __name__=="__main__":
    create_database()
    mcdonalds = scrape_restaurant("https://fastfoodnutrition.org/mcdonalds")
    wendys = scrape_restaurant("https://fastfoodnutrition.org/wendys")
    # starbucks = scrape_restaurant("https://fastfoodnutrition.org/starbucks")
    # dairy_queen = scrape_restaurant("https://fastfoodnutrition.org/dairy-queen")
    load_databse(mcdonalds)
    load_databse(wendys)
    # load_databse(starbucks)
    # load_databse(dairy_queen)