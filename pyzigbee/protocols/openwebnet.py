#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015 Legrand France
# All rights reserved

import re
import logging
from pyzigbee.protocols.baseprotocol import BaseProtocol
from pyzigbee.core.exceptions import PyZigBeeBadFormatError

class OWNProtocol(BaseProtocol):
    """OWN protocol is in charge of decoding/encoding OpenWebNet frames"""

    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def _build_where_field(self, zigbee_id=None):
        if zigbee_id is None:
            return ""
        else:
            return zigbee_id

    def get_info(self):

        return { "description": "OpenWebNet protocol" }

    def get_end_of_frame_sep(self):

        return "##"

    def encode_get_dev_number(self):
        """Build the frames sequence to get the number of devices"""

        return [ { "tx": "*13*65*##" },
                 { "rx": "*#*1##" },
                 { "delay": 5 },
                 { "answer": ""} ]

    def decode_dev_number(self, data):
        """Decode the given data to find the number of devices"""

        m = re.match("\*\#13\*\*67\*(\S+)\#\#", data)
        if m is not None:
            dev_nb = int(m.group(1))
            self.logger.debug("number of devices: %d", dev_nb)
            return dev_nb
        else:
            raise PyZigBeeBadFormatError("OWN: could not extract device number from frame: %s" % data)

    def encode_get_dev_id(self, dev_index):
        """Build the frames sequence to get the device ID from a given device index"""

        return [ { "tx": "*#13**66#%d##" % dev_index},
                 { "answer": ""} ]

    def decode_dev_id(self, data):
        """Decode the given data to find the device ID"""

        m = re.match("\*\#13\*(.*)\#.*\#.*\#\#", data)
        if m is not None:
            dev_id = m.group(1)
            self.logger.debug("device ID: %s", dev_id)
            return dev_id
        else:
            raise PyZigBeeBadFormatError("OWN: could not extract device ID from frame: %s" % data)

    def encode_get_firmware_version(self, zigbee_id=None):
        """Build the frames sequence to get the firmware version of the gateway"""

        return [ { "tx": "*#13*%s*16##" % self._build_where_field(zigbee_id)},
                 { "answer": ""} ]

    def encode_get_hardware_version(self, zigbee_id=None):
        """Build the frames sequence to get the firmware version of the gateway"""

        return [ { "tx": "*#13*%s*17##" % self._build_where_field(zigbee_id) },
                 { "rx": "*#*1##"},
                 { "answer": ""} ]

    def decode_firmware_version(self, data, zigbee_id=None):

        return self._decode_version(data, "16", zigbee_id)

    def decode_hardware_version(self, data, zigbee_id=None):

        return self._decode_version(data, "17", zigbee_id)

    def _decode_version(self, data, code="16", zigbee_id=None):
        """Decode the given data to find the version"""

        escaped_id = re.escape(self._build_where_field(zigbee_id))
        m = re.match("\*\#13\*%s\*%s\*(\S+)\*(\S+)\*(\S+)\#\#" % (escaped_id, code), data)
        if m is not None:
            version = m.group(1) + "." + m.group(2) + "." + m.group(3)
            self.logger.debug("version: %s", version)
            return version
        else:
            raise PyZigBeeBadFormatError("OWN: could not extract gateway version from frame: %s" % data)
