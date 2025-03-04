import asyncio
import contextlib
from api.dependencies.authentication import get_users_db
from api.dependencies.authentication import get_user_manager
from core.authentication.user_manager import UserManager
from core.config import settings
from core.models import db_helper, User
from core.schemas.user import UserCreate


# get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_users_db_context = contextlib.asynccontextmanager(get_users_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

default_email = settings.admin.default_email
default_password = settings.admin.default_password
default_is_active = settings.admin.default_is_active
default_is_superuser = settings.admin.default_is_superuser
default_is_verified = settings.admin.default_is_verified


async def create_user(
    user_manager: UserManager,
    user_create: UserCreate,
) -> User:
    user = await user_manager.create(
        user_create=user_create,
        safe=False,
    )
    return user


async def create_superuser(
    email: str = default_email,
    password: str = default_password,
    is_active: bool = default_is_active,
    is_superuser: bool = default_is_superuser,
    is_verified: bool = default_is_verified,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with db_helper.session_factory() as session:
        async with get_users_db_context(session) as users_db:
            async with get_user_manager_context(users_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )


if __name__ == '__main__':
    asyncio.run(create_superuser())