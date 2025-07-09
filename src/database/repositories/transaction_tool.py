from typing import Optional, Type

from sqlalchemy import ColumnExpressionArgument
from typing_extensions import Unpack

from src.database import models
from src.database.exceptions import InvalidParamsError
from src.database.repositories.base import BaseRepository
from src.database.repositories.types.transaction_tool import (
    SavePrivateKeyType,
)


class TransactionToolsRepository(BaseRepository[models.TransactionTool]):
    __slots__ = ()

    @property
    def model(self) -> Type[models.TransactionTool]:
        return models.TransactionTool

    async def save_private_key(self, **data: Unpack[SavePrivateKeyType]) -> None:
        await self._crud.insert(**data)

    async def exists_private_key(self) -> bool:
        result = await self._crud.exists()
        return result

    async def get_verification_code(
        self, verification_code_id: int
    ) -> Optional[models.TransactionTool]:
        if not any([verification_code_id]):
            raise InvalidParamsError("at least one identifier must be provided")

        where_clauses: list[ColumnExpressionArgument[bool]] = []

        if verification_code_id:
            where_clauses.append(
                self.model.verification_code_id == verification_code_id
            )

        return await self._crud.select(*where_clauses)
