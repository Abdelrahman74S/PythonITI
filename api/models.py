from pydantic import BaseModel


class Meal(BaseModel):
    id: int
    name: str
    price: float


class Customer(BaseModel):
    id: int
    name: str
    address: str


class Order(BaseModel):
    id: int
    customer_id: int
    meal_id: int
    quantity: int
    status: str = "pending"
