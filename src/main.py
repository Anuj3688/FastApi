from fastapi import FastAPI
from routers import factory, tea, bulk_handling
app = FastAPI(
    title="TeaHub Service",
    description="Manage teas with origin, price, and inventory via RESTful API.",
    version="1.0.0"
)

app.include_router(tea.router)
app.include_router(factory.router)
app.include_router(bulk_handling.router)

@app.get("/")
def get_root():
    return { "message": "Let's Start learning! Jai Shree Ram" }




