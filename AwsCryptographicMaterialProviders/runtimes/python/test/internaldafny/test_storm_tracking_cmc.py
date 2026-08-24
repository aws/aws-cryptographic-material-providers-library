# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0
"""Unit tests for the StormTrackingCMC extern."""
from unittest.mock import patch

from aws_cryptographic_material_providers.internaldafny.extern.StormTrackingCMC import (
    StormTrackingCMC,
)


class _FakeCacheValue:
    def __init__(self, is_full=False, is_empty_fetch=False, data=None):
        self.is_Full = is_full
        self.is_EmptyFetch = is_empty_fetch
        self.data = data


class _FakeResult:
    def __init__(self, is_failure=False, error=None, value=None):
        self.is_Failure = is_failure
        self.error = error
        self.value = value


class _FakeWrapped:
    def __init__(self, results, sleep_milli, in_flight_ttl):
        self._results = list(results)
        self.sleepMilli = sleep_milli
        self.inFlightTTL = in_flight_ttl

    def GetFromCache(self, input):
        return self._results.pop(0)


def test_get_cache_entry_sleep_time():
    sleep_milli = 20
    pending = _FakeResult(value=_FakeCacheValue())
    full = _FakeResult(value=_FakeCacheValue(is_full=True, data="entry"))
    cmc = StormTrackingCMC(_FakeWrapped([pending, full], sleep_milli, in_flight_ttl=60 * 1000))

    with patch("time.sleep") as mock_sleep:
        result = cmc.GetCacheEntry_k(input=None)

    assert result.value == "entry"
    mock_sleep.assert_called_once_with(sleep_milli / 1000)
