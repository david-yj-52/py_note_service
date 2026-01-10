# 📝 Markdown Note Management System (PoC)

본 프로젝트는 로컬 Git 리포지토리에 저장된 마크다운(`.md`) 파일들을 관리하고, 해당 파일들의 메타데이터를 DB(SQLite)와 동기화하며 버전 관리(Git Commit Hash)를 수행하는 비동기 API 서버입니다.

## 🚀 주요 기능

* **Git 기반 버전 관리**: 노트 저장 시 자동으로 Git Commit을 수행하고 고유 해시값을 DB에 저장합니다.
* **실시간 동기화 (Sync)**: 파일 시스템의 변경사항(이동, 삭제, 생성)을 감지하여 DB 메타데이터를 업데이트합니다.
* **충돌 방지 (Optimistic Locking)**: 사용자가 수정 중인 파일의 해시값과 DB의 해시값을 비교하여 동시 수정 충돌을 방지합니다.
* **계층형 트리 구조**: 파일 경로를 분석하여 폴더 및 파일 트리를 JSON 형태로 응답합니다.

## 🛠 기술 스택

* **Backend**: FastAPI, Uvicorn
* **Database**: SQLAlchemy (Async), SQLite
* **Git**: GitPython
* **File I/O**: aiofiles

## 📋 사전 요구 사항

`.env` 파일을 프로젝트 루트에 생성하고 아래 설정을 추가하세요.

```env
REPO_PATH=C:/your/git/repository/path
DATABASE_URL=sqlite+aiosqlite:///./note_metadata.db
```

## 🏗 프로젝트 설치 및 실행

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```

### 2. 서버 실행

```bash
uvicorn app.main:app --reload
```

## 🔌 주요 API 엔드포인트

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/notes/save` | 노트 저장 및 Git Commit 수행 |
| `GET` | `/notes/folder-tree` | 폴더/파일 계층 구조 조회 |
| `GET` | `/notes/by-path` | 파일 경로 기반 메타데이터 및 내용 조회 |
| `GET` | `/notes/{note_id}` | ID(UUID) 기반 노트 조회 |

## ⚠️ 경로 처리 주의사항 (Windows/Linux)

본 서비스는 윈도우 환경의 `WindowsPath` 객체와 Git의 경로 포맷 간 호환성을 위해 모든 경로를 **상대 경로 및 슬래시(`/`)**로 정규화하여 처리합니다.

```python
# 내부 로직 예시
formatted_rel_path = str(rel_path).replace("\\", "/")  # WindowsPath 에러 방지
```

## 📁 프로젝트 구조

```
py_note_service/
├── .env                              # 리포지토리 경로(REPO_PATH), DB URL 등 환경 변수
├── .gitignore                        # git 관리 제외 설정 (__pycache__, .db, .env 등)
├── requirements.txt                  # 프로젝트 의존성 라이브러리 목록
├── README.md                         # 프로젝트 개요 및 실행 방법 가이드
├── main.py                           # FastAPI 앱 생성 및 미들웨어 설정
├── data/                             # (로컬 테스트용)
│   └── note/                         # 실제 .md 파일들이 저장되는 Git 리포지토리 위치
├── app/
│   ├── __init__.py
│   ├── core/
│   │   ├── config.py                 # .env 설정을 읽어오는 Pydantic Settings
│   │   └── exceptions.py             # NoteNotFoundError 등 커스텀 예외 정의
│   ├── database/
│   │   ├── session.py                # SQLAlchemy AsyncSession 설정
│   │   └── default_model_mixin.py    # UseStatEnum, 상속용 기본 컬럼 정의
│   ├── models/
│   │   ├── __init__.py
│   │   └── note.py                   # NoteMetadata 테이블 모델 정의
│   ├── routers/
│   │   ├── __init__.py
│   │   └── note_router.py            # /notes 관련 엔드포인트 정의 (Controller)
│   └── service/
│       ├── __init__.py
│       └── note_mng/
│           ├── note_mng_biz_service.py  # NoteService: 비즈니스 로직 중심
│           └── git_service.py           # GitService: 파일 I/O 및 Git 명령어 처리
└── tests/                            # 단위 테스트 코드 (선택 사항)
```