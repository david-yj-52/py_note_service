from app.service.note_mng.note_mng_biz_service import NoteService
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db

router = APIRouter()


# 1. 폴더 트리 구조 조회 (가장 먼저 선언)
@router.get("/folder-tree")
async def get_folder_tree(db: AsyncSession = Depends(get_db)):
    service = NoteService(db)
    return await service.get_folder_tree()


# 2. 경로 기반 노트 상세 조회
@router.get("/by-path")
async def get_note_by_path(
        file_path: str = Query(..., description="파일 상대 경로"),
        db: AsyncSession = Depends(get_db)
):
    service = NoteService(db)
    return await service.get_note_detail_by_path(file_path)


# 3. 신규 저장 및 업데이트
@router.post("/save")
async def save_note(
        title: str,
        file_path: str,
        content: str,
        user_name: str,
        last_hash: str = None,
        db: AsyncSession = Depends(get_db)
):
    service = NoteService(db)
    return await service.save_or_update_note(title, file_path, content, user_name, last_hash)


# 4. ID 기반 조회 (가장 마지막에 선언)
@router.get("/{note_id}")
async def get_note_by_id(note_id: str, db: AsyncSession = Depends(get_db)):
    service = NoteService(db)
    return await service.get_note_by_id(note_id)
