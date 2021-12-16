# FastAPI est une classe fournissant les fonctionnalites necessaires a votre API
from fastapi import FastAPI

app = FastAPI()

@app.get("/personnes")
def get_all_persons ():
    return {"message": "Hello World"}

@app.get("/personnes/{ssn}")
def get_person_with_ssn():
    return {"message": "Hello World"}

@app.update("/personnes/{ssn}")
def update_persone_with_ssn():
    return {"message": "Hello World"}

@app.delete("/personnes/{ssn}")
def delete_person_with_ssn(item_id: int):
    return {"item_id": item_id}
