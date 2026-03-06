# /routers/router.py
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter(prefix="/", redirect_slashes=True)

@router.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# app.py
from routers.router import router

app.include_router(router)