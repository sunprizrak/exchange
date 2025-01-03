from fastapi import APIRouter

from api.dependencies.authentication.backend import authentication_backend
from core.config import settings
from api.api_v1.fastapi_users import fastapi_users


router = APIRouter(
    prefix=settings.api.v1.auth,
    tags=["Auth"],
)

router.include_router(
    router=fastapi_users.get_auth_router(authentication_backend),
)