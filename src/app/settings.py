"""Load settings from environment variables.

Reads `.env` from the project root when present (local development).
In CI and production, values come from the real environment.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
TRUE_VALUES = {"1", "true", "yes", "on"}


def _load_dotenv(path: Path) -> None:
    if not path.is_file():
        return
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        os.environ.setdefault(key, value)


def _as_bool(value: str) -> bool:
    return value.strip().lower() in TRUE_VALUES


@dataclass(frozen=True)
class Settings:
    app_env: str
    debug: bool
    log_level: str
    secret_key: str


def load_settings(env_file: Path | None = None) -> Settings:
    _load_dotenv(env_file or PROJECT_ROOT / ".env")
    return Settings(
        app_env=os.environ.get("APP_ENV", "development"),
        debug=_as_bool(os.environ.get("APP_DEBUG", "false")),
        log_level=os.environ.get("LOG_LEVEL", "info").lower(),
        secret_key=os.environ.get("SECRET_KEY", "change-me"),
    )
