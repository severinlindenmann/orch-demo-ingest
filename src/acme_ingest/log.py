"""Structured log events (WIP)."""


def event(name: str, **fields) -> dict:
    return {"event": name, **fields}
