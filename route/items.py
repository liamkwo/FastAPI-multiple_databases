from fastapi import APIRouter, Depends, Body
from api.database import get_db, get_db2

router = APIRouter()


@router.get(
    "/items/get_db1", description="multiple DB"
)
async def get_db1(
    db=Depends(get_db),
):
    
    return True
    
    
@router.get(
    "/items/get_db2", description="multiple DB"
)
async def get_db2(
    db=Depends(get_db2),
):
    
    return True
