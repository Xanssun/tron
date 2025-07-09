from sqlalchemy import Integer, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column

from src.database.models.base import Base
from src.database.models.base.mixins import ModelWithIDMixin, ModelWithTimeMixin


class TransactionTool(ModelWithIDMixin, ModelWithTimeMixin, Base):
    verification_code_id: Mapped[int] = mapped_column(Integer, index=True, unique=True)
    private_key: Mapped[bytes] = mapped_column(LargeBinary)
    verification_code: Mapped[str] = mapped_column(index=True)
