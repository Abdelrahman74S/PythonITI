from fastapi import FastAPI, HTTPException
from models import Meal, Customer, Order
from database import meals, customers, orders

app = FastAPI()


@app.get("/meals")
def get_meals():
    return meals


@app.post("/customers")
def register_customer(customer: Customer):
    customers.append(customer.dict())
    return {"message": "Customer registered", "customer_id": customer.id}


@app.post("/orders")
def place_order(order: Order):
    meal = next((m for m in meals if m["id"] == order.meal_id), None)
    customer = next((c for c in customers if c["id"] == order.customer_id), None)
    if not meal or not customer:
        raise HTTPException(status_code=404, detail="Meal or customer not found")

    orders.append(order.dict())
    return {"message": "Order placed", "order_id": order.id}


@app.get("/orders/{order_id}")
def get_order(order_id: int):
    order = next((o for o in orders if o["id"] == order_id), None)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order


@app.put("/orders/{order_id}")
def update_order_status(order_id: int, status: str):
    for o in orders:
        if o["id"] == order_id:
            o["status"] = status
            return {"message": "Order updated", "status": status}
    raise HTTPException(status_code=404, detail="Order not found")
