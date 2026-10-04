"""Gateway client moved here from acme-energy-data (DEMO-0019)."""
from acme_ingest.download import backoff_seconds


def plan_retries(max_attempts: int = 5) -> list[int]:
    return [s for a in range(1, max_attempts + 1) if (s := backoff_seconds(a)) is not None]
