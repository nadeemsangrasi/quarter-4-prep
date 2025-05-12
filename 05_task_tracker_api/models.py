from pydantic import BaseModel,field_validator,EmailStr,constr
class UserCreate(BaseModel):
    name: str
    username: constr(
        strip_whitespace=True,
        to_lower=True,
        min_length=3, 
        max_length=50,
    )
    email: EmailStr
    age: int | None = None

    @field_validator("name")
    def name_length(cls, v):
        if len(v) < 2:
            raise ValueError("Name must be at least 2 characters long")
        if len(v) > 40:
            raise ValueError("Name must be less than or equal to 40 characters")
        return v
    
class ReadUser(BaseModel):
    id:int
    name:str
    username:str
    email:EmailStr
    age:int | None = None

class CreateTask(BaseModel):
    title: str
    description: str

    @field_validator("title")
    def title_length(cls, v):
        if len(v.strip()) < 3:
            raise ValueError("Title must be at least 3 characters long")
        if len(v) > 100:
            raise ValueError("Title must be less than or equal to 100 characters")
        return v

    @field_validator("description")
    def description_length(cls, v):
        if len(v.strip()) == 0:
            raise ValueError("Description cannot be empty")
        if len(v) > 500:
            raise ValueError("Description must be less than or equal to 500 characters")
        return v
    
class ReadTask(BaseModel):
    id:int
    user_id:int
    title:str
    description:str
