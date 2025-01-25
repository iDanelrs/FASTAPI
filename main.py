from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def main():
    return {'Hello World from FastAPI':'Alfredo Danel Rolon Salazar'}