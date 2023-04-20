from fastapi import APIRouter, Depends, Header, HTTPException, Request, status
from fastapi.security import HTTPBasic

db_items = [
    {"name": "Laurel wreath", "description": "Veni, vidi, vici"},
    {"name": "Billboard", "description": "This could be your ad"},
    {"name": "Lightsaber", "description": "May the Force be with you"},
    {"name": "Golden snitch", "description": "I open at the close"},
]

BLACK_LIST = [
    # "127.0.0.1",
    "56.24.15.106"
]

router = APIRouter()


async def verify_token(authorization: str = Header()):
    def is_valid(token: str) -> bool:
        if "Bearer" not in token:
            return False
        # get token and validate
        return True

    if not is_valid(authorization):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authorization",
        )


async def check_allowed_ip(request: Request):
    def is_ip_banned(headers):
        is_banned = False
        try:
            real_ip = headers["X-REAL-IP"]
            print(real_ip)
            is_banned = real_ip in BLACK_LIST
        except KeyError:
            print("IP header not found")
            is_banned = True
        return is_banned

    if is_ip_banned(request.headers):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


@router.get(
    "/items_verified/",
    dependencies=[Depends(verify_token), Depends(check_allowed_ip)],
)
async def get_items():
    return db_items
