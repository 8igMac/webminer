from fastapi import FastAPI
from typing import Optional
from enum import Enum

import mysql.connector as database

class Mysql:

    def __init__(self):
        db_conn_info = {
            'user': 'michael',
            'password': 'michael',
            'host': 'localhost',
            'database': 'shop'
        }
        
        self.conn = database.connect(**db_conn_info)
        self.cur = self.conn.cursor()

    def add_data(self, name, rating, sales, price):
        try:
            statement = 'INSERT INTO items (name, rating, sales, price) VALUES (%s, %s, %s, %s)'
            data = (name, rating, sales, price)
            self.cur.execute(statement, data)
            self.conn.commit()
            #print('Sucessfully add data')  # debug
        except database.Error as e: 
            print(f'Error adding entry to database: {e}')

    def get_data(self, name):
        try:
            statement = f"SELECT * FROM items WHERE name LIKE '{name}%'"
            self.cur.execute(statement)
            return self.cur.fetchall()
        except database.Error as e: 
            print(f'Error getting entry to database: {e}')

    def __del__(self):
        self.conn.close()
        print('Connection closed')

app = FastAPI()
mysql = Mysql()

class SortOption(str, Enum):
    relevancy = 'relevancy'  # Todo: define relevancy.
    time = 'time'
    sales = 'sales'
    price = 'price'

class SortOrder(str, Enum):
    asc = 'asc'
    desc = 'desc'

@app.get('/')
async def read_main():
    return {'msg': 'Hello, World'}

@app.get('/search')
async def search(
    keyword: str, 
    sort_by: Optional[SortOption] = None, 
    order: Optional[SortOrder] = None,
):
    result = mysql.get_data(keyword) 

    return result
#    return {
#        'operation': 'search',
#        'keyword': keyword,
#        'sort_by': sort_by,
#        'order': order,
#    }
