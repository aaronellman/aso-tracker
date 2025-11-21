from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Welcome to ASO Tracker"}

@router.get("/apps")
def get_apps():
    return {"apps": []}

@router.get("/keywords")
def add_keyword(keyword: str):
    return {"keyword_added": keyword}

@router.post("/track")
def add_keyword(keyword: str):
    return {"keyword_added": keyword}
