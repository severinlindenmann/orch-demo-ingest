import sys
import unittest

sys.path.insert(0, "src")
from acme_ingest.download import backoff_seconds, parse_export  # noqa: E402


class Backoff(unittest.TestCase):
    def test_grows_and_gives_up(self):
        self.assertEqual([backoff_seconds(a) for a in (1, 2, 6)], [2, 4, None])

    def test_retry_after_wins(self):
        self.assertEqual(backoff_seconds(1, retry_after=9), 9)


class Parse(unittest.TestCase):
    def test_rows(self):
        self.assertEqual(parse_export("meter,kwh\nm1,3\n"), [{"meter": "m1", "kwh": "3"}])
