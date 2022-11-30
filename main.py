from fastapi import FastAPI
from typing import Optional
app = FastAPI()

@app.get('/blog')
def index(limit, published: bool = True, sort: Optional[str] = None):
    # only get 10 published blods
    if published:
        return {'data': f'{limit} published blogs from the db list'}
    else:
        return {'data': f'{limit} blogs from the db list'}
@app.get('/blog/unpublished')
def unpublished():
    return{'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    # fetch blog with id = id
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    # fetch comments of blog with id = id
    return {'data':{'1','2'}}