from sqlalchemy import String, Index
from sqlalchemy.orm import Mapped, mapped_column

from app.database.default_model_mixin import DefaultModelMixin
from app.database.session import Base


class NoteMetadata(Base, DefaultModelMixin):
    __tablename__ = "note_metadata"

    # 노트 제목
    title: Mapped[str] = mapped_column(String(255), nullable=False)

    # 파일 시스템 상의 상대 경로 (예: 'folder/note.md')
    # 이 경로는 DB 내에서 유일해야 하며 검색의 기준이 됩니다.
    file_path: Mapped[str] = mapped_column(String(500), nullable=False, unique=True)

    # 마지막으로 커밋된 Git Hash값 (Optimistic Locking 및 버전 관리용)
    last_commit_hash: Mapped[str] = mapped_column(String(100), nullable=True)

    # 인덱스 설정: 경로 기반 조회가 잦으므로 인덱스를 생성합니다.
    __table_args__ = (
        Index("ix_note_metadata_file_path", "file_path"),
    )
