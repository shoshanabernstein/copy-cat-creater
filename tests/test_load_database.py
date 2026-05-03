from unittest.mock import patch
from database import load_database, create_database
from test_database import Test_Food_Data, in_memory_db

def test_load_database(in_memory_db):
    create_database()
    with patch('sqlite3.connect', return_value=in_memory_db):
        
        load_database(Test_Food_Data)

        c = in_memory_db.cursor()
        c.execute('SELECT * FROM restaurant_foods')
        results = c.fetchall()

        assert len(results) == len(Test_Food_Data)

def test_load_database_runs():
    try:
        load_database(Test_Food_Data)
    except Exception:
        assert False, "load_database crashed"