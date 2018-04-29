# -*- coding: utf-8 -*-

"""Weeb.sh API Wrapper for discord.py integration
"""

__title__ = 'weebapi'
__author__ = 'AndyTempel'
__license__ = 'MIT'
__copyright__ = 'Copyright 2018 AndyTempel'
__version__ = '0.1.11b'

import logging
from collections import namedtuple

from weebapi.data_objects import *
from weebapi.errors import *
from weebapi.client import Client

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')

version_info = VersionInfo(major=0, minor=1, micro=11, releaselevel='beta', serial=0)

try:
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

logging.getLogger(__name__).addHandler(NullHandler())
