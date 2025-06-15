from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return{'data':{'Name':'My name is Maryam!!!'}}


@app.get('/about')
def about():
    return{'data':{'About':'I am LeaRNING FAST API'}}
