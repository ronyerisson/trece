"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PACKAGE_NAME = "trece"

_ = MessageFactory("trece")

logger = logging.getLogger("trece")
