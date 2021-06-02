import mysql.connector as database
import random

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

    def __del__(self):
        self.conn.close()
        print('Connection closed')

def gen_test_data():
    mysql = Mysql()
    item_names = ['phone', 'books', 'laptop', 'shirt']
    record_num = 10000
    for i in range(record_num):
        name = random.choice(item_names) + '-' + str(random.randrange(100))
        rating = random.randrange(6)
        sales = random.randrange(100, 1000)
        price = random.randrange(1000, 20000)
        mysql.add_data(name, rating, sales, price)
        if i % 1000 == 0:
            print(i)

if __name__ == '__main__':
    gen_test_data()
