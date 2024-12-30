from typing import TYPE_CHECKING

from fastapi import Depends
from fastapi_users.authentication.strategy.db import DatabaseStrategy
from sqlalchemy.sql.annotation import Annotated

from .access_tokens import get_access_tokens_db
from core.config import settings

if TYPE_CHECKING:
    from core.models import AccessToken
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase


def get_database_strategy(
    access_tokens_db: Annotated[
        AccessTokenDatabase["AccessToken"],
        Depends(get_access_tokens_db),
    ]
) -> DatabaseStrategy:
    return DatabaseStrategy(
        database=access_tokens_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )