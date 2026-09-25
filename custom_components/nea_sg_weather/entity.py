"""Device info shared by the NEA Singapore Weather entity platforms."""
from __future__ import annotations

from homeassistant.helpers.device_registry import DeviceInfo

from .const import DOMAIN


def main_device_info(entry_id: str) -> DeviceInfo:
    """Return device info for the config entry's main device.

    The device itself is registered in async_setup_entry.
    """
    return DeviceInfo(identifiers={(DOMAIN, entry_id)})


REGION_DEVICE_NAMES = {
    "Central": "Central Singapore",
    "North": "Northern Singapore",
    "South": "Southern Singapore",
    "East": "Eastern Singapore",
    "West": "Western Singapore",
}


def region_device_info(coordinator, entry_id: str, region: str) -> DeviceInfo:
    """Return device info for a region's child device (e.g. Central Singapore)."""
    return DeviceInfo(
        identifiers={(DOMAIN, f"{entry_id}_{region.lower()}")},
        name=REGION_DEVICE_NAMES[region],
        via_device=(DOMAIN, entry_id),
    )
