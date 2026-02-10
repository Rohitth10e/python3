from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool

input_data = {'id':101, 'name':'Ronika', 'is_active':True}
ronika = User(**input_data)
print(ronika)