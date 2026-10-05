import sys
import unittest

sys.path.insert(0, "src")
from acme_ingest.client import plan_retries  # noqa: E402


class Client(unittest.TestCase):
    def test_plan(self):
        self.assertEqual(plan_retries(3), [2, 4, 8])
