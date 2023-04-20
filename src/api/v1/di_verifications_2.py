from fastapi import APIRouter, Depends, Response, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

DB_USERS = [
    {"id": 1, "name": "John Smith"},
    {"id": 2, "name": "John Snow"},
    {"id": 3, "name": "James Bond"},
    {"id": 4, "name": "Mr. Born"},
    {"id": 5, "name": "Mr. President"},
    {"id": 6, "name": "Superman"},
    {"id": 7, "name": "The"},
]


forbidden_agent_keys = ["msie", "windows", "edg"]


async def verify_agent(user_agent: str = Header()):
    def is_valid(header_data: str) -> bool:
        if any(
            list(map(lambda x: x in header_data.lower(), forbidden_agent_keys))
        ):
            return False
        return True

    print("Validate header: used agent...")
    if not is_valid(user_agent):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)


auth = HTTPBasic()


async def verify_token(creds: HTTPBasicCredentials = Depends(auth)):
    def is_valid(credentials: HTTPBasicCredentials) -> bool:
        # user exists, returns True
        return DB_mock.user_exists(creds=credentials)

    print("Validate authorization...")
    if not is_valid(creds):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
        )


async def verify_offset(offset: Optional[int] = 0):
    print("Validate offset value...")
    if offset < 0 or offset >= len(DB_USERS):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid offset value",
        )


async def verify_limit(limit: Optional[int] = 5):
    print("Validate limit value...")
    if limit == 0 or limit > 100:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid limit value",
        )


async def limit_extractor(limit: Optional[int] = 5):
    print("Extract limit param...")
    return limit


async def get_data(
    q: Optional[str] = "",
    limit: int = Depends(limit_extractor),
    offset: Optional[int] = 0,
):
    print("Generate response data...")
    return DB_USERS[offset : offset + limit]


router = APIRouter(dependencies=[Depends(verify_agent)])


@router.get(
    "/",
    dependencies=[
        Depends(verify_token),
        Depends(verify_offset),
        Depends(verify_limit),
    ],
)
async def get_items(data: dict = Depends(get_data)):
    print("Send response...")
    headers = {"X-API-VERSION": "1.3.0"}
    return Response(content=json.dumps(data), headers=headers)
