import unittest

try:
    from queue import Queue
except:
    from Queue import Queue

from analytics.consumer import Consumer


class TestConsumer(unittest.TestCase):

    def test_next(self):
        q = Queue()
        consumer = Consumer(q, '')
        q.put(1)
        next = consumer.next()
        self.assertEqual(next, [1])

    def test_next_limit(self):
        q = Queue()
        upload_size = 50
        consumer = Consumer(q, '', upload_size=upload_size)
        for i in range(10000):
            q.put(i)
        next = consumer.next()
        self.assertEqual(next, list(range(upload_size)))

    def test_upload(self):
        q = Queue()
        consumer  = Consumer(q, 'fWlU0N6jJKbcgW_OR6OidQ', 'UZ8YjpEXXPBYmROvPnJ5jw')
        track = {
            'method': 'set_contact',
            'contact_uid': 'contact_uid'
        }
        consumer.request([track])
        q.put(track)
        success = consumer.upload()
        self.assertTrue(success)

    def test_request(self):
        consumer = Consumer(None, 'fWlU0N6jJKbcgW_OR6OidQ', 'UZ8YjpEXXPBYmROvPnJ5jw')
        track = {
            'method': 'set_contact',
            'contact_uid': 'contact_uid'
        }
        consumer.request([track])

    def test_pause(self):
        consumer = Consumer(None, 'testsecret')
        consumer.pause()
        self.assertFalse(consumer.running)
