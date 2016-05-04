"""Defines Echo Reply message during the handshake"""

# System imports

# Third-party imports

# Local source tree imports
from ofp.v0x01.common import header as of_header
from ofp.v0x01.foundation import base

# Classes


class EchoReply(base.GenericStruct):
    """OpenFlow Reply message

    This message does not contain a body beyond the OpenFlow Header
        :param xid: xid to be used on the message header
    """
    header = of_header.Header()

    def __init__(self, xid=None):
        self.header.message_type = of_header.Type.OFPT_ECHO_REPLY
        self.header.length = 8
        self.header.xid = xid
