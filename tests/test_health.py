"""Application health checks used by local tests and CI."""

from app import __version__
from app.__main__ import main
from app.health import is_healthy, status


def test_health_status_is_ok() -> None:
    info = status()
    assert info["status"] == "ok"
    assert info["service"] == "template"
    assert info["version"] == __version__


def test_is_healthy() -> None:
    assert is_healthy() is True


def test_main_prints_status(capsys) -> None:
    main()
    output = capsys.readouterr().out
    assert "template" in output
    assert "status=ok" in output
