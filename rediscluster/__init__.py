# -*- coding: utf-8 -*-

# python std lib
import logging

# rediscluster imports
from rediscluster.client import RedisCluster
from rediscluster.connection import (
    ClusterBlockingConnectionPool,
    ClusterConnection,
    ClusterConnectionPool,
)
from rediscluster.exceptions import (
    RedisClusterException,
    RedisClusterError,
    ClusterDownException,
    ClusterError,
    ClusterCrossSlotError,
    ClusterDownError,
    AskError,
    TryAgainError,
    MovedError,
    MasterDownError,
)
from rediscluster.pipeline import ClusterPipeline


def int_or_str(value):
    try:
        return int(value)
    except ValueError:
        return value


# Major, Minor, Fix version
__version__ = '2.1.4+monetate.1'
# Treat the PEP 440 local separator as a component separator, so the local label lands in its own
# element and the fix version stays an int: 2.1.4+monetate.1 -> (2, 1, 4, 'monetate', 1). Versions
# with no local part are unaffected.
VERSION = tuple(map(int_or_str, __version__.replace('+', '.').split('.')))

__all__ = [
    'AskError',
    'ClusterBlockingConnectionPool',
    'ClusterConnection',
    'ClusterConnectionPool',
    'ClusterCrossSlotError',
    'ClusterDownError',
    'ClusterDownException',
    'ClusterError',
    'ClusterPipeline',
    'MasterDownError',
    'MovedError',
    'RedisCluster',
    'RedisClusterError',
    'RedisClusterException',
    'TryAgainError',
]

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
