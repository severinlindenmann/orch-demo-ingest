"""Download gateway exports with retry and backoff."""


def backoff_seconds(attempt: int, retry_after: int | None = None) -> int | None:
    """Seconds to wait before retry `attempt` (1-based); None means give up."""
    if attempt > 5:
        return None
    if retry_after is not None:
        return retry_after
    return min(2 ** attempt, 60)


def parse_export(text: str) -> list[dict]:
    if not text.strip():
        return []
    header, *rows = text.splitlines()
    names = header.split(",")
    return [dict(zip(names, row.split(","))) for row in rows if row]
