import requests
import typer
from typer import Option

from shttp.types import HTTPMethod


def main(
    url: str,
    method: HTTPMethod = Option(HTTPMethod.GET, "--method", "-m"),
    headers: list[str] = Option([], "--header", "-h"),
    params: list[str] = Option([], "--param", "-p"),
    body: str = Option(None, "--body", "-b"),
) -> None:
    response = requests.request(
        url=url,
        method=method,
        headers=dict(header.split(":") for header in headers),
        params=dict(param.split("=") for param in params),
        data=body,
    )

    typer.echo(f"{response.status_code} {response.reason}")
    typer.echo(response.text)


if __name__ == "__main__":
    typer.run(main)
