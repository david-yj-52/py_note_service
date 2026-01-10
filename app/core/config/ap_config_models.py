from pydantic import BaseModel

from app.core.enum.db_type_enum import DbTypeEnum


class AppConfig(BaseModel):
    """어플리케이션 설정"""
    name: str = "NoteService"
    description: str = "Note Service BackEnd"
    version: str = "1.0"
    debug: bool = False


class DataBaseConfig(BaseModel):
    """데이터베이스 설정"""
    SqliteConfig: SqliteConfig = SqliteConfig()
    PostgresqlConfig: PostgresDataBaseConfig = PostgresDataBaseConfig()
    OracleConfig: OracleDataBaseConfig = OracleDataBaseConfig()



class SqliteDataBaseConfig(BaseModel):
    """데이터베이스 (Sqlite) 설정"""
    db_type: DbTypeEnum = DbTypeEnum.SQLITE
    filepath: str
    username: str | None = None
    password: str | None = None
    database: str


class PostgresDataBaseConfig(BaseModel):
    """데이터베이스 (Postgresql) 설정"""
    db_type: DbTypeEnum = DbTypeEnum.POSTGRESQL
    host: str
    port: int
    username: str
    password: str
    database: str


class OracleDataBaseConfig(BaseModel):
    """데이터베이스 (Oracle) 설정"""
    db_type: DbTypeEnum = DbTypeEnum.SQLITE
    host: str | None = None
    port: int | None = None
    username: str | None = None
    password: str | None = None
    database: str
    url: str = url(self.db_type)


def url(DyTypeEnum dbtype) -> str:
    if self.db_type is DbTypeEnum.SQLITE:
        # SQLite는 파일 기반이라 host/port/user/password 필요 없음
        return f"sqlite:///{self.database}"
    if self.db_type is DbTypeEnum.POSTGRESQL:
        return (f"postgresql://{self.username}:{self.password}" f"@{self.host}:{self.port}/{self.database}")
    if self.db_type is DbTypeEnum.ORACLE:
        # Oracle은 일반적으로 이런 형태를 사용
        return (
            f"oracle://{self.username}:{self.password}" f"@{self.host}:{self.port}/?service_name={self.database}")
    raise ValueError(f"지원하지 않는 DB 타입입니다: {self.db_type}")


class CorsConfig(BaseModel):
    """CORS 설정"""
    allow_origins: list[str] = ["*"]
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]
    allow_credentials: bool = True


class ServerConfig(BaseModel):
    """서버 설정"""
    host: str = "127.0.0.1"
    port: int = 9900
    reload: bool = True
    workers: int = 1
