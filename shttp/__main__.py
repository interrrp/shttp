import requests
import typer
from typer import Option

from shttp.types import HTTPMethod


def main(
    url: str,
    method: HTTPMethod = Option(HTTPMethod.GET, "--method", "-m"),
    headers: list[str] = Option([], "--header", "-h"),
    data: str = Option(None, "--data", "-d"),
) -> None:
    response = requests.request(
        url=url,
        method=method,
        headers=dict(header.split(":") for header in headers),
        data=data,
    )

    typer.echo(f"{response.status_code} {response.reason}")
    typer.echo(response.text)


if __name__ == "__main__":
    typer.run(main)
