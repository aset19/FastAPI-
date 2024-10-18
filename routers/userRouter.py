from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from  sqlalchemy.orm import Session
from starlette.responses import StreamingResponse

from conf.database import get_db
from  services import  userService
from  schemas.user import   UserBase
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates


router = APIRouter()


templates = Jinja2Templates(directory="templates")





@router.post('/', tags=["create_user"])
async def create(data: Annotated[UserBase, Depends()], db: Session = Depends(get_db)):
    user_created = userService.create_user(data,db)
    return user_created


@router.get('/all', tags=["get_all_users"],response_class=HTMLResponse)
async def get_all_user(request: Request, db: Session = Depends(get_db)):
    data = userService.get_all(db)
    return templates.TemplateResponse(
        "item.html",  # Имя шаблона
        {"request": request, "data": data}  #Контекст с request и id
    )


@router.get('/{id}', tags=["get_user"])
async def get_user(id: int, db: Session = Depends(get_db)):
    return userService.get_user(id, db)


@router.put('/{id}', tags=["update_user"])
async def update(id: int , data: Annotated[UserBase, Depends()], db: Session = Depends(get_db)):
    return userService.update_user(data,db,id)


@router.delete('/{id}', tags=["delete_user"])
async def delete(id: int , db: Session = Depends(get_db)):
    return userService.delete_user(db,id)


@router.delete('/' ,tags=["delete_all_users"])
async def delete(db: Session = Depends(get_db)):
    return userService.delete_all_users(db)
