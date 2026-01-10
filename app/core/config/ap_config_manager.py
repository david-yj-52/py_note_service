import os
from pathlib import Path
from typing import Optional

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    """전체 설정을 관리하는 클래스"""

    # 환경 변수
    environment: str = "development"

    # 하위 설정들
    app: AppConfig


class ConfigManager:
    """설정 파일 로더 및 관리자"""

    def __init__(self, env: str = None):
        self.base_dir = Path(__file__).resolve().parent
        self.env = env or os.getenv("ENVIRONMENT", "development")
        self._settings: Optional[Settings] = None


# 싱글톤 인스턴스
_config_manager = ConfigManager()


def get_settings() -> Settings:
    return _config_manager.get()


settings = get_settings()
