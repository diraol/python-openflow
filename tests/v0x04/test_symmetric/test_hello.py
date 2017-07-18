"""Hello message tests."""
from pyof.v0x04.symmetric.hello import Hello
from tests.test_struct import TestStruct


class TestHello(TestStruct):
    """Hello message tests (also those in :class:`.TestDump`)."""

    @classmethod
    def setUpClass(cls):
        """Configure raw file and its object in parent class (TestDump)."""
        super().setUpClass()
        super().set_raw_dump_file('v0x04', 'ofpt_hello')
        super().set_raw_dump_object(Hello, xid=1)
        super().set_minimum_size(8)

    def test_hello_attributes(self):
        obj = self.get_raw_object()
        print(obj, obj.header, obj.header.version, obj.header.message_type)
        self.assertEqual(obj.header.version, 4)
        self.assertEqual(obj.header.message_type, 0)
        self.assertEqual(obj.header.xid, 1)
        obj.update_header_length()
        self.assertEqual(obj.header.length, 8)

