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
        headers=parse_headers(headers),
        params=dict(param.split("=") for param in params),
        data=body,
    )

    typer.echo(f"{response.status_code} {response.reason}")
    typer.echo(response.text)


def parse_headers(headers_arg: list[str]) -> dict[str, str]:
    """Parse the :code:`headers` argument into a dictionary.

    :param headers_arg: A list of headers in the format :code:`key: value` (whitespace
        around the colon are stripped).
    """

    headers = {}
    for header in headers_arg:
        key, value = header.split(":", 1)
        headers[key.strip()] = value.strip()
    return headers


def main_wrapper() -> None:
    """A wrapper to run :func:`main` for the Poetry script system."""
    typer.run(main)


if __name__ == "__main__":
    main_wrapper()
