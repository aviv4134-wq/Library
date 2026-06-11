import fastapi


app = fastapi.FastAPI()

@app.get('/')
def fdf():
    return 'fsdf'