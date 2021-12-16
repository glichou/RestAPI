import pydantic
from pydantic import BaseModel

class ModelPerson(BaseModel):
        nom : str
        prenom : str
        ssn : str