import unittest

from ofp.v0x01.common.header import OFPHeader
from ofp.v0x01.controller2switch.stats_reply import StatsReply

class TestStatsReply(unittest.TestCase):
    def test_get_size(self):
        sr = StatsReply(OFPHeader(), 3, 1)
        self.assertEqual(sr.get_size(), 12)

    def test_pack(self):
        sr = StatsReply(OFPHeader(), 3, 1)
        sr.pack()

    def test_unpack(self):
        pass
