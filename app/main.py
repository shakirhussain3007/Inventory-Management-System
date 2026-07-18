from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.config.db import test_database_connection

from app.routes.user_routes import router as user_router
from app.routes.product_routes import router as product_router
from app.routes.admin_routes import router as admin_router
from app.routes.auth_routes import router as auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting Inventory Management System...")
    test_database_connection()
    yield
    print("Application Stopped")


app = FastAPI(
    title="Inventory Management System",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(user_router)
app.include_router(product_router)
app.include_router(admin_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {
        "message": "Inventory Management System API"
    }