# adapters/primary/cookies.py
from datetime import timedelta

REFRESH_COOKIE_NAME = "refresh_token"
REFRESH_COOKIE_PATH = "/auth/"
REFRESH_COOKIE_MAX_AGE = timedelta(days=7)


def set_refresh_cookie(response, refresh_token: str) -> None:
    response.set_cookie(
        key=REFRESH_COOKIE_NAME,
        value=refresh_token,
        max_age=int(REFRESH_COOKIE_MAX_AGE.total_seconds()),
        path=REFRESH_COOKIE_PATH,
        httponly=True,
        samesite="Lax",
    )


def clear_refresh_cookie(response) -> None:
    response.delete_cookie(REFRESH_COOKIE_NAME, path=REFRESH_COOKIE_PATH)


def read_refresh_cookie(request) -> str | None:
    return request.COOKIES.get(REFRESH_COOKIE_NAME)
