from enum import Enum


class DbTypeEnum(Enum):
    SQLITE = "sqlite"
    POSTGRESQL = "postgresql"
    ORACLE = "oracle"
