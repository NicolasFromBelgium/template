"""Runtime and CI health checks.

`status()` is the small, stable surface that tests and CI assert against.
"""

from app import __version__


def status() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "template",
        "version": __version__,
    }


def is_healthy() -> bool:
    return status()["status"] == "ok"
