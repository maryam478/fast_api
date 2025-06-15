from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def index():
    return{'data':{'Name':'My name is Maryam!!!'}}


@app.get('/about')
def about():
    return{'data':{'About':'I am LeaRNING FAST API'}}

# Fixed Path or Fixed route
@app.get('/blog/published')
def blog_published():
    return{'data':{'blog':'Published'}}

# Dynamic Path or Dynamic route
@app.get('/blog/{id}')
def blog(id:int):
    return{'data':{'blog_id':id}}

# Query Parameters
@app.get('/book')
def book(pages:int,published:bool):
    if published:
        return{'data':f'{pages} pages published '}
    else:
        return{'data':f'{pages} pages NOT published '}


#Query parameters with default values
@app.get('/book')
def book(pages:int=5,published:bool|None = None):
    if published:
        return{'data':f'{pages} pages published '}
    else:
        return{'data':f'{pages} pages NOT published '}
    
# Posting the request and sending it in request body

class Items(BaseModel):
    name:str
    description:str|None = None
    price:float
    tax:float|None = None


@app.post('/items')
def items(item:Items):
    return item

 


