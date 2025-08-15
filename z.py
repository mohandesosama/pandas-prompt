from pydantic import BaseModel, conint

class Person(BaseModel):
    name: str
    age: conint(ge=0, le=120)

def save_emp(emp: Person):
    print("saved", emp)

save_emp(Person(name="Alice", age=30))  # Raises ValidationError
