# NEA Singapore Weather Integration for Home Assistant

## HA 2024.12 maintenance branch

This branch starts from upstream `v2.7.1`, which has been confirmed working on Home Assistant Core 2024.12.3. It retains the `nea_sg_weather` integration domain and existing config entries. The integration manifest declares a minimum of HA 2024.6.0; Core 2024.12.3 is the tested user version, not a promise that every intervening release has been tested.

Upstream `v2.8.0` raises the minimum to HA 2026.9.0 and imports `ChildDeviceInfo` for region devices. Do not merge that release into this branch without an explicit HA 2024 compatibility port and runtime test.

To use this branch through HACS, publish this repository to your GitHub account, create a release from the `v2.7.1.1` tag, and add `<owner>/<repository>` as a HACS custom repository of type **Integration**. Install it over the existing `custom_components/nea_sg_weather` files, then restart Home Assistant. Keep a backup of that directory first. Do not remove the integration from Settings > Devices & Services; that would discard its config entry. Do not install the upstream repository and this fork at the same time because both provide the same domain.

For future maintenance, cherry-pick individual upstream fixes into `ha-2024.12`, review imports against Core 2024.12.3, run the tests, and publish a new release with a matching manifest version.

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


## Weather Map Overlays

Several `yaml` files are included to help you quickly set up a weather map card on Lovelace UI.
![image](https://user-images.githubusercontent.com/57534857/142712510-cabf3214-09c2-4fda-8d43-ff230aebd91c.png)

For the overlays to display properly, you will need the `area`, `region` and `rain` entities activated in the config flow.

1. `input_boolean.yaml`: to set up `input_boolean` toggles for the map overlays
2. `automations.yaml`: automations to manage how the map toggles work
3. `lovelace.yaml`: preset card config to display the weather map card

Instructions for how to integrate the `yaml` files are included in the various files in the `nea_sg_weather/yaml` folder.

## Rainfall sensors

Rainfall sensors are created dynamically from the live NEA API — no static station list is used. Orphaned sensors (stations decommissioned by NEA) are automatically removed from Home Assistant on startup and whenever the station list changes at runtime.

Sensors include location attributes so they can be displayed on a Lovelace map card.

For entity pictures to display correctly, copy all image files in `www/weather/` to your `config/www/weather/` folder.
![image](https://user-images.githubusercontent.com/57534857/171048147-5e6dcfd3-40c4-4eff-a09c-f1f6c31ddb92.png)
