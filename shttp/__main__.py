import typer
from typer import Option

from shttp.types import HTTPMethod


def main(
    url: str,
    method: HTTPMethod = Option(HTTPMethod.GET, "--method", "-m"),
    headers: list[str] = Option([], "--header", "-h"),
    data: str = Option(None, "--data", "-d"),
) -> None:
    print(f"URL: {url}")
    print(f"Method: {method}")
    print(f"Headers: {headers}")
    print(f"Data: {data}")


if __name__ == "__main__":
    typer.run(main)
