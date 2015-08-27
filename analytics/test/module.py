import unittest

import analytics


class TestModule(unittest.TestCase):

    def failed(self):
        self.failed = True

    def setUp(self):
        self.failed = False
        analytics.key = 'testkey'
        analytics.secret = 'testsecret'
        analytics.on_error = self.failed
        analytics.debug = True

    def test_set_contact(self):
      analytics.set_contact('contact_uid')
      analytics.flush()

    def test_set_account(self):
      analytics.set_account('account_uid')
      analytics.flush()

    def test_track_event(self):
      analytics.track_event('contact_uid', 'event_uid')
      analytics.flush()

    def test_track_pageview(self):
      analytics.track_pageview('contact_uid')
      analytics.flush()

    def test_flush(self):
        analytics.flush()
