"""Entry point: python -m app"""

from app.health import status


def main() -> None:
    info = status()
    print(f"{info['service']} {info['version']} status={info['status']}")


if __name__ == "__main__":
    main()
