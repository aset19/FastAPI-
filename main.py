
from fastapi import FastAPI


from conf.database import SessionLocal, engine, Base
from routers import userRouter
from fastapi.staticfiles import StaticFiles



app = FastAPI()

app.include_router(userRouter.router, prefix='/user')

app.mount("/static", StaticFiles(directory="static"), name="static")

