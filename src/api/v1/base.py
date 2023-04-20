import sys
from fastapi import APIRouter
from fastapi.responses import PlainTextResponse


# Объект router, в котором регистрируем обработчики
router = APIRouter()


@router.get('/')
async def root_handler():
    return {
        'version': 'v1',
        'python': sys.version_info
    }

@router.get('/action/{action}')
async def action_handler(action):
    return {
        'action': action,
    }


@router.get('/filter')
@router.post('/filter')
async def filter_handler(
    param1: str, 
    param2: int | None = None,
) -> dict[str, str | int | None]:
    return {
        'action': 'filter',
        'param1': param1,
        'param2': param2
    }


@router.get("/plain_text", response_class=PlainTextResponse)
async def main():
    return "Custom text for test"