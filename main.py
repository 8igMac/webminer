from fastapi import FastAPI
from typing import Optional
from enum import Enum

app = FastAPI()

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
    order: Optional[SortOrder] = None
):

    return {
        'operation': 'search',
        'keyword': keyword,
        'sort_by': sort_by,
        'order': order,
    }
