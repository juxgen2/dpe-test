from forepaas.dwh.connect import connect
import logging

logger = logging.getLogger(__name__)


def customfunc(event):

    logger.info("Begin function A v2.1")
    