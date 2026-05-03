from database import ( get_categories_by_restaurant, 
                      get_food_categories, get_food_restaurant, filter_foods)
import sqlite3
import pytest
from unittest.mock import patch
import unittest.mock as mock


Test_Food_Data = [{
"food_name":"Filet-O-Fish®",
"food_calories":390,
"food_restaurant":"McDonald's",
"food_logo":"https://fastfoodnutrition.org/logos/mcdonalds.jpg",
"food_category":"Burgers & Sandwiches",
"food_link":"https://fastfoodnutrition.org/mcdonalds/filet-o-fish",
"food_image":"https://fastfoodnutrition.org/item-photos/400x228/1826.jpg"}, 
{"food_name":"Cheeseburger",
"food_calories":300,
"food_restaurant":"McDonald's",
"food_logo":"https://fastfoodnutrition.org/logos/mcdonalds.jpg",
"food_category":"Burgers & Sandwiches",
"food_link":"https://fastfoodnutrition.org/mcdonalds/cheeseburger",
"food_image":"https://fastfoodnutrition.org/item-photos/400x228/1823.jpg"
}]

@pytest.fixture
def in_memory_db():
    """Provide a fresh in-memory database with schema created."""
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()

    # Create schema
    c = conn.cursor()
    c.execute('''
        CREATE TABLE restaurant_foods (
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
    yield conn
    conn.close()

@pytest.fixture
def mock_scraper(mocker):
    return mocker.Mock(return_value=Test_Food_Data)

def test_get_food_restaurant(in_memory_db):
    with patch('sqlite3.connect', return_value=in_memory_db):

        c = in_memory_db.cursor()
        for food in Test_Food_Data:
            c.execute('''
                  INSERT INTO restaurant_foods (food_name, food_restaurant, food_category) VALUES (?, ?, ?)
                  ''', (food['food_name'], food['food_restaurant'], food['food_category']))
        in_memory_db.commit()

        results = get_food_restaurant()

        assert len(results) == 1
        assert results[0] == "McDonald's"

def test_get_categories_by_restaurant(in_memory_db):
    with patch('sqlite3.connect', return_value=in_memory_db):
        
        c = in_memory_db.cursor()
        for food in Test_Food_Data:
            c.execute('''
                  INSERT INTO restaurant_foods (food_name, food_restaurant, food_category) VALUES (?, ?, ?)
                  ''', (food['food_name'], food['food_restaurant'], food['food_category']))
        in_memory_db.commit()

        results = get_categories_by_restaurant("McDonald's")

        assert len(results) == 1
        assert results[0] == "Burgers & Sandwiches"




    # for food in Test_Food_Data:
    #     c.execute('''
    #           INSERT INTO restaurant_foods (food_name, food_restaurant, food_calories)
    #           VALUES (?, ?, ?)
    #           ''', (food['food_name'], food['food_restaurant'], food['food_calories']))
    # in_memory_db.commit()

    # results = get_food_categories()

    # assert len(results) == len(Test_Food_Data)

def test_get_food_categories(in_memory_db):
    with patch('sqlite3.connect', return_value=in_memory_db):

        c = in_memory_db.cursor()
        for food in Test_Food_Data:
            c.execute('''
                  INSERT INTO restaurant_foods (food_name, food_restaurant, food_category) VALUES (?, ?, ?)
                  ''', (food['food_name'], food['food_restaurant'], food['food_category']))
        in_memory_db.commit()

        results = get_food_categories()

        assert len(results) == 1
        assert results[0] == "Burgers & Sandwiches"

def test_filter_foods(in_memory_db):
    with patch('sqlite3.connect', return_value=in_memory_db):
        c = in_memory_db.cursor()
        for food in Test_Food_Data:
            c.execute('''
                  INSERT INTO restaurant_foods (food_name, food_restaurant, food_category, food_calories) VALUES (?, ?, ?, ?)
                  ''', (food['food_name'], food['food_restaurant'], food['food_category'], food['food_calories']))
        in_memory_db.commit()

        results = filter_foods(restaurant="McDonald's", calories=400, category="Burgers & Sandwiches")

        assert len(results) == 2
        assert results[0]['food_restaurant'] == "McDonald's"
        assert results[0]['food_name'] == "Filet-O-Fish®"
        assert results[0]['food_calories'] == 390
        assert results[0]['food_category'] == "Burgers & Sandwiches"