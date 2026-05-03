"""Database module for the Copy-Cat Creater app."""
import sqlite3
from scraper import scrape_restaurant

def get_connection(db_path="food.db"):
    return sqlite3.connect(db_path)
# Function to create the database and the restaurant_foods table
def create_database():
    """Creates the database"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS restaurant_foods (
                id INTEGER PRIMARY KEY,
                food_name TEXT,
                food_calories INT,
                food_restaurant TEXT,
                food_logo BLOB,
                food_category TEXT,
                food_link TEXT,
                food_image BLOB
            )
        ''')
    conn.commit()

# Function to load the data into the database
def load_database(foods):
    """Loads the data into the databse"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        
        for food in foods:
            c.execute('''
                INSERT INTO restaurant_foods(food_name, food_calories, food_restaurant, food_logo, 
                      food_category, food_link, food_image) VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (food['food_name'], food['food_calories'], food['food_restaurant'], 
                  food['food_logo'], food['food_category'], food['food_link'], food['food_image']))

    conn.commit()

# Function to filter the foods by restaurant, calories, and category and return a list of foods
def filter_foods(restaurant=None, calories=None, category=None): 
    """Filters the foods by restaurant, calories, and category and returns a list of foods"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()

        query = f"""SELECT id, food_name, food_calories, food_restaurant, food_logo, food_category, food_link, food_image
        FROM restaurant_foods
        WHERE 1=1
        """
        params = []

        # Add conditions to the query based on the provided filters
        if restaurant:
            query += " AND food_restaurant = ?"
            params.append(restaurant)
        
        if calories is not None:
            query += " AND food_calories <= ?"
            params.append(calories)

        if category:
             query += " AND food_category = ?"
             params.append(category)
             
        c.execute(query, tuple(params))

        rows = c.fetchall() 
        filter_foods = []

        # Loop through the rows and create a list of foods based on the query results
        for row in rows:
                food_id, food_name, food_calories, food_restaurant, food_logo, food_category, food_link, food_image = row

                filter_foods.append({
                        "id": food_id,
                        "food_name": food_name,
                        "food_calories": food_calories,
                        "food_restaurant": food_restaurant,
                        "food_logo": food_logo,
                        "food_category": food_category,
                        "food_link": food_link,
                        "food_image": food_image
                    })

    return filter_foods

# Function to get the list of food categories
def get_food_categories(conn=None):
    """Get list of food categories"""
    if conn is None:
        conn = get_connection()
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT food_category FROM restaurant_foods GROUP BY food_category''')

        rows = c.fetchall()

    categories = []
    for row in rows:
        categories.append(row[0])
    return categories

# Function to get the list of food restaurants
def get_food_restaurant():
    """Get list of food restaurant"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT food_restaurant FROM restaurant_foods GROUP BY food_restaurant''')

        rows = c.fetchall()

    restaurant = []
    for row in rows:
        restaurant.append(row[0])
    return restaurant

# Function to get the list of categories by restaurant
def get_categories_by_restaurant(restaurant):
    """Get list of categpries by food restaurant"""
    with sqlite3.connect('foods.db') as conn:
        c = conn.cursor()
        c.execute('''SELECT DISTINCT food_category 
                FROM restaurant_foods 
                WHERE food_restaurant = ?''', (restaurant,))

        rows = c.fetchall()

    restaurant = []
    for row in rows:
        restaurant.append(row[0])
    return restaurant

def delete_by_id(food_id):
    try:
        with sqlite3.connect('foods.db') as conn:
            c = conn.cursor()
            c.execute('DELETE FROM restaurant_foods WHERE id = ?',
                    (food_id, ))
            conn.commit()
    except sqlite3.Error as e:
        return
