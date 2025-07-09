from collections.abc import Mapping
from types import MappingProxyType
from typing import Dict, List, Type

from sqlalchemy.orm import RelationshipProperty

from src.database.models.base import Base

from .transaction_tool import TransactionTool

__all__ = ("Base", "User", "Role", "TransactionTool", "ServiceToken")


def _retrieve_relationships() -> Dict[
    Type[Base], List[RelationshipProperty[Type[Base]]]
]:
    return {
        mapper.class_: list(mapper.relationships.values())
        for mapper in Base.registry.mappers
    }


MODELS_RELATIONSHIPS_NODE: Mapping[
    Type[Base], List[RelationshipProperty[Type[Base]]]
] = MappingProxyType(_retrieve_relationships())
