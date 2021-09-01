from typing import Optional
from fastapi.params import Form
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form, HTTPException
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from starlette.responses import RedirectResponse
from forms import LoginForm
from db import login as db_login
import sqlite3

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def login(request: Request, query: Optional[str] = Form(None)):
    return templates.TemplateResponse("index.html", {"request": request, "incorrect_credentials" : False})

@app.post("/login")
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    open('logs.txt', 'a+').write(f"\n[*] New login attempt: {username} : {password}")
    con = sqlite3.connect("C:\Tools\database\simpleLogin.db")    
    cur = con.cursor()
    login_status = db_login(cur, username, password)

    if login_status[0] is True:
        is_admin = username == 'admin'
        return templates.TemplateResponse("userpanel.html", {"username" : login_status[1], "request" : request, "is_admin" : is_admin})
    elif login_status[0] is False:
        return templates.TemplateResponse("index.html", {"request": request, "incorrect_credentials" : True, "error_details" : "Incorrect Login or password."})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "incorrect_credentials" : True, "error_details" : login_status})

@app.get("/login")
async def index_redirect():
    return RedirectResponse(url='/')