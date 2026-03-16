from fastapi import FastAPI
from app.routes.student_routes import router
from app.database.connection import engine
from app.models.student import Base

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)

# include routes
app.include_router(router)