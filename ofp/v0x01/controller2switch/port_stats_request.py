"""Information about physical ports is requested with OFPST_PORT"""

# System imports

# Third-party imports

# Local source tree imports
from ..foundation import base
from ..foundation import basic_types


class PortStatsRequest(base.GenericStruct):
    """
    Body for ofp_stats_request of type OFPST_PORT

        :param port_no -- OFPST_PORT message must request statistics either
                          for a single port (specified in port_no) or for
                          all ports (if port_no == OFPP_NONE).
        :param pad --

    """
    port_no = basic_types.UBInt16()
    pad = basic_types.UBInt8Array(length=6)

    def __init__(self, port_no=None, pad=None):

        self.port_no = port_no
        self.pad = pad
