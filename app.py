from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Model for request body validation
class Person(BaseModel):
    name: str
    occupation: str
    address: str

# Existing data list
data = []

# POST request handler to add new people
@app.post('/person')
def add_person(person: Person):
    # Extract data from request body
    name = person.name
    occupation = person.occupation
    address = person.address
    
    # Check if any field in the request body is blank
    for field, value in person:
        if not value:
            error_message = f"{field.capitalize()} cannot be empty"
            return {"success": False, "result": {"error_message": error_message}}
    
    # Create a new person dictionary
    new_person = {
        'name': name,
        'occupation': occupation,
        'address': address,
    }
    data.append(new_person)
    print(new_person)
    return {"success": True, "result": new_person}

@app.get('/person')
def get_people():
    return data

 
# {
# 	"name": "Beef Wellington",
# 	"occupation": "Fry Cook",
# 	"address": "124 Conch Street"
# }

# # sample response
# {
# 	"success": true,
# 	"result": {
# 		"name": "Beef Wellington",
# 		"occupation": "Fry Cook",
# 		"address": "124 Conch Street"
# 	}
# }