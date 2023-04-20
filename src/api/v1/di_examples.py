from fastapi import APIRouter, Depends

router = APIRouter()


async def paginator_response():
    return {"offset": 2, "limit": 10}


@router.get("/users/")
async def get_users(params: dict = Depends(paginator_response)):
    return params


db_items = [
    {"name": "Laurel wreath", "description": "Veni, vidi, vici"},
    {"name": "Billboard", "description": "This could be your ad"},
    {"name": "Lightsaber", "description": "May the Force be with you"},
    {"name": "Golden snitch", "description": "I open at the close"},
]


class Paginator:
    def __init__(self, offset: int = 0, limit: int = 10):
        self.offset = offset
        self.limit = limit

    def __str__(self):
        return "{}: offset: {}, limit: {}".format(
            self.__class__.__name__, self.offset, self.limit
        )

    def __call__(self, q: str = ""):
        return self


default_paginator = Paginator(offset=1, limit=2)


@router.get("/items/")
async def get_items(paginator: Paginator = Depends(default_paginator)):
    response = {}
    print(paginator)
    response.update(
        {
            "data": db_items[
                paginator.offset : paginator.offset + paginator.limit
            ]
        }
    )
    return response
