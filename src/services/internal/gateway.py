from src.api.common.cache.redis import RedisCache
from src.common.interfaces.gateway import BaseGateway
from src.database import DBGateway


class InternalServiceGateway(BaseGateway):
    __slots__ = ("database", "redis", "_settings")

    def __init__(
        self,
        database: DBGateway,
        redis: RedisCache,
    ) -> None:
        self.database = database
        self.redis = redis
        super().__init__(database)
