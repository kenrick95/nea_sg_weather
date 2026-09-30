# NEA Singapore Weather Integration for Home Assistant

## HA 2024.12 maintenance branch

This branch starts from upstream `v2.7.1` and targets Home Assistant Core 2024.12.3. It retains the `nea_sg_weather` integration domain, config entries, entity IDs, and unique IDs. The minimum HA version is set to the version used in integration tests.

Release `v2.7.1.3` incorporates upstream through `v2.9.0` (`4691c9e`): pollutant sensors, entity naming and region devices, reconfiguration, and map overlays. It uses HA 2024.12's concentration constants and `DeviceInfo.via_device` instead of newer APIs. Existing entity IDs and unique IDs are preserved; friendly names and device grouping change. All 30 pollutant sensors remain disabled by default.

To use this fork through HACS, add `kenrick95/nea_sg_weather` as a custom repository of type **Integration** and install `v2.7.1.3`. Restart Home Assistant. Keep the existing integration entry in Settings > Devices & Services. Release `v2.7.1.2` remains available for rollback. Updating the integration does not change which entities are selected. Reconfigure removes entities you explicitly switch off; switching them on again may require restoring their customizations. The example map needs the updated YAML toggles copied into your dashboard configuration.

For future maintenance, cherry-pick individual upstream fixes into `ha-2024.12`, review imports against Core 2024.12.3, run the unit and HA integration tests, and publish a new release with a matching manifest version.

[CHANGELOG](CHANGELOG.md)

Home Assistant Integration to get current weather information directly from Data.gov.sg weather API published by Singapore National Environment Agency (SG NEA)

![image](https://user-images.githubusercontent.com/57534857/142906976-9f28571f-290f-42e1-85a0-68ee23f917d8.png)

![image](https://user-images.githubusercontent.com/57534857/142907008-1e5b1f76-c054-4797-b73f-8ad0d22e6b4c.png)

## Installation

Add this integration to Home Assistant using HACS, or copy everything in `custom_components/nea_sg_weather` to your `custom_components` folder in your Home Assistant `config` folder. 

Follow the integration config flow to set up the following entities:
- `weather`: weather entity with 4 day forecasts
- `area` (town) sensors: current weather conditions for up to 47 areas/towns in Singapore
- `region` sensors: 24 hour weather condition forecast for North/South/East/West/Central regions of Singapore
- `rain` camera: 2 camera entities for static and animated rain map overlays updated every 5 minutes from NEA
- `rain` sensors: one rainfall sensor per active NEA station, fetched live from the API — stations are added and removed automatically as the API changes
- `pm25` sensors: 5 pm2.5 sensors for North/South/East/West/Central regions of Singapore
- `psi` sensors: 5 sensors with the 24-hour PSI for North/South/East/West/Central regions of Singapore; the 24-hour PM2.5 and the per-pollutant sub-indices are exposed as attributes
- `uv_index` sensor: UV index for Singapore

### Changing the configuration

To change which entities an instance sets up (weather entity, areas, region sensors, rain map and sensors, scan interval or timeout), open the integration's menu and choose **Reconfigure**; there is no need to remove and re-add it. The name and sensor prefix cannot be changed there, so existing entity IDs stay the same. Entities you switch off are removed when the integration reloads, and those you keep keep their settings.

### Devices and entity names

Each configured instance creates a device named after the instance (e.g. "Singapore Weather") holding the weather entity, the UV, area and rainfall sensors and the rain map cameras. When region sensors are enabled, each region gets its own device ("Central Singapore", "Northern Singapore", …) under the main device, holding that region's forecast, PM2.5 and PSI sensors.

Entity names follow Home Assistant's convention of device name plus entity name, e.g. "Singapore Weather UV index" or "Central Singapore PSI (24-hour)". Entity IDs are built from the configured prefix and do not depend on these names.


## Weather Map Overlays

Several `yaml` files are included to help you quickly set up a weather map card on Lovelace UI.
![image](https://user-images.githubusercontent.com/57534857/142712510-cabf3214-09c2-4fda-8d43-ff230aebd91c.png)

For the overlays to display properly, you will need the `area`, `region` and `rain` entities activated in the config flow (or switched on later with **Reconfigure**).

Besides the rain map and the town and region weather icons, the card can show NEA's own map overlays from the [rain areas page](https://www.nea.gov.sg/weather/rain-areas) — landmarks, townships, MRT stations and expressways — each with its own toggle, and NEA's rain intensity legend below the map.

1. `input_boolean.yaml`: to set up `input_boolean` toggles for the map overlays
2. `automations.yaml`: automations to manage how the map toggles work
3. `lovelace.yaml`: preset card config to display the weather map card

Instructions for how to integrate the `yaml` files are included in the various files in the `nea_sg_weather/yaml` folder.

## Rainfall sensors

Rainfall sensors are created dynamically from the live NEA API — no static station list is used. Orphaned sensors (stations decommissioned by NEA) are automatically removed from Home Assistant on startup and whenever the station list changes at runtime.

Sensors include location attributes so they can be displayed on a Lovelace map card.

For entity pictures to display correctly, copy all image files in `www/weather/` to your `config/www/weather/` folder.
![image](https://user-images.githubusercontent.com/57534857/171048147-5e6dcfd3-40c4-4eff-a09c-f1f6c31ddb92.png)
